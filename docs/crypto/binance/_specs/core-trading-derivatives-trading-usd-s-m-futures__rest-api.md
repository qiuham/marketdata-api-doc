---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:18.923996
---

# core-trading-derivatives-trading-usd-s-m-futures__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Futures (USDⓈ-M) REST API
  description: Access market data, manage accounts, and trade USDⓈ-M perpetual futures.
  x-description-cn: 访问市场数据、管理账户，并交易 USDⓈ-M 永续合约。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
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
  - name: convert
    x-displayName: Convert
    x-displayName-cn: 合约钱包闪兑
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
  - url: https://fapi.binance.com
  - url: https://testnet.binancefuture.com
paths:
  /fapi/v2/account:
    get:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#account-information-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/accountInformationV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/account_information_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/account_information_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/AccountInformationV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/AccountInformationV2/AccountInformationV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/AccountInformationV2Example.php
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
          description: Account Information V2
          x-description-cn: 账户 信息 V2
          content:
            application/json:
              schema:
                type: object
                properties:
                  feeTier:
                    type: integer
                    example: 0
                    format: int64
                    description: Account commission tier.
                    x-description-cn: 手续费等级。
                  feeBurn:
                    type: boolean
                    example: true
                    description: Whether fee discount is enabled.
                    x-description-cn: 是否开启手续费抵扣。
                  canTrade:
                    type: boolean
                    example: true
                    description: Whether trading is enabled.
                    x-description-cn: 是否可以交易。
                  canDeposit:
                    type: boolean
                    example: true
                    description: Whether transfer-in is enabled.
                    x-description-cn: 是否可以入金。
                  canWithdraw:
                    type: boolean
                    example: true
                    description: Whether transfer-out is enabled.
                    x-description-cn: 是否可以出金。
                  updateTime:
                    type: integer
                    example: 0
                    format: int64
                    description: Reserved field, ignore.
                    x-description-cn: 保留字段，可忽略。
                  multiAssetsMargin:
                    type: boolean
                    example: true
                    description: Whether multi-assets mode is enabled.
                    x-description-cn: 是否开启多资产模式。
                  tradeGroupId:
                    type: integer
                    example: -1
                    format: int64
                    description: Trade group identifier.
                    x-description-cn: 交易组 ID。
                  totalInitialMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Total initial margin requirement. USDT only in single-asset mode; the sum of USD value of all
                      cross positions/open order initial margin in multi-assets mode.
                    x-description-cn: 起始保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓/挂单起始保证金的美元价值总和。
                  totalMaintMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Total maintenance margin requirement. USDT only in single-asset mode; the sum of USD value of all
                      cross positions maintenance margin in multi-assets mode.
                    x-description-cn: 维持保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓维持保证金的美元价值总和。
                  totalWalletBalance:
                    type: string
                    example: "126.72469206"
                    description: Total wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 账户总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalUnrealizedProfit:
                    type: string
                    example: "0.00000000"
                    description: Total unrealized profit. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalMarginBalance:
                    type: string
                    example: "126.72469206"
                    description: Total margin balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 保证金总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalPositionInitialMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Initial margin required for positions. USDT only in single-asset mode; the sum of USD value of all
                      cross positions initial margin in multi-assets mode.
                    x-description-cn: 持仓所需起始保证金。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓起始保证金的美元价值总和。
                  totalOpenOrderInitialMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Initial margin required for open orders. USDT only in single-asset mode; USD-denominated in
                      multi-assets mode.
                    x-description-cn: 当前挂单所需起始保证金。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalCrossWalletBalance:
                    type: string
                    example: "126.72469206"
                    description: Cross wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 全仓账户余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalCrossUnPnl:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Unrealized PnL for cross positions. USDT only in single-asset mode; USD-denominated in
                      multi-assets mode.
                    x-description-cn: 全仓持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  availableBalance:
                    type: string
                    example: "126.72469206"
                    description: Available balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 可用余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  maxWithdrawAmount:
                    type: string
                    example: "126.72469206"
                    description: >-
                      Maximum transferable/withdrawable amount. USDT only in single-asset mode; a maximum virtual USD
                      amount in multi-assets mode.
                    x-description-cn: 最大可转出余额。单资产模式下仅计 USDT；多资产模式下为可转出的最大虚拟美元金额。
                  assets:
                    type: array
                    description: Asset-level account details.
                    x-description-cn: 资产维度账户信息。
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                          description: Asset name.
                          x-description-cn: 资产名称。
                        walletBalance:
                          type: string
                          example: "23.72469206"
                          description: Wallet balance.
                          x-description-cn: 钱包余额。
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: Unrealized profit.
                          x-description-cn: 未实现盈亏。
                        marginBalance:
                          type: string
                          example: "23.72469206"
                          description: Margin balance.
                          x-description-cn: 保证金余额。
                        maintMargin:
                          type: string
                          example: "0.00000000"
                          description: Maintenance margin requirement.
                          x-description-cn: 维持保证金。
                        initialMargin:
                          type: string
                          example: "0.00000000"
                          description: Total initial margin requirement.
                          x-description-cn: 所需起始保证金。
                        positionInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: Initial margin required for positions.
                          x-description-cn: 持仓所需起始保证金。
                        openOrderInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: Initial margin required for open orders.
                          x-description-cn: 当前挂单所需起始保证金。
                        crossWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: Cross wallet balance.
                          x-description-cn: 全仓账户余额。
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: Unrealized PnL for cross positions.
                          x-description-cn: 全仓持仓未实现盈亏。
                        availableBalance:
                          type: string
                          example: "126.72469206"
                          description: Available balance.
                          x-description-cn: 可用余额。
                        maxWithdrawAmount:
                          type: string
                          example: "23.72469206"
                          description: Maximum transferable/withdrawable amount.
                          x-description-cn: 最大可转出余额。
                        marginAvailable:
                          type: boolean
                          example: true
                          description: Whether the asset can be used as margin in multi-assets mode.
                          x-description-cn: 在多资产模式下，该资产是否可作为保证金。
                        updateTime:
                          type: integer
                          example: 1625474304765
                          format: int64
                          description: Last update time in milliseconds.
                          x-description-cn: 最后更新时间（毫秒）。
                  positions:
                    type: array
                    description: Position details for symbols. One-way mode returns BOTH; hedge mode returns LONG/SHORT.
                    x-description-cn: 各交易对持仓信息。单向模式返回 BOTH，双向模式返回 LONG/SHORT。
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          description: Symbol.
                          x-description-cn: 交易对。
                        initialMargin:
                          type: string
                          example: "0"
                          description: Initial margin requirement.
                          x-description-cn: 所需起始保证金。
                        maintMargin:
                          type: string
                          example: "0"
                          description: Maintenance margin requirement.
                          x-description-cn: 维持保证金。
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: Unrealized profit.
                          x-description-cn: 持仓未实现盈亏。
                        positionInitialMargin:
                          type: string
                          example: "0"
                          description: Initial margin required for positions.
                          x-description-cn: 持仓所需起始保证金。
                        openOrderInitialMargin:
                          type: string
                          example: "0"
                          description: Initial margin required for open orders.
                          x-description-cn: 当前挂单所需起始保证金。
                        leverage:
                          type: string
                          example: "100"
                          description: Current initial leverage.
                          x-description-cn: 当前杠杆倍数。
                        isolated:
                          type: boolean
                          example: true
                          description: Whether the position uses isolated margin mode.
                          x-description-cn: 是否为逐仓模式。
                        entryPrice:
                          type: string
                          example: "0.00000"
                          description: Average entry price.
                          x-description-cn: 持仓成本价。
                        maxNotional:
                          type: string
                          example: "250000"
                          description: Maximum available notional under current leverage.
                          x-description-cn: 当前杠杆下可用最大名义价值。
                        bidNotional:
                          type: string
                          example: "0"
                          description: Bid notional (ignore).
                          x-description-cn: 买单名义价值（可忽略）。
                        askNotional:
                          type: string
                          example: "0"
                          description: Ask notional (ignore).
                          x-description-cn: 卖单名义价值（可忽略）。
                        positionSide:
                          type: string
                          example: BOTH
                          description: Position side.
                          x-description-cn: 持仓方向。
                        positionAmt:
                          type: string
                          example: "0"
                          description: Position quantity.
                          x-description-cn: 持仓数量。
                        updateTime:
                          type: integer
                          example: 0
                          format: int64
                          description: Last update time in milliseconds.
                          x-description-cn: 最后更新时间（毫秒）。
                      description: positions of all symbols in the market are returned
                      x-description-cn: 头寸，将返回所有市场symbol。
  /fapi/v3/account:
    get:
      summary: Account Information V3 (USER_DATA)
      x-summary-cn: 账户信息V3 (USER_DATA)
      description: >-
        Get current account information. User in single-asset/ multi-assets mode will see different value, see comments
        in response section for detail.
      x-description-cn: 现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。
      tags:
        - account
      operationId: accountInformationV3
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#account-information-v3
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/accountInformationV3.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/account_information_v3.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/account_information_v3.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/AccountInformationV3Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/AccountInformationV3/AccountInformationV3.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/AccountInformationV3Example.php
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
          description: Account Information V3
          x-description-cn: 账户 信息 V3
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalInitialMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Total initial margin requirement. USDT only in single-asset mode; the sum of USD value of all
                      cross positions/open order initial margin in multi-assets mode.
                    x-description-cn: 起始保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓/挂单起始保证金的美元价值总和。
                  totalMaintMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Total maintenance margin requirement. USDT only in single-asset mode; the sum of USD value of all
                      cross positions maintenance margin in multi-assets mode.
                    x-description-cn: 维持保证金总额。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓维持保证金的美元价值总和。
                  totalWalletBalance:
                    type: string
                    example: "126.72469206"
                    description: Total wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 账户总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalUnrealizedProfit:
                    type: string
                    example: "0.00000000"
                    description: Total unrealized profit. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalMarginBalance:
                    type: string
                    example: "126.72469206"
                    description: Total margin balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 保证金总余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalPositionInitialMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Initial margin required for positions. USDT only in single-asset mode; the sum of USD value of all
                      cross positions initial margin in multi-assets mode.
                    x-description-cn: 持仓所需起始保证金。单资产模式下仅计 USDT；多资产模式下为全部全仓持仓起始保证金的美元价值总和。
                  totalOpenOrderInitialMargin:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Initial margin required for open orders. USDT only in single-asset mode; USD-denominated in
                      multi-assets mode.
                    x-description-cn: 当前挂单所需起始保证金。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalCrossWalletBalance:
                    type: string
                    example: "126.72469206"
                    description: Cross wallet balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 全仓账户余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  totalCrossUnPnl:
                    type: string
                    example: "0.00000000"
                    description: >-
                      Unrealized PnL for cross positions. USDT only in single-asset mode; USD-denominated in
                      multi-assets mode.
                    x-description-cn: 全仓持仓未实现盈亏总额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  availableBalance:
                    type: string
                    example: "126.72469206"
                    description: Available balance. USDT only in single-asset mode; USD-denominated in multi-assets mode.
                    x-description-cn: 可用余额。单资产模式下仅计 USDT；多资产模式下以美元计价。
                  maxWithdrawAmount:
                    type: string
                    example: "126.72469206"
                    description: >-
                      Maximum transferable/withdrawable amount. USDT only in single-asset mode; a maximum virtual USD
                      amount in multi-assets mode.
                    x-description-cn: 最大可转出余额。单资产模式下仅计 USDT；多资产模式下为可转出的最大虚拟美元金额。
                  assets:
                    type: array
                    description: Asset-level account details.
                    x-description-cn: 资产维度账户信息。
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                          description: Asset name.
                          x-description-cn: 资产名称。
                        walletBalance:
                          type: string
                          example: "23.72469206"
                          description: Wallet balance.
                          x-description-cn: 钱包余额。
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: Unrealized profit.
                          x-description-cn: 未实现盈亏。
                        marginBalance:
                          type: string
                          example: "23.72469206"
                          description: Margin balance.
                          x-description-cn: 保证金余额。
                        maintMargin:
                          type: string
                          example: "0.00000000"
                          description: Maintenance margin requirement.
                          x-description-cn: 维持保证金。
                        initialMargin:
                          type: string
                          example: "0.00000000"
                          description: Total initial margin requirement.
                          x-description-cn: 所需起始保证金。
                        positionInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: Initial margin required for positions.
                          x-description-cn: 持仓所需起始保证金。
                        openOrderInitialMargin:
                          type: string
                          example: "0.00000000"
                          description: Initial margin required for open orders.
                          x-description-cn: 当前挂单所需起始保证金。
                        crossWalletBalance:
                          type: string
                          example: "23.72469206"
                          description: Cross wallet balance.
                          x-description-cn: 全仓账户余额。
                        crossUnPnl:
                          type: string
                          example: "0.00000000"
                          description: Unrealized PnL for cross positions.
                          x-description-cn: 全仓持仓未实现盈亏。
                        availableBalance:
                          type: string
                          example: "23.72469206"
                          description: Available balance.
                          x-description-cn: 可用余额。
                        maxWithdrawAmount:
                          type: string
                          example: "23.72469206"
                          description: Maximum transferable/withdrawable amount.
                          x-description-cn: 最大可转出余额。
                        updateTime:
                          type: integer
                          example: 1625474304765
                          format: int64
                          description: Last update time in milliseconds.
                          x-description-cn: 最后更新时间（毫秒）。
                      description: For assets that are quote assets, USDT/USDC/BTC
                      x-description-cn: For assets that are quote assets, USDT/USDC/BTC
                  positions:
                    type: array
                    description: Position details for symbols.
                    x-description-cn: 各交易对持仓信息。
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          description: Symbol.
                          x-description-cn: 交易对。
                        positionSide:
                          type: string
                          example: BOTH
                          description: Position side.
                          x-description-cn: 持仓方向。
                        positionAmt:
                          type: string
                          example: "1.000"
                          description: Position quantity.
                          x-description-cn: 持仓数量。
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                          description: Unrealized profit.
                          x-description-cn: 持仓未实现盈亏。
                        isolatedMargin:
                          type: string
                          example: "0.00000000"
                          description: Isolated margin.
                          x-description-cn: 逐仓保证金。
                        notional:
                          type: string
                          example: "0"
                          description: Position notional value.
                          x-description-cn: 持仓名义价值。
                        isolatedWallet:
                          type: string
                          example: "0"
                          description: Isolated wallet balance.
                          x-description-cn: 逐仓钱包余额。
                        initialMargin:
                          type: string
                          example: "0"
                          description: Initial margin requirement.
                          x-description-cn: 所需起始保证金。
                        maintMargin:
                          type: string
                          example: "0"
                          description: Maintenance margin requirement.
                          x-description-cn: 维持保证金。
                        updateTime:
                          type: integer
                          example: 0
                          format: int64
                          description: Last update time in milliseconds.
                          x-description-cn: 最后更新时间（毫秒）。
                      description: positions of all symbols user had position/ open orders are returned
                      x-description-cn: 仅有仓位或挂单的交易对会被返回
  /fapi/v2/balance:
    get:
      summary: Futures Account Balance V2 (USER_DATA)
      x-summary-cn: 账户余额V2 (USER_DATA)
      description: Query account balance information.
      x-description-cn: 查询账户余额信息。
      tags:
        - account
      operationId: futuresAccountBalanceV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#futures-account-balance-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/futuresAccountBalanceV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/futures_account_balance_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/futures_account_balance_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/FuturesAccountBalanceV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/FuturesAccountBalanceV2/FuturesAccountBalanceV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/FuturesAccountBalanceV2Example.php
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
            maximum: 60000
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
      responses:
        "200":
          description: Futures Account Balance V2
          x-description-cn: 合约 账户 Balance V2
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
                      description: Unique account alias.
                      x-description-cn: 唯一账户别名。
                    asset:
                      type: string
                      example: USDT
                      description: Asset name.
                      x-description-cn: 资产名称。
                    balance:
                      type: string
                      example: "122607.35137903"
                      description: Wallet balance.
                      x-description-cn: 钱包余额。
                    crossWalletBalance:
                      type: string
                      example: "23.72469206"
                      description: Cross wallet balance.
                      x-description-cn: 全仓钱包余额。
                    crossUnPnl:
                      type: string
                      example: "0.00000000"
                      description: Unrealized PnL of cross positions.
                      x-description-cn: 全仓持仓未实现盈亏。
                    availableBalance:
                      type: string
                      example: "23.72469206"
                      description: Available balance.
                      x-description-cn: 可用余额。
                    maxWithdrawAmount:
                      type: string
                      example: "23.72469206"
                      description: Maximum transferable/withdrawable amount.
                      x-description-cn: 最大可转出余额。
                    marginAvailable:
                      type: boolean
                      example: true
                      description: Whether the asset can be used as margin in multi-assets mode.
                      x-description-cn: 在多资产模式下，该资产是否可作为保证金。
                    updateTime:
                      type: integer
                      example: 1617939110373
                      format: int64
                      description: Last update time in milliseconds.
                      x-description-cn: 最后更新时间（毫秒）。
  /fapi/v3/balance:
    get:
      summary: Futures Account Balance V3 (USER_DATA)
      x-summary-cn: 账户余额V3 (USER_DATA)
      description: Query account balance information.
      x-description-cn: 查询账户余额信息。
      tags:
        - account
      operationId: futuresAccountBalanceV3
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#futures-account-balance-v3
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/futuresAccountBalanceV3.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/futures_account_balance_v3.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/futures_account_balance_v3.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/FuturesAccountBalanceV3Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/FuturesAccountBalanceV3/FuturesAccountBalanceV3.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/FuturesAccountBalanceV3Example.php
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
            maximum: 60000
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
      responses:
        "200":
          description: Futures Account Balance V3
          x-description-cn: 合约 账户 Balance V3
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
                      description: Unique account alias.
                      x-description-cn: 唯一账户别名。
                    asset:
                      type: string
                      example: USDT
                      description: Asset name.
                      x-description-cn: 资产名称。
                    balance:
                      type: string
                      example: "122607.35137903"
                      description: Wallet balance.
                      x-description-cn: 钱包余额。
                    crossWalletBalance:
                      type: string
                      example: "23.72469206"
                      description: Cross wallet balance.
                      x-description-cn: 全仓钱包余额。
                    crossUnPnl:
                      type: string
                      example: "0.00000000"
                      description: Unrealized PnL of cross positions.
                      x-description-cn: 全仓持仓未实现盈亏。
                    availableBalance:
                      type: string
                      example: "23.72469206"
                      description: Available balance.
                      x-description-cn: 可用余额。
                    maxWithdrawAmount:
                      type: string
                      example: "23.72469206"
                      description: Maximum transferable/withdrawable amount.
                      x-description-cn: 最大可转出余额。
                    marginAvailable:
                      type: boolean
                      example: true
                      description: Whether the asset can be used as margin in multi-assets mode.
                      x-description-cn: 在多资产模式下，该资产是否可作为保证金。
                    updateTime:
                      type: integer
                      example: 1617939110373
                      format: int64
                      description: Last update time in milliseconds.
                      x-description-cn: 最后更新时间（毫秒）。
  /fapi/v1/accountConfig:
    get:
      summary: Futures Account Configuration (USER_DATA)
      x-summary-cn: 账户配置 (USER_DATA)
      description: Query account configuration
      x-description-cn: 查询账户 configuration
      tags:
        - account
      operationId: futuresAccountConfiguration
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#futures-account-configuration
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/futuresAccountConfiguration.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/futures_account_configuration.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/futures_account_configuration.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/FuturesAccountConfigurationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/FuturesAccountConfiguration/FuturesAccountConfiguration.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/FuturesAccountConfigurationExample.php
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
          description: Futures Account Configuration
          x-description-cn: 合约 账户 Configuration
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
                  updateTime:
                    type: integer
                    example: 0
                    format: int64
                    description: reserved property, please ignore
                    x-description-cn: 忽略
                  multiAssetsMargin:
                    type: boolean
                    example: false
                  tradeGroupId:
                    type: integer
                    example: -1
                    format: int64
  /fapi/v1/apiTradingStatus:
    get:
      summary: Futures Trading Quantitative Rules Indicators (USER_DATA)
      x-summary-cn: 合约交易量化规则指标 (USER_DATA)
      description: >-
        Futures trading quantitative rules indicators, for more information on this, please refer to the [Futures
        Trading Quantitative Rules](https://www.binance.com/en/support/faq/4f462ebe6ff445d4a170be7d9e897272)
      x-description-cn: 合约交易量化规则指标，更多细节, 请参考[合约交易量化规则](https://www.binance.com/cn/support/faq/4f462ebe6ff445d4a170be7d9e897272)
      tags:
        - account
      operationId: futuresTradingQuantitativeRulesIndicators
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#futures-trading-quantitative-rules-indicators
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/futuresTradingQuantitativeRulesIndicators.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/futures_trading_quantitative_rules_indicators.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/futures_trading_quantitative_rules_indicators.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/FuturesTradingQuantitativeRulesIndicatorsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/FuturesTradingQuantitativeRulesIndicators/FuturesTradingQuantitativeRulesIndicators.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/FuturesTradingQuantitativeRulesIndicatorsExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        - **1** for a single symbol
        - **10** when the symbol parameter is omitted
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
          description: Futures Trading Quantitative Rules Indicators
          x-description-cn: 合约 Trading Quantitative Rules Indicators
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
                              x-description-cn: 用户该品种交易是否被风控禁用
                              description: Is Locked.
                            plannedRecoverTime:
                              type: integer
                              example: 1545741270000
                              format: int64
                              x-description-cn: 预计恢复时间，若当前时间大等于预计恢复时间则为空
                              description: Planned Recover Time.
                            indicator:
                              type: string
                              example: UFR
                              description: Too many violations under multiple symbols trigger account violation
                              x-description-cn: Too many violations 多交易对触发账号层级违规
                            value:
                              type: number
                              example: 0.05
                              format: float
                              description: Current value
                              x-description-cn: Current value
                            triggerValue:
                              type: number
                              example: 0.995
                              format: float
                              description: Trigger value
                              x-description-cn: Trigger value
                      ETHUSDT:
                        type: array
                        items:
                          type: object
                          properties:
                            isLocked:
                              type: boolean
                              example: true
                              x-description-cn: 用户该品种交易是否被风控禁用
                              description: Is Locked.
                            plannedRecoverTime:
                              type: integer
                              example: 1545741270000
                              format: int64
                              x-description-cn: 预计恢复时间，若当前时间大等于预计恢复时间则为空
                              description: Planned Recover Time.
                            indicator:
                              type: string
                              example: UFR
                              description: Too many violations under multiple symbols trigger account violation
                              x-description-cn: Too many violations 多交易对触发账号层级违规
                            value:
                              type: number
                              example: 0.05
                              format: float
                              description: Current value
                              x-description-cn: Current value
                            triggerValue:
                              type: number
                              example: 0.995
                              format: float
                              description: Trigger value
                              x-description-cn: Trigger value
                      ACCOUNT:
                        type: array
                        items:
                          type: object
                          properties:
                            indicator:
                              type: string
                              example: TMV
                              description: Too many violations under multiple symbols trigger account violation
                              x-description-cn: Too many violations 多交易对触发账号层级违规
                            value:
                              type: integer
                              example: 10
                              format: int64
                              description: Current value
                              x-description-cn: Current value
                            triggerValue:
                              type: integer
                              example: 1
                              format: int64
                              description: Trigger value
                              x-description-cn: Trigger value
                            plannedRecoverTime:
                              type: integer
                              example: 1644919865000
                              format: int64
                              x-description-cn: 预计恢复时间，若当前时间大等于预计恢复时间则为空
                              description: Planned Recover Time.
                            isLocked:
                              type: boolean
                              example: true
                              x-description-cn: 用户该品种交易是否被风控禁用
                              description: Is Locked.
                    description: >-
                      indicator: quantitative rules indicators, value: user's indicators value, triggerValue: trigger
                      indicator value threshold of quantitative rules.
                    x-description-cn: indicator:风控指标名, value:用户在该市场的风控指标数值, triggerValue:阈值, 对于没有达到记录阈值的则不返回数据。
                  updateTime:
                    type: integer
                    example: 1644913304748
                    format: int64
                    x-description-cn: 返回值的更新时间
                    description: Update Time.
  /fapi/v1/feeBurn:
    get:
      summary: Get BNB Burn Status (USER_DATA)
      x-summary-cn: 获取BNB抵扣开关状态 (USER_DATA)
      description: Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )
      x-description-cn: 查询用户 ***所有 symbol*** 合约交易BNB抵扣开关状态(手续费抵扣开或关)
      tags:
        - account
      operationId: getBnbBurnStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-bnb-burn-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getBnbBurnStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_bnb_burn_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_bnb_burn_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetBnbBurnStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetBnbBurnStatus/GetBnbBurnStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetBnbBurnStatusExample.php
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
          description: Get BNB Burn Status
          x-description-cn: 获取BNB Burn 状态
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
      summary: Toggle BNB Burn On Futures Trade (TRADE)
      x-summary-cn: 合约交易BNB抵扣开关 (TRADE)
      description: Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on ***EVERY symbol***
      x-description-cn: 改变用户 ***所有 symbol*** 合约交易BNB抵扣开关(手续费抵扣开或关)
      tags:
        - account
      operationId: toggleBnbBurnOnFuturesTrade
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#toggle-bnb-burn-on-futures-trade
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/toggleBnbBurnOnFuturesTrade.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/toggle_bnb_burn_on_futures_trade.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/toggle_bnb_burn_on_futures_trade.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/ToggleBnbBurnOnFuturesTradeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/ToggleBnbBurnOnFuturesTrade/ToggleBnbBurnOnFuturesTrade.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/ToggleBnbBurnOnFuturesTradeExample.php
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
                - feeBurn
                - timestamp
              properties:
                feeBurn:
                  type: string
                  example: "true"
                  description: '"true": Fee Discount On; "false": Fee Discount Off'
                  x-description-cn: '"true": 手续费抵扣开; "false": 手续费抵扣关'
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
          description: Toggle BNB Burn On Futures Trade
          x-description-cn: Toggle BNB Burn On 合约 交易
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                  msg:
                    type: string
                    example: success
  /fapi/v1/multiAssetsMargin:
    get:
      summary: Get Current Multi-Assets Mode (USER_DATA)
      x-summary-cn: 查询联合保证金模式 (USER_DATA)
      description: Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on ***Every symbol***
      x-description-cn: 查询用户目前在 ***所有symbol*** 合约上的联合保证金模式。
      tags:
        - account
      operationId: getCurrentMultiAssetsMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-current-multi-assets-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getCurrentMultiAssetsMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_current_multi_assets_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_current_multi_assets_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetCurrentMultiAssetsModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetCurrentMultiAssetsMode/GetCurrentMultiAssetsMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetCurrentMultiAssetsModeExample.php
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
          description: Get Current Multi-Assets Mode
          x-description-cn: 获取当前 Multi-Assets Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  multiAssetsMargin:
                    type: boolean
                    example: true
                    description: '"true": Multi-Assets Mode; "false": Single-Asset Mode'
                    x-description-cn: '"true": 联合保证金模式开启；"false": 联合保证金模式关闭'
    post:
      summary: Change Multi-Assets Mode (TRADE)
      x-summary-cn: 更改联合保证金模式 (TRADE)
      description: Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on ***Every symbol***
      x-description-cn: 变换用户在 ***所有symbol*** 合约上的联合保证金模式：开启或关闭联合保证金模式。
      tags:
        - trade
      operationId: changeMultiAssetsMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#change-multi-assets-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/changeMultiAssetsMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/change_multi_assets_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/change_multi_assets_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ChangeMultiAssetsModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ChangeMultiAssetsMode/ChangeMultiAssetsMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ChangeMultiAssetsModeExample.php
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
                - multiAssetsMargin
                - timestamp
              properties:
                multiAssetsMargin:
                  type: string
                  example: "true"
                  description: '"true": Multi-Assets Mode; "false": Single-Asset Mode'
                  x-description-cn: '"true": 联合保证金模式开启；"false": 联合保证金模式关闭'
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
          description: Change Multi-Assets Mode
          x-description-cn: 修改Multi-Assets Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                  msg:
                    type: string
                    example: success
  /fapi/v1/positionSide/dual:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-current-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getCurrentPositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_current_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_current_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetCurrentPositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetCurrentPositionMode/GetCurrentPositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetCurrentPositionModeExample.php
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
                    description: '"true": Hedge Mode; "false": One-way Mode'
                    x-description-cn: '"true": 双向持仓模式；"false": 单向持仓模式'
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#change-position-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/changePositionMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/change_position_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/change_position_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ChangePositionModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ChangePositionMode/ChangePositionMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ChangePositionModeExample.php
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
                  maximum: 60000
                  format: int64
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
                  msg:
                    type: string
                    example: success
  /fapi/v1/order/asyn:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-download-id-for-futures-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getDownloadIdForFuturesOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_download_id_for_futures_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_download_id_for_futures_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetDownloadIdForFuturesOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetDownloadIdForFuturesOrderHistory/GetDownloadIdForFuturesOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetDownloadIdForFuturesOrderHistoryExample.php
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
        - Request Limitation is 10 times per month, shared by front end download page and rest api
        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 存在每月10次的请求限制，网页端和Rest接口下载次数共用。
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
                    x-description-cn: 下载Id
                    description: Download Id.
  /fapi/v1/trade/asyn:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-download-id-for-futures-trade-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getDownloadIdForFuturesTradeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_download_id_for_futures_trade_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_download_id_for_futures_trade_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetDownloadIdForFuturesTradeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetDownloadIdForFuturesTradeHistory/GetDownloadIdForFuturesTradeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetDownloadIdForFuturesTradeHistoryExample.php
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
        - Request Limitation is 5 times per month, shared by front end download page and rest api
        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 存在每月5次的请求限制，网页端和Rest接口下载次数共用。
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
                    x-description-cn: 下载Id
                    description: Download Id.
  /fapi/v1/income/asyn:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-download-id-for-futures-transaction-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getDownloadIdForFuturesTransactionHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_download_id_for_futures_transaction_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_download_id_for_futures_transaction_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetDownloadIdForFuturesTransactionHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetDownloadIdForFuturesTransactionHistory/GetDownloadIdForFuturesTransactionHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetDownloadIdForFuturesTransactionHistoryExample.php
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
      x-parameters-notes: >-
        - The request limit is 100 times per month, shared across the front end download page and rest api, as well as
        between USDⓈ-M and COIN-M contracts.

        - The time between `startTime` and `endTime` can not be longer than 1 year
      x-parameters-notes-cn: |-
        - 存在每月100次的请求限制，该限制在网页端下载页面与Rest接口之间共用，并且在U本位合约与币本位合约之间共用。
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
                    x-description-cn: 下载Id
                    description: Download Id.
  /fapi/v1/order/asyn/id:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-futures-order-history-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getFuturesOrderHistoryDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_futures_order_history_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_futures_order_history_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetFuturesOrderHistoryDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetFuturesOrderHistoryDownloadLinkById/GetFuturesOrderHistoryDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetFuturesOrderHistoryDownloadLinkByIdExample.php
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
                    x-description-cn: 下载Id
                    description: Download Id.
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
  /fapi/v1/trade/asyn/id:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-futures-trade-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getFuturesTradeDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_futures_trade_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_futures_trade_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetFuturesTradeDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetFuturesTradeDownloadLinkById/GetFuturesTradeDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetFuturesTradeDownloadLinkByIdExample.php
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
                    x-description-cn: 下载Id
                    description: Download Id.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 状态，枚举类型：completed 已完成，processing 处理中
                  url:
                    type: string
                    example: www.binance.com
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  notified:
                    type: boolean
                    example: false
                    description: ignore
                    x-description-cn: 忽略
                  expirationTimestamp:
                    type: integer
                    example: 1645009771000
                    format: int64
                    description: The link would expire after this timestamp
                    x-description-cn: 晚于该时间戳之后链接将自动失效
                  isExpired:
                    type: string
                    example: "null"
  /fapi/v1/income/asyn/id:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-futures-transaction-history-download-link-by-id
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getFuturesTransactionHistoryDownloadLinkById.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_futures_transaction_history_download_link_by_id.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_futures_transaction_history_download_link_by_id.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetFuturesTransactionHistoryDownloadLinkByIdExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetFuturesTransactionHistoryDownloadLinkById/GetFuturesTransactionHistoryDownloadLinkById.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetFuturesTransactionHistoryDownloadLinkByIdExample.php
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
                    x-description-cn: 下载Id
                    description: Download Id.
                  status:
                    type: string
                    example: processing
                    description: Enum：completed，processing
                    x-description-cn: 状态，枚举类型：completed 已完成，processing 处理中
                  url:
                    type: string
                    example: www.binance.com
                    description: The link is mapped to download id
                    x-description-cn: 适配该笔ID请求的下载链接
                  notified:
                    type: boolean
                    example: false
                    description: ignore
                    x-description-cn: 忽略
                  expirationTimestamp:
                    type: integer
                    example: 1645009771000
                    format: int64
                    description: The link would expire after this timestamp
                    x-description-cn: 晚于该时间戳之后链接将自动失效
                  isExpired:
                    type: string
                    example: "null"
  /fapi/v1/income:
    get:
      summary: Get Income History (USER_DATA)
      x-summary-cn: 获取账户损益资金流水 (USER_DATA)
      description: Query income history
      x-description-cn: 获取账户损益资金流水
      tags:
        - account
      operationId: getIncomeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#get-income-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/getIncomeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/get_income_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/get_income_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/GetIncomeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/GetIncomeHistory/GetIncomeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/GetIncomeHistoryExample.php
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
            example: BTCUSDT
          description: Trading symbol.
          x-description-cn: 交易对。
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
              - AUTO_EXCHANGE
              - DELIVERED_SETTELMENT
              - COIN_SWAP_DEPOSIT
              - COIN_SWAP_WITHDRAW
              - POSITION_LIMIT_INCREASE_FEE
              - STRATEGY_UMFUTURES_TRANSFER
              - FEE_RETURN
              - BFUSD_REWARD
              - SPECIAL_FUNDING_FEE
          description: Income type.
          x-description-cn: 收益类型。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Timestamp in milliseconds (inclusive start).
          x-description-cn: 起始时间戳（毫秒，包含）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: Timestamp in milliseconds (inclusive end).
          x-description-cn: 结束时间戳（毫秒，包含）。
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
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `incomeType ` is not sent, all kinds of flow will be returned
        - If `startTime` and `endTime` are not sent, the recent 7-day data will be returned.
        - `trandId` is unique in the same `incomeType` for a user.
        - Income history only contains data for the last three months.
      x-parameters-notes-cn: |-
        - 如果不发送 `incomeType`，将返回所有类型的资金流。
        - 如果不发送 `startTime` 和 `endTime`，将返回最近 7 天的数据。
        - `trandId` 在同一 `incomeType` 下对用户唯一。
        - 收入历史仅包含最近三个月的数据。
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
                      description: trade symbol, if existing
                      x-description-cn: 交易对，仅针对涉及交易对的资金流
                    incomeType:
                      type: string
                      example: TRANSFER
                      description: income type
                      x-description-cn: 资金流类型
                    income:
                      type: string
                      example: "-0.37500000"
                      description: income amount
                      x-description-cn: 资金流数量，正数代表流入，负数代表流出
                    asset:
                      type: string
                      example: USDT
                      description: income asset
                      x-description-cn: 资产内容
                    info:
                      type: string
                      example: TRANSFER
                      description: extra information
                      x-description-cn: 备注信息，取决于流水类型
                    time:
                      type: integer
                      example: 1570608000000
                      format: int64
                      x-description-cn: 时间
                      description: Time.
                    tranId:
                      type: integer
                      example: 9689322392
                      format: int64
                      description: transaction id
                      x-description-cn: 划转ID
                    tradeId:
                      type: string
                      example: ""
                      description: trade id, if existing
                      x-description-cn: 引起流水产生的原始交易ID
  /fapi/v1/leverageBracket:
    get:
      summary: Notional and Leverage Brackets (USER_DATA)
      x-summary-cn: 杠杆分层标准 (USER_DATA)
      description: Query user notional and leverage bracket on speicfic symbol
      x-description-cn: 查询账户特定交易对的杠杆分层标准
      tags:
        - account
      operationId: notionalAndLeverageBrackets
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#notional-and-leverage-brackets
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/notionalAndLeverageBrackets.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/notional_and_leverage_brackets.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/notional_and_leverage_brackets.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/NotionalAndLeverageBracketsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/NotionalAndLeverageBrackets/NotionalAndLeverageBrackets.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/NotionalAndLeverageBracketsExample.php
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
          description: Notional and Leverage Brackets
          x-description-cn: Notional 和 Leverage Brackets
          content:
            application/json:
              schema:
                oneOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: ETHUSDT
                        notionalCoef:
                          type: number
                          example: 1.5
                          format: float
                          description: user symbol bracket multiplier, only appears when user's symbol bracket is adjusted
                          x-description-cn: 用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示
                        brackets:
                          type: array
                          example: []
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
                                x-description-cn: 该层对应的名义价值上限
                              notionalFloor:
                                type: integer
                                example: 0
                                format: int64
                                description: Notional threshold of this bracket
                                x-description-cn: 该层对应的名义价值下限
                              maintMarginRatio:
                                type: number
                                example: 0.0065
                                format: float
                                description: Maintenance ratio for this bracket
                                x-description-cn: 该层对应的维持保证金率
                              cum:
                                type: number
                                example: 0
                                format: float
                                description: Auxiliary number for quick calculation
                                x-description-cn: 速算数
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: ETHUSDT
                      notionalCoef:
                        type: number
                        example: 1.5
                        format: float
                        description: user symbol bracket multiplier, only appears when user's symbol bracket is adjusted
                        x-description-cn: 用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示
                      brackets:
                        type: array
                        example: []
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
                              x-description-cn: 该层对应的名义价值上限
                            notionalFloor:
                              type: integer
                              example: 0
                              format: int64
                              description: Notional threshold of this bracket
                              x-description-cn: 该层对应的名义价值下限
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
  /fapi/v1/rateLimit/order:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#query-user-rate-limit
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/queryUserRateLimit.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/query_user_rate_limit.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/query_user_rate_limit.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/QueryUserRateLimitExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/QueryUserRateLimit/QueryUserRateLimit.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/QueryUserRateLimitExample.php
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
            maximum: 60000
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
                    interval:
                      type: string
                      example: SECOND
                    intervalNum:
                      type: integer
                      example: 10
                      format: int64
                    limit:
                      type: integer
                      example: 10000
                      format: int64
  /fapi/v1/symbolConfig:
    get:
      summary: Symbol Configuration (USER_DATA)
      x-summary-cn: 交易对配置 (USER_DATA)
      description: Get current account symbol configuration.
      x-description-cn: 查询交易对上的基础配置
      tags:
        - account
      operationId: symbolConfiguration
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#symbol-configuration
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/symbolConfiguration.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/symbol_configuration.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/symbol_configuration.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/SymbolConfigurationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/SymbolConfiguration/SymbolConfiguration.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/SymbolConfigurationExample.php
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
            maximum: 60000
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
      responses:
        "200":
          description: Symbol Configuration
          x-description-cn: 交易对 Configuration
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
                    marginType:
                      type: string
                      example: CROSSED
                    isAutoAddMargin:
                      type: boolean
                      example: false
                    leverage:
                      type: integer
                      example: 21
                      format: int64
                    maxNotionalValue:
                      type: string
                      example: "1000000"
  /fapi/v1/commissionRate:
    get:
      summary: User Commission Rate (USER_DATA)
      x-summary-cn: 用户手续费率 (USER_DATA)
      description: Get User Commission Rate
      x-description-cn: 查询用户手续费率
      tags:
        - account
      operationId: userCommissionRate
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account#user-commission-rate
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/AccountApi/userCommissionRate.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/account_api/user_commission_rate.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Account/user_commission_rate.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/account/UserCommissionRateExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/AccountAPI/UserCommissionRate/UserCommissionRate.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/account/UserCommissionRateExample.php
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
          description: User Commission Rate
          x-description-cn: 用户 手续费 利率
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSDT
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
                  rpiCommissionRate:
                    type: string
                    example: "0.00005"
                    description: 0.005%
                    x-description-cn: 0.005%
  /fapi/v1/convert/acceptQuote:
    post:
      summary: Accept the offered quote (USER_DATA)
      x-summary-cn: 接受报价 (USER_DATA)
      description: Accept the offered quote by quote ID.
      x-description-cn: 通过 quote ID 来接受报价。
      tags:
        - convert
      operationId: acceptTheOfferedQuote
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/convert#accept-the-offered-quote
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/ConvertApi/acceptTheOfferedQuote.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/convert_api/accept_the_offered_quote.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Convert/accept_the_offered_quote.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/convert/AcceptTheOfferedQuoteExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/ConvertAPI/AcceptTheOfferedQuote/AcceptTheOfferedQuote.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/convert/AcceptTheOfferedQuoteExample.php
      x-ip-weight: 200
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
                - quoteId
                - timestamp
              properties:
                quoteId:
                  type: string
                  example: "1"
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
          description: Accept the offered quote
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
                    description: PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL
                    x-description-cn: PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL
  /fapi/v1/convert/exchangeInfo:
    get:
      summary: List All Convert Pairs
      x-summary-cn: 查询可交易币对信息
      description: Query for all convertible token pairs and the tokens’ respective upper/lower limits
      x-description-cn: 查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。
      tags:
        - convert
      operationId: listAllConvertPairs
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/convert#list-all-convert-pairs
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/ConvertApi/listAllConvertPairs.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/convert_api/list_all_convert_pairs.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Convert/list_all_convert_pairs.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/convert/ListAllConvertPairsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/ConvertAPI/ListAllConvertPairs/ListAllConvertPairs.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/convert/ListAllConvertPairsExample.php
      x-ip-weight: 20
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
        - User needs to supply either or both of the input parameter
        - If not defined for both fromAsset and toAsset, only partial token pairs will be returned
        - Asset BNFCR is only available to convert for MICA region users.
      x-parameters-notes-cn: |-
        - 用户应当fromAsset和toAsset参数至少填一个。
        - 如果fromAsset和toAsset只填写了一个参数，将会返回部分币对信息。
        - BNFCR资产仅对MICA地区用户有效
      responses:
        "200":
          description: List All Convert Pairs
          x-description-cn: 列表All Convert Pairs
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
  /fapi/v1/convert/orderStatus:
    get:
      summary: Order status (USER_DATA)
      x-summary-cn: 查询订单状态 (USER_DATA)
      description: Query order status by order ID.
      x-description-cn: 通过 order ID 来查询订单状态。
      tags:
        - convert
      operationId: orderStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/convert#order-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/ConvertApi/orderStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/convert_api/order_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Convert/order_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/convert/OrderStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/ConvertAPI/OrderStatus/OrderStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/convert/OrderStatusExample.php
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
        - name: orderId
          in: query
          required: false
          schema:
            type: string
            example: 933256278426274400
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
          x-description-cn: 订单 状态
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
  /fapi/v1/convert/getQuote:
    post:
      summary: Send Quote Request (USER_DATA)
      x-summary-cn: 发送获取报价请求 (USER_DATA)
      description: Request a quote for the requested token pairs
      x-description-cn: 对所需的币对发送获取报价请求
      tags:
        - convert
      operationId: sendQuoteRequest
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/convert#send-quote-request
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/ConvertApi/sendQuoteRequest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/convert_api/send_quote_request.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Convert/send_quote_request.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/convert/SendQuoteRequestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/ConvertAPI/SendQuoteRequest/SendQuoteRequest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/convert/SendQuoteRequestExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        50(IP)
        360/hour, 500/day
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
        - Either fromAmount or toAmount should be sent
        - `quoteId` will be returned only if you have enough funds to convert
      x-parameters-notes-cn: |-
        - 参数fromAmount或者toAmount只需要提供其中一个。
        - `quoteId`仅在账户余额充足时返回。
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
                  example: "1.0"
                  format: float
                  description: When specified, it is the amount you will be debited after the conversion
                  x-description-cn: 这是成交后将被扣除的金额
                toAmount:
                  type: number
                  example: "1.0"
                  format: float
                  description: When specified, it is the amount you will be credited after the conversion
                  x-description-cn: 这是成交后将会获得的金额
                validTime:
                  type: string
                  example: 10s
                  description: 10s, default 10s
                  x-description-cn: 可以支持10s，默认值为10s
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
          x-description-cn: Send Quote 请求
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
  /fapi/v1/symbolAdlRisk:
    get:
      summary: ADL Risk
      x-summary-cn: 自动减仓风险评级
      description: |-
        Query the symbol-level ADL risk rating.

        The ADL risk rating measures the likelihood of ADL during liquidation,
        and the rating takes into account the insurance fund balance, position
        concentration on the symbol, order book depth, price volatility, average
        leverage, unrealized PnL, and margin utilization at the symbol level.

        The rating can be high, medium and low, and is updated every 30 minutes.
      x-description-cn: |-
        查询symbol级别的 ADL 风险评级。

        ADL 风险评级用于衡量在发生强平时触发 ADL
        的可能性，该评级会综合考虑该symbol的保险基金余额、仓位集中度、盘口深度、价格波动率、平均杠杆水平、未实现盈亏以及保证金利用率。

        风险等级分为高、中、低，每半小时更新一次。
      tags:
        - market-data
      operationId: adlRisk
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#adl-risk
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/adlRisk.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/adl_risk.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/adl_risk.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/AdlRiskExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/AdlRisk/AdlRisk.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/AdlRiskExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Symbol
          x-description-cn: 交易对
      responses:
        "200":
          description: ADL Risk
          x-description-cn: 请参见英文说明：ADL Risk
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      adlRisk:
                        type: string
                        example: low
                        description: ADL Risk rating
                        x-description-cn: 自动减仓风险评级
                      updateTime:
                        type: integer
                        example: 1597370495002
                        format: int64
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        adlRisk:
                          type: string
                          example: low
                          description: ADL Risk rating
                          x-description-cn: 自动减仓风险评级
                        updateTime:
                          type: integer
                          example: 1597370495002
                          format: int64
  /futures/data/basis:
    get:
      summary: Basis
      x-summary-cn: 基差
      description: Query future basis
      x-description-cn: 查询期货基差
      tags:
        - market-data
      operationId: basis
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#basis
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/basis.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/basis.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/basis.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/BasisExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/Basis/Basis.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/BasisExample.php
      x-ip-weight: 0
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
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
                      example: "34400.15945055"
                    contractType:
                      type: string
                      example: PERPETUAL
                    basisRate:
                      type: string
                      example: "0.0004"
                    futuresPrice:
                      type: string
                      example: "34414.10"
                    annualizedBasisRate:
                      type: string
                      example: ""
                    basis:
                      type: string
                      example: "13.94054945"
                    pair:
                      type: string
                      example: BTCUSDT
                    timestamp:
                      type: integer
                      example: 1698742800000
                      format: int64
                      description: Start time of the period, in milliseconds.
                      x-description-cn: 该周期的开始时间，单位为毫秒。
  /fapi/v1/time:
    get:
      summary: Check Server Time
      x-summary-cn: 获取服务器时间
      description: Test connectivity to the Rest API and get the current server time.
      x-description-cn: 获取服务器时间
      tags:
        - market-data
      operationId: checkServerTime
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#check-server-time
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/checkServerTime.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/check_server_time.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/check_server_time.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/CheckServerTimeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/CheckServerTime/CheckServerTime.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/CheckServerTimeExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: Check Server Time
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
                    x-description-cn: 当前的系统时间
                    description: Server Time.
  /fapi/v1/indexInfo:
    get:
      summary: Composite Index Symbol Information
      x-summary-cn: 综合指数交易对信息
      description: Query composite index symbol information
      x-description-cn: 获取交易对为综合指数的基础成分信息。
      tags:
        - market-data
      operationId: compositeIndexSymbolInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#composite-index-symbol-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/compositeIndexSymbolInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/composite_index_symbol_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/composite_index_symbol_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/CompositeIndexSymbolInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/CompositeIndexSymbolInformation/CompositeIndexSymbolInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/CompositeIndexSymbolInformationExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: DEFIUSDT
      x-parameters-notes: "- Only for composite index symbols"
      x-parameters-notes-cn: "- 仅 用于 composite index symbols"
      responses:
        "200":
          description: Composite Index Symbol Information
          x-description-cn: Composite Index 交易对 信息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: DEFIUSDT
                    time:
                      type: integer
                      example: 1589437530011
                      format: int64
                      description: Current time
                      x-description-cn: 请求时间
                    component:
                      type: string
                      example: baseAsset
                      description: Component asset
                      x-description-cn: 成分资产
                    baseAssetList:
                      type: array
                      example: []
                      items:
                        type: object
                        properties:
                          baseAsset:
                            type: string
                            example: BAL
                            x-description-cn: 基础资产
                            description: Base Asset.
                          quoteAsset:
                            type: string
                            example: USDT
                            x-description-cn: 报价资产
                            description: Quote Asset.
                          weightInQuantity:
                            type: string
                            example: "1.04406228"
                            x-description-cn: 权重(数量)
                            description: Weight In Quantity.
                          weightInPercentage:
                            type: string
                            example: "0.02783900"
                            x-description-cn: 权重(比例)
                            description: Weight In Percentage.
  /fapi/v1/aggTrades:
    get:
      summary: Compressed/Aggregate Trades List
      x-summary-cn: 近期成交
      description: |-
        Get compressed, aggregate market trades. Market trades that fill in
        100ms with the same price and the same taking side will have the
        quantity aggregated.

        Retail Price Improvement(RPI) orders are aggregated and without special
        tags to be distinguished.
      x-description-cn: |-
        获取归集/压缩的市场成交记录。100ms内价格和买卖方向相同的成交会被归集成一条记录。

        零点价差改善订单（RPI订单）会被归集，并且没有特殊标签区分。
      tags:
        - market-data
      operationId: compressedAggregateTradesList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#compressed-aggregate-trades-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/compressedAggregateTradesList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/compressed_aggregate_trades_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/compressed_aggregate_trades_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/CompressedAggregateTradesListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/CompressedAggregateTradesList/CompressedAggregateTradesList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/CompressedAggregateTradesListExample.php
      x-ip-weight: 20
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
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
          x-description-cn: 从包含fromID的成交开始返回结果
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
            example: 50
            format: int64
            default: 500
            maximum: 1000
      x-parameters-notes: >-
        - only trade histories within the past 48 hours (counted from now) can be queried

        - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 1 hour.

        - If `fromId`, `startTime`, and `endTime` are not sent, the most recent aggregate trades will be returned.

        - Only market trades will be aggregated and returned, which means the insurance fund trades and ADL trades won't
        be aggregated.

        - Sending both `startTime`/`endTime` and `fromId` might cause response timeout, please send either `fromId` or
        `startTime`/`endTime`
      x-parameters-notes-cn: |-
        - 接口仅支持查询最近48小时（以当前时间为准）内的交易数据
        - 如果同时发送`startTime`和`endTime`，间隔必须小于一小时
        - 如果没有发送任何筛选参数(`fromId`, `startTime`, `endTime`)，默认返回最近的成交记录
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
                      example: 26129
                      format: int64
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
                    nq:
                      type: string
                      example: "100"
                      description: Normal quantity without the trades involving RPI orders
                      x-description-cn: 普通订单成交量，不包含RPI订单数据
                    f:
                      type: integer
                      example: 27781
                      format: int64
                      description: First tradeId
                      x-description-cn: 被归集的首个成交ID
                    l:
                      type: integer
                      example: 27781
                      format: int64
                      description: Last tradeId
                      x-description-cn: 被归集的末个成交ID
                    T:
                      type: integer
                      example: 1498793709153
                      format: int64
                      description: Timestamp
                      x-description-cn: 成交时间
                    m:
                      type: boolean
                      example: true
                      description: Was the buyer the maker?
                      x-description-cn: 是否为主动卖出单
  /fapi/v1/continuousKlines:
    get:
      summary: Continuous Contract Kline/Candlestick Data
      x-summary-cn: 连续合约K线数据
      description: |-
        Kline/candlestick bars for a specific contract type.
        Klines are uniquely identified by their open time.
      x-description-cn: 获取特定合约类型的K线数据。K线由开盘时间唯一标识。
      tags:
        - market-data
      operationId: continuousContractKlineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#continuous-contract-kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/continuousContractKlineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/continuous_contract_kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/continuous_contract_kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/ContinuousContractKlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/ContinuousContractKlineCandlestickData/ContinuousContractKlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/ContinuousContractKlineCandlestickDataExample.php
      x-weight: |-
        based on parameter `LIMIT`

        | LIMIT       | weight |
        | ----------- | ------ |
        | [1,100)     | 1      |
        | [100, 500)  | 2      |
        | [500, 1000] | 5      |
        | > 1000      | 10     |
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: After CM migration, accepts both UM and CM pair values.
          x-description-cn: 标的交易对 迁移后支持传入 UM 与 CM 的 pair。
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
              - TRADIFI_PERPETUAL
          description: Futurestype
          x-description-cn: 合约类型
        - name: interval
          in: query
          required: true
          schema:
            type: string
            example: 1m
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
            example: 50
            format: int64
            default: 500
            maximum: 1500
      x-parameters-notes: "- If startTime and endTime are not sent, the most recent klines are returned."
      x-parameters-notes-cn: "- 如果不发送startTime和endTime，则返回最近的K线数据。"
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
                      example: 1607444700000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "18879.99"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "18900.00"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "18878.98"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "18896.13"
                    - type: string
                      description: Volume
                      x-description-cn: 成交量
                      example: "492.363"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1607444759999
                    - type: string
                      description: Quote asset volume
                      x-description-cn: 成交额
                      example: "9302145.66080"
                    - type: integer
                      description: Number of trades
                      x-description-cn: 成交笔数
                      example: 1874
                    - type: string
                      description: Taker buy base asset volume
                      x-description-cn: 主动买入成交量
                      example: "385.983"
                    - type: string
                      description: Taker buy quote asset volume
                      x-description-cn: 主动买入成交额
                      example: "7292402.33267"
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
                        example: 1607444700000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "18879.99"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "18900.00"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "18878.98"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "18896.13"
                      - type: string
                        description: Volume
                        x-description-cn: 成交量
                        example: "492.363"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1607444759999
                      - type: string
                        description: Quote asset volume
                        x-description-cn: 成交额
                        example: "9302145.66080"
                      - type: integer
                        description: Number of trades
                        x-description-cn: 成交笔数
                        example: 1874
                      - type: string
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入成交量
                        example: "385.983"
                      - type: string
                        description: Taker buy quote asset volume
                        x-description-cn: 主动买入成交额
                        example: "7292402.33267"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /fapi/v1/exchangeInfo:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#exchange-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/exchangeInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/exchange_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/exchange_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/ExchangeInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/ExchangeInformation/ExchangeInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/ExchangeInformationExample.php
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
                      example: ""
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        interval:
                          type: string
                          example: MINUTE
                          x-description-cn: 按照分钟计算
                          description: Interval.
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          x-description-cn: 按照1分钟计算
                          description: Interval Num.
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          x-description-cn: 上限次数
                          description: Limit.
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          x-description-cn: 按照访问权重来计算
                          description: Rate Limit Type.
                      x-description-cn: API访问的限制
                      description: API
                    x-description-cn: API访问的限制
                    description: Rate Limits.
                  serverTime:
                    type: integer
                    example: 1565613908500
                    format: int64
                    description: Ignore please. If you want to check current server time, please check via "GET /fapi/v1/time"
                    x-description-cn: 请忽略。如果需要获取当前系统时间，请查询接口 “GET /fapi/v1/time”
                  assets:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: BTC
                        marginAvailable:
                          type: boolean
                          example: true
                          description: whether the asset can be used as margin in Multi-Assets mode
                          x-description-cn: 是否可用作保证金
                        autoAssetExchange:
                          type: string
                          example: "-0.10"
                          description: auto-exchange threshold in Multi-Assets margin mode
                          x-description-cn: 保证金资产自动兑换阈值
                      description: assets information
                      x-description-cn: 资产信息
                    description: assets information
                    x-description-cn: 资产信息
                  symbols:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BLZUSDT
                          x-description-cn: 交易对
                          description: Symbol.
                        pair:
                          type: string
                          example: BLZUSDT
                          x-description-cn: 标的交易对
                          description: Pair.
                        contractType:
                          type: string
                          example: PERPETUAL
                          x-description-cn: 合约类型
                          description: Contract Type.
                        deliveryDate:
                          type: integer
                          example: 4133404800000
                          format: int64
                          x-description-cn: 交割日期
                          description: Delivery Date.
                        onboardDate:
                          type: integer
                          example: 1598252400000
                          format: int64
                          x-description-cn: 上线日期
                          description: Onboard Date.
                        status:
                          type: string
                          example: TRADING
                          x-description-cn: 交易对状态
                          description: Status.
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
                        baseAsset:
                          type: string
                          example: BLZ
                          x-description-cn: 标的资产
                          description: Base Asset.
                        quoteAsset:
                          type: string
                          example: USDT
                          x-description-cn: 报价资产
                          description: Quote Asset.
                        marginAsset:
                          type: string
                          example: USDT
                          x-description-cn: 保证金资产
                          description: Margin Asset.
                        pricePrecision:
                          type: integer
                          example: 5
                          format: int64
                          description: please do not use it as tickSize
                          x-description-cn: 价格小数点位数(仅作为系统精度使用，注意同tickSize 区分）
                        quantityPrecision:
                          type: integer
                          example: 0
                          format: int64
                          description: please do not use it as stepSize
                          x-description-cn: 数量小数点位数(仅作为系统精度使用，注意同stepSize 区分）
                        baseAssetPrecision:
                          type: integer
                          example: 8
                          format: int64
                          x-description-cn: 标的资产精度
                          description: Base Asset Precision.
                        quotePrecision:
                          type: integer
                          example: 8
                          format: int64
                          x-description-cn: 报价资产精度
                          description: Quote Precision.
                        underlyingType:
                          type: string
                          example: COIN
                        underlyingSubType:
                          type: array
                          items:
                            type: string
                            example: STORAGE
                        settlePlan:
                          type: integer
                          example: 0
                          format: int64
                        triggerProtect:
                          type: string
                          example: "0.15"
                          description: threshold for algo order with "priceProtect"
                          x-description-cn: 开启"priceProtect"的条件订单的触发阈值
                        filters:
                          type: array
                          items:
                            type: object
                            properties:
                              filterType:
                                type: string
                                example: PRICE_FILTER
                                x-description-cn: 市价订单数量限制
                                description: Filter Type.
                              maxPrice:
                                type: string
                                example: "300"
                                x-description-cn: 价格上限, 最大价格
                                description: Max Price.
                              minPrice:
                                type: string
                                example: "0.0001"
                                x-description-cn: 价格下限, 最小价格
                                description: Min Price.
                              tickSize:
                                type: string
                                example: "0.0001"
                                x-description-cn: 订单最小价格间隔
                                description: Tick Size.
                              maxQty:
                                type: string
                                example: "10000000"
                                x-description-cn: 数量上限, 最大数量
                                description: Max Qty.
                              minQty:
                                type: string
                                example: "1"
                                x-description-cn: 数量下限, 最小数量
                                description: Min Qty.
                              stepSize:
                                type: string
                                example: "1"
                                x-description-cn: 订单最小数量间隔
                                description: Step Size.
                              limit:
                                type: integer
                                example: 200
                                format: int64
                                x-description-cn: 上限次数
                                description: Limit.
                              notional:
                                type: string
                                example: "5.0"
                              multiplierUp:
                                type: string
                                example: "1.1500"
                                x-description-cn: 价格上限百分比
                                description: Multiplier Up.
                              multiplierDown:
                                type: string
                                example: "0.8500"
                                x-description-cn: 价格下限百分比
                                description: Multiplier Down.
                              multiplierDecimal:
                                type: string
                                example: "4"
                        orderTypes:
                          type: array
                          items:
                            type: string
                            example: LIMIT
                        timeInForce:
                          type: array
                          items:
                            type: string
                            example: GTC
                            x-description-cn: 有效方式
                            description: timeInForce.
                          x-description-cn: 有效方式
                          description: Time In Force.
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
                      x-description-cn: 交易对信息
                      description: symbols.
                    x-description-cn: 交易对信息
                    description: Symbols.
                  timezone:
                    type: string
                    example: UTC
                    x-description-cn: 服务器所用的时间区域
                    description: Timezone.
  /fapi/v1/fundingRate:
    get:
      summary: Get Funding Rate History
      x-summary-cn: 查询资金费率历史
      description: Get Funding Rate History
      x-description-cn: 查询资金费率历史
      tags:
        - market-data
      operationId: getFundingRateHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#get-funding-rate-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/getFundingRateHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/get_funding_rate_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/get_funding_rate_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/GetFundingRateHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/GetFundingRateHistory/GetFundingRateHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/GetFundingRateHistoryExample.php
      x-weight: share 500/5min/IP rate limit with GET /fapi/v1/fundingInfo
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
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
            example: 50
            format: int64
            default: 100
            maximum: 1000
      x-parameters-notes: >-
        - If `startTime` and `endTime` are not sent, the most recent 200 records are returned.

        - If the number of data between `startTime` and `endTime` is larger than `limit`, return as `startTime` +
        `limit`.

        - In ascending order.
      x-parameters-notes-cn: |-
        - 如果 `startTime` 和 `endTime` 没有发送，则返回最近的 200 条记录。
        - 如果 `startTime` 和 `endTime` 之间的数据量大于 `limit`，则返回 `startTime` + `limit`。
        - 升序。
      responses:
        "200":
          description: Get Funding Rate History
          x-description-cn: 获取Funding 利率 历史
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
                      x-description-cn: 交易对
                      description: Symbol.
                    fundingRate:
                      type: string
                      example: "-0.03750000"
                      x-description-cn: 资金费率
                      description: Funding Rate.
                    fundingTime:
                      type: integer
                      example: 1570608000000
                      format: int64
                      x-description-cn: 资金费时间
                      description: Funding Time.
                    markPrice:
                      type: string
                      example: "34287.54619963"
                      description: mark price associated with a particular funding fee charge
                      x-description-cn: 资金费对应标记价格
                    rateType:
                      type: string
                      enum:
                        - Regular
                        - Special
                      example: Regular
                      description: >-
                        Funding rate type. `Regular` for the normal funding rate; `Special` for the additional funding
                        rate generated by stock dividends.
                      x-description-cn: 资金费率类型。`Regular` 为正常资金费率；`Special` 为股票分红产生的额外资金费率。
  /fapi/v1/fundingInfo:
    get:
      summary: Get Funding Rate Info
      x-summary-cn: 查询资金费率信息
      description: Query funding rate info for symbols that had FundingRateCap/FundingRateFloor / fundingIntervalHours adjustment
      x-description-cn: 查询资金费率信息，接口仅返回FundingRateCap/FundingRateFloor/fundingIntervalHours等被特殊调整过的交易对，没调整过的不返回。
      tags:
        - market-data
      operationId: getFundingRateInfo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#get-funding-rate-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/getFundingRateInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/get_funding_rate_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/get_funding_rate_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/GetFundingRateInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/GetFundingRateInfo/GetFundingRateInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/GetFundingRateInfoExample.php
      x-weight: |-
        **0**

        share 500/5min/IP rate limit with `GET /fapi/v1/fundingRate`
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
                      example: BLZUSDT
                    adjustedFundingRateCap:
                      type: string
                      example: "0.02500000"
                    adjustedFundingRateFloor:
                      type: string
                      example: "-0.02500000"
                    fundingIntervalHours:
                      type: integer
                      example: 8
                      format: int64
                    disclaimer:
                      type: boolean
                      example: false
                      description: ingore
                      x-description-cn: ingore
  /fapi/v1/indexPriceKlines:
    get:
      summary: Index Price Kline/Candlestick Data
      x-summary-cn: 价格指数K线数据
      description: |-
        Kline/candlestick bars for the index price of a pair.
        Klines are uniquely identified by their open time.
      x-description-cn: 价格指数K线数据，每根K线的开盘时间可视为唯一ID
      tags:
        - market-data
      operationId: indexPriceKlineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#index-price-kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/indexPriceKlineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/index_price_kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/index_price_kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/IndexPriceKlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/IndexPriceKlineCandlestickData/IndexPriceKlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/IndexPriceKlineCandlestickDataExample.php
      x-weight: |-
        based on parameter `LIMIT`

        | LIMIT       | weight |
        | ----------- | ------ |
        | [1,100)     | 1      |
        | [100, 500)  | 2      |
        | [500, 1000] | 5      |
        | > 1000      | 10     |
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: After CM migration, accepts both UM and CM pair values.
          x-description-cn: 标的交易对 迁移后支持传入 UM 与 CM 的 pair。
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
            example: 50
            format: int64
            default: 500
            maximum: 1500
      x-parameters-notes: "- If startTime and endTime are not sent, the most recent klines are returned."
      x-parameters-notes-cn: "- 缺省返回最近的数据"
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
                      description: Ignore
                      x-description-cn: 忽略字段
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
                        description: Ignore
                        x-description-cn: 忽略字段
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
  /fapi/v1/klines:
    get:
      summary: Kline/Candlestick Data
      x-summary-cn: K线数据
      description: |-
        Kline/candlestick bars for a symbol.
        Klines are uniquely identified by their open time.
      x-description-cn: 每根K线的开盘时间可视为唯一ID
      tags:
        - market-data
      operationId: klineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/klineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/KlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/KlineCandlestickData/KlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/KlineCandlestickDataExample.php
      x-weight: |-
        based on parameter `LIMIT`

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
            example: BTCUSDT
          description: After CM migration, accepts both UM and CM symbols.
          x-description-cn: 交易对 迁移后支持传入 UM 与 CM 的 symbol。
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
            example: 50
            format: int64
            default: 500
            maximum: 1500
      x-parameters-notes: "- If startTime and endTime are not sent, the most recent klines are returned."
      x-parameters-notes-cn: "- 缺省返回最近的数据"
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
                      example: "17928899.62484339"
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
                        example: "17928899.62484339"
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#long-short-ratio
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/longShortRatio.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/long_short_ratio.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/long_short_ratio.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/LongShortRatioExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/LongShortRatio/LongShortRatio.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/LongShortRatioExample.php
      x-ip-weight: 0
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
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
            example: 50
            format: int64
            default: 30
            maximum: 500
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
        - IP rate limit 1000 requests/5min
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
        - IP限频为1000次/5min
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
                    symbol:
                      type: string
                      example: BTCUSDT
                      description: long/short account num ratio of all traders
                      x-description-cn: long/short account num ratio of all traders
                    longShortRatio:
                      type: string
                      example: "0.1960"
                      description: long account num ratio of all traders
                      x-description-cn: 多空人数比值
                    longAccount:
                      type: string
                      example: "0.6622"
                      description: short account num ratio of all traders
                      x-description-cn: 多仓人数比例
                    shortAccount:
                      type: string
                      example: "0.3378"
                      x-description-cn: 空仓人数比例
                      description: Short Account.
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /fapi/v1/premiumIndex:
    get:
      summary: Mark Price
      x-summary-cn: 最新标记价格和资金费率
      description: Mark Price and Funding Rate
      x-description-cn: 采集各大交易所数据加权平均
      tags:
        - market-data
      operationId: markPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#mark-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/markPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/mark_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/mark_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/MarkPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/MarkPrice/MarkPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/MarkPriceExample.php
      x-weight: "**1** with symbol, **10**\_without symbol"
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
      responses:
        "200":
          description: Mark Price
          x-description-cn: Mark 价格
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                        x-description-cn: 交易对
                        description: Symbol.
                      markPrice:
                        type: string
                        example: "11793.63104562"
                        description: mark price
                        x-description-cn: 标记价格
                      indexPrice:
                        type: string
                        example: "11781.80495970"
                        description: index price
                        x-description-cn: 指数价格
                      estimatedSettlePrice:
                        type: string
                        example: "11781.16138815"
                        description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                        x-description-cn: 预估结算价,仅在交割开始前最后一小时有意义
                      lastFundingRate:
                        type: string
                        example: "0.00038246"
                        description: This is the Latest funding rate
                        x-description-cn: 最近更新的资金费率
                      interestRate:
                        type: string
                        example: "0.00010000"
                        x-description-cn: 标的资产基础利率
                        description: Interest Rate.
                      nextFundingTime:
                        type: integer
                        example: 1597392000000
                        format: int64
                        x-description-cn: 下次资金费时间
                        description: Next Funding Time.
                      time:
                        type: integer
                        example: 1597370495002
                        format: int64
                        x-description-cn: 更新时间
                        description: Time.
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          x-description-cn: 交易对
                          description: Symbol.
                        markPrice:
                          type: string
                          example: "11793.63104562"
                          description: mark price
                          x-description-cn: 标记价格
                        indexPrice:
                          type: string
                          example: "11781.80495970"
                          description: index price
                          x-description-cn: 指数价格
                        estimatedSettlePrice:
                          type: string
                          example: "11781.16138815"
                          description: Estimated Settle Price, only useful in the last hour before the settlement starts.
                          x-description-cn: 预估结算价,仅在交割开始前最后一小时有意义
                        lastFundingRate:
                          type: string
                          example: "0.00038246"
                          description: This is the Latest funding rate
                          x-description-cn: 最近更新的资金费率
                        interestRate:
                          type: string
                          example: "0.00010000"
                          x-description-cn: 标的资产基础利率
                          description: Interest Rate.
                        nextFundingTime:
                          type: integer
                          example: 1597392000000
                          format: int64
                          x-description-cn: 下次资金费时间
                          description: Next Funding Time.
                        time:
                          type: integer
                          example: 1597370495002
                          format: int64
                          x-description-cn: 更新时间
                          description: Time.
  /fapi/v1/markPriceKlines:
    get:
      summary: Mark Price Kline/Candlestick Data
      x-summary-cn: 标记价格K线数据
      description: |-
        Kline/candlestick bars for the mark price of a symbol.
        Klines are uniquely identified by their open time.
      x-description-cn: 每根K线的开盘时间可视为唯一ID
      tags:
        - market-data
      operationId: markPriceKlineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#mark-price-kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/markPriceKlineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/mark_price_kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/mark_price_kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/MarkPriceKlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/MarkPriceKlineCandlestickData/MarkPriceKlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/MarkPriceKlineCandlestickDataExample.php
      x-weight: |-
        based on parameter `LIMIT`

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
            example: BTCUSDT
          description: After CM migration, accepts both UM and CM symbols.
          x-description-cn: 交易对 迁移后支持传入 UM 与 CM 的 symbol。
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
            example: 50
            format: int64
            default: 500
            maximum: 1500
      x-parameters-notes: "- If startTime and endTime are not sent, the most recent klines are returned."
      x-parameters-notes-cn: "- 缺省返回最近的数据"
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
                      example: 1591256460000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "9653.29201333"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "9654.56401333"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "9653.07367333"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "9653.07367333"
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1591256519999
                    - type: string
                      description: Ignore
                      x-description-cn: 忽略字段
                      example: "0"
                    - type: integer
                      description: Ignore
                      x-description-cn: 忽略字段
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
                        example: 1591256460000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "9653.29201333"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "9654.56401333"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "9653.07367333"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "9653.07367333"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1591256519999
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
                      - type: integer
                        description: Ignore
                        x-description-cn: 忽略字段
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
  /fapi/v1/assetIndex:
    get:
      summary: Multi-Assets Mode Asset Index
      x-summary-cn: 多资产模式资产汇率指数
      description: >-
        Asset index price.


        > **CM-UM Integration (Effective 2026-06-30):** Renamed from *Multi-Assets Mode Asset Index*. The response now
        additionally pushes COIN-M settlement-asset price index entries (e.g., `BTCUSD`, `ETHUSD`, `BNBUSD`). The
        endpoint path `/fapi/v1/assetIndex` is unchanged.
      x-description-cn: >-
        资产汇率指数。


        > **币本位/U本位整合迁移(2026-06-30 生效):** 接口名由 *多资产模式资产汇率指数* 变更为 *资产汇率指数*。响应中**额外推送**币本位结算资产的价格指数(如
        `BTCUSD`、`ETHUSD`、`BNBUSD`)。HTTP 路径 `/fapi/v1/assetIndex` 保持不变。
      tags:
        - market-data
      operationId: assetIndex
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#asset-index
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/assetIndex.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/asset_index.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/asset_index.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/AssetIndexExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/AssetIndex/AssetIndex.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/AssetIndexExample.php
      x-weight: "**1** for a single symbol; **10** when the symbol parameter is omitted"
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: ADAUSD
          description: Asset pair
          x-description-cn: 资产 pair
      responses:
        "200":
          description: Multi-Assets Mode Asset Index
          x-description-cn: Multi-Assets Mode 资产 Index
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: ADAUSD
                      time:
                        type: integer
                        example: 1635740268004
                        format: int64
                      index:
                        type: string
                        example: "1.92957370"
                      bidBuffer:
                        type: string
                        example: "0.10000000"
                      askBuffer:
                        type: string
                        example: "0.10000000"
                      bidRate:
                        type: string
                        example: "1.73661633"
                      askRate:
                        type: string
                        example: "2.12253107"
                      autoExchangeBidBuffer:
                        type: string
                        example: "0.05000000"
                      autoExchangeAskBuffer:
                        type: string
                        example: "0.05000000"
                      autoExchangeBidRate:
                        type: string
                        example: "1.83309501"
                      autoExchangeAskRate:
                        type: string
                        example: "2.02605238"
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: ADAUSD
                        time:
                          type: integer
                          example: 1635740268004
                          format: int64
                        index:
                          type: string
                          example: "1.92957370"
                        bidBuffer:
                          type: string
                          example: "0.10000000"
                        askBuffer:
                          type: string
                          example: "0.10000000"
                        bidRate:
                          type: string
                          example: "1.73661633"
                        askRate:
                          type: string
                          example: "2.12253107"
                        autoExchangeBidBuffer:
                          type: string
                          example: "0.05000000"
                        autoExchangeAskBuffer:
                          type: string
                          example: "0.05000000"
                        autoExchangeBidRate:
                          type: string
                          example: "1.83309501"
                        autoExchangeAskRate:
                          type: string
                          example: "2.02605238"
  /fapi/v1/historicalTrades:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#old-trades-lookup
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/oldTradesLookup.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/old_trades_lookup.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/old_trades_lookup.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/OldTradesLookupExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/OldTradesLookup/OldTradesLookup.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/OldTradesLookupExample.php
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
            example: BTCUSDT
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 50
            format: int64
            default: 100
            maximum: 500
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: TradeId to fetch from. Default gets most recent trades.
          x-description-cn: 从该 TradeId 开始获取数据，默认获取最近的成交数据
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
                      example: 28457
                      format: int64
                      x-description-cn: 成交ID
                      description: Id.
                    price:
                      type: string
                      example: "4.00000100"
                      x-description-cn: 成交价格
                      description: Price.
                    qty:
                      type: string
                      example: "12.00000000"
                      x-description-cn: 成交量
                      description: Qty.
                    quoteQty:
                      type: string
                      example: "8000.00"
                      x-description-cn: 成交额
                      description: Quote Qty.
                    time:
                      type: integer
                      example: 1499865549590
                      format: int64
                      x-description-cn: 时间
                      description: Time.
                    isBuyerMaker:
                      type: boolean
                      example: true
                      x-description-cn: 买方是否为挂单方
                      description: Is Buyer Maker.
                    isRPITrade:
                      type: boolean
                      example: true
                      x-description-cn: Maker方是否为RPI挂单
                      description: Is RPITrade.
  /fapi/v1/openInterest:
    get:
      summary: Open Interest
      x-summary-cn: 获取未平仓合约数
      description: Get present open interest of a specific symbol.
      x-description-cn: 获取未平仓合约数
      tags:
        - market-data
      operationId: openInterest
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#open-interest
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/openInterest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/open_interest.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/open_interest.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/OpenInterestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/OpenInterest/OpenInterest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/OpenInterestExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
      responses:
        "200":
          description: Open Interest
          x-description-cn: 未完成利息
          content:
            application/json:
              schema:
                type: object
                properties:
                  openInterest:
                    type: string
                    example: "10659.509"
                    x-description-cn: 未平仓合约数量
                    description: Open Interest.
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
                  time:
                    type: integer
                    example: 1589437530011
                    format: int64
                    description: Transaction time
                    x-description-cn: 撮合引擎时间
  /futures/data/openInterestHist:
    get:
      summary: Open Interest Statistics
      x-summary-cn: 合约持仓量历史
      description: Open Interest Statistics
      x-description-cn: 查询合约持仓量历史
      tags:
        - market-data
      operationId: openInterestStatistics
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#open-interest-statistics
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/openInterestStatistics.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/open_interest_statistics.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/open_interest_statistics.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/OpenInterestStatisticsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/OpenInterestStatistics/OpenInterestStatistics.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/OpenInterestStatisticsExample.php
      x-ip-weight: 0
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
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
            example: 50
            format: int64
            default: 30
            maximum: 500
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
      x-parameters-notes: >-
        - If startTime and endTime are not sent, the most recent data is returned.

        - Only the data of the latest 1 month is available.

        - IP rate limit 1000 requests/5min

        - A period with no trades has no record and is omitted from the response. Such gaps are expected and are not
        backfilled.
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近1个月的数据
        - IP限频为1000次/5min
        - 若某周期内没有成交，则该周期无数据记录，响应中不会返回。此类缺失为预期行为，不会回补。
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
                    symbol:
                      type: string
                      example: BTCUSDT
                    sumOpenInterest:
                      type: string
                      example: "20403.12345678"
                      description: total open interest
                      x-description-cn: 持仓总数量
                    sumOpenInterestValue:
                      type: string
                      example: "176196512.12345678"
                      description: total open interest value
                      x-description-cn: 持仓总价值
                    CMCCirculatingSupply:
                      type: string
                      example: "165880.538"
                      description: circulating supply provided by CMC
                      x-description-cn: CMC提供的流通供应量
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /fapi/v1/depth:
    get:
      summary: Order Book
      x-summary-cn: 深度信息
      description: |-
        Query symbol orderbook

        Retail Price Improvement(RPI) orders are not visible and excluded in the
        response message.
      x-description-cn: |-
        查询交易对订单 Book

        零售价格改进（RPI）订单不可见，并且在响应消息中被排除。
      tags:
        - market-data
      operationId: orderBook
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#order-book
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/orderBook.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/order_book.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/order_book.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/OrderBookExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/OrderBook/OrderBook.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/OrderBookExample.php
      x-weight: |-
        Adjusted based on the limit:

        | Limit         | Weight |
        | ------------- | ------ |
        | 5, 10, 20, 50 | 2      |
        | 100           | 5      |
        | 500           | 10     |
        | 1000          | 20     |
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 50
            format: int64
            default: 500
            maximum: 1000
          description: Valid limits:[5, 10, 20, 50, 100, 500, 1000]
          x-description-cn: 可选值:[5, 10, 20, 50, 100, 500, 1000]
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
                    example: 1027024
                    format: int64
                  E:
                    type: integer
                    example: 1589436922972
                    format: int64
                    description: Message output time
                    x-description-cn: 消息时间
                  T:
                    type: integer
                    example: 1589436922959
                    format: int64
                    description: Transaction time
                    x-description-cn: 撮合引擎时间
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
  /fapi/v1/premiumIndexKlines:
    get:
      summary: Premium index Kline Data
      x-summary-cn: 溢价指数K线数据
      description: Premium index kline bars of a symbol. Klines are uniquely identified by their open time.
      x-description-cn: 获取某个交易对的溢价指数K线数据。K线由开盘时间唯一标识。
      tags:
        - market-data
      operationId: premiumIndexKlineData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#premium-index-kline-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/premiumIndexKlineData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/premium_index_kline_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/premium_index_kline_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/PremiumIndexKlineDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/PremiumIndexKlineData/PremiumIndexKlineData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/PremiumIndexKlineDataExample.php
      x-weight: |-
        based on parameter `LIMIT`

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
            example: BTCUSDT
          description: After CM migration, accepts both UM and CM symbols.
          x-description-cn: 交易对。迁移后支持传入 UM 与 CM 的 symbol。
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
            example: 50
            format: int64
            default: 500
            maximum: 1500
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
  /futures/data/delivery-price:
    get:
      summary: Quarterly Contract Settlement Price
      x-summary-cn: 季度合约历史结算价
      description: Latest price for a symbol or symbols.
      x-description-cn: 返回季度合约历史结算价
      tags:
        - market-data
      operationId: quarterlyContractSettlementPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#quarterly-contract-settlement-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/quarterlyContractSettlementPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/quarterly_contract_settlement_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/quarterly_contract_settlement_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/QuarterlyContractSettlementPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/QuarterlyContractSettlementPrice/QuarterlyContractSettlementPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/QuarterlyContractSettlementPriceExample.php
      x-ip-weight: 0
      parameters:
        - name: pair
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
      responses:
        "200":
          description: Quarterly Contract Settlement Price
          x-description-cn: Quarterly Contract Settlement 价格
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    deliveryTime:
                      type: integer
                      example: 1695945600000
                      format: int64
                    deliveryPrice:
                      type: number
                      example: 27103
                      format: float
  /fapi/v1/constituents:
    get:
      summary: Query Index Price Constituents
      x-summary-cn: 查询指数价格成分
      description: |-
        Query index price constituents

        **Note**:
        Prices from constituents of TradFi perps will be hiden and displayed as -1.
      x-description-cn: |-
        查询指数价格成分

        **注意：** 传统金融合约的成分价格将被隐藏，并统一显示为 -1。
      tags:
        - market-data
      operationId: queryIndexPriceConstituents
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#query-index-price-constituents
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/queryIndexPriceConstituents.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/query_index_price_constituents.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/query_index_price_constituents.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/QueryIndexPriceConstituentsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/QueryIndexPriceConstituents/QueryIndexPriceConstituents.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/QueryIndexPriceConstituentsExample.php
      x-ip-weight: 2
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
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
                    example: BTCUSDT
                  time:
                    type: integer
                    example: 1745401553408
                    format: int64
                  constituents:
                    type: array
                    example: []
                    items:
                      type: object
                      properties:
                        exchange:
                          type: string
                          example: binance
                        symbol:
                          type: string
                          example: BTCUSDT
                        price:
                          type: string
                          example: "94057.03000000"
                        weight:
                          type: string
                          example: "0.51282051"
  /fapi/v1/insuranceBalance:
    get:
      summary: Query Insurance Fund Balance Snapshot
      x-summary-cn: 查询保险基金余额快照
      description: Query Insurance Fund Balance Snapshot
      x-description-cn: 查询保险基金余额快照
      tags:
        - market-data
      operationId: queryInsuranceFundBalanceSnapshot
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#query-insurance-fund-balance-snapshot
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/queryInsuranceFundBalanceSnapshot.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/query_insurance_fund_balance_snapshot.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/query_insurance_fund_balance_snapshot.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/QueryInsuranceFundBalanceSnapshotExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/QueryInsuranceFundBalanceSnapshot/QueryInsuranceFundBalanceSnapshot.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/QueryInsuranceFundBalanceSnapshotExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BNBUSDT
          description: Symbol
          x-description-cn: 交易对
      responses:
        "200":
          description: Insurance Fund Balance Snapshot
          x-description-cn: 请参见英文说明：Insurance Fund Balance Snapshot
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbols:
                        type: array
                        example: []
                        items:
                          type: string
                          example: BNBUSDT
                      assets:
                        type: array
                        example: []
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: USDC
                            marginBalance:
                              type: string
                              example: "299999998.6497832"
                            updateTime:
                              type: integer
                              example: 1745366402000
                              format: int64
                  - type: array
                    items:
                      type: object
                      properties:
                        symbols:
                          type: array
                          example: []
                          items:
                            type: string
                            example: ADAUSDT
                        assets:
                          type: array
                          example: []
                          items:
                            type: object
                            properties:
                              asset:
                                type: string
                                example: USDT
                              marginBalance:
                                type: string
                                example: "314151411.06482935"
                              updateTime:
                                type: integer
                                example: 1745366402000
                                format: int64
  /fapi/v1/trades:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#recent-trades-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/recentTradesList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/recent_trades_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/recent_trades_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/RecentTradesListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/RecentTradesList/RecentTradesList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/RecentTradesListExample.php
      x-ip-weight: 5
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 50
            format: int64
            default: 500
            maximum: 1000
      x-parameters-notes: >-
        - Market trades means trades filled in the order book. Only market trades will be returned, which means the
        insurance fund trades and ADL trades won't be returned.
      x-parameters-notes-cn: "- 仅返回订单簿成交，即不会返回保险基金和自动减仓(ADL)成交"
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
                      x-description-cn: 成交ID
                      description: Id.
                    price:
                      type: string
                      example: "4.00000100"
                      x-description-cn: 成交价格
                      description: Price.
                    qty:
                      type: string
                      example: "12.00000000"
                      x-description-cn: 成交量
                      description: Qty.
                    quoteQty:
                      type: string
                      example: "48.00"
                      x-description-cn: 成交额
                      description: Quote Qty.
                    time:
                      type: integer
                      example: 1499865549590
                      format: int64
                      x-description-cn: 时间
                      description: Time.
                    isBuyerMaker:
                      type: boolean
                      example: true
                      x-description-cn: 买方是否为挂单方
                      description: Is Buyer Maker.
                    isRPITrade:
                      type: boolean
                      example: true
                      x-description-cn: Maker方是否为RPI挂单
                      description: Is RPITrade.
  /fapi/v1/rpiDepth:
    get:
      summary: RPI Order Book
      x-summary-cn: RPI深度信息
      description: |-
        Query symbol orderbook with RPI orders

        RPI(Retail Price Improvement) orders are included and aggreated in the
        response message. Crossed price levels are hidden and invisible.
      x-description-cn: 交易对深度信息，包含非交叉的RPI订单
      tags:
        - market-data
      operationId: rpiOrderBook
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#rpi-order-book
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/rpiOrderBook.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/rpi_order_book.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/rpi_order_book.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/RpiOrderBookExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/RpiOrderBook/RpiOrderBook.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/RpiOrderBookExample.php
      x-weight: |-
        Adjusted based on the limit:

        | Limit         | Weight |
        | ------------- | ------ |
        | 1000          | 20     |
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            format: int64
            default: 1000
          description: Valid limits:[1000]
          x-description-cn: 可选值:[1000]
      responses:
        "200":
          description: RPI Order Book
          x-description-cn: RPI 订单 Book
          content:
            application/json:
              schema:
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
                    x-description-cn: 消息时间
                  T:
                    type: integer
                    example: 1589436922959
                    format: int64
                    description: Transaction time
                    x-description-cn: 撮合引擎时间
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
  /fapi/v1/ticker/bookTicker:
    get:
      summary: Symbol Order Book Ticker
      x-summary-cn: 当前最优挂单
      description: |-
        Best price/qty on the order book for a symbol or symbols.

        Retail Price Improvement(RPI) orders are not visible and excluded in the
        response message.
      x-description-cn: 返回当前最优的挂单(最高买单，最低卖单)
      tags:
        - market-data
      operationId: symbolOrderBookTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#symbol-order-book-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/symbolOrderBookTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/symbol_order_book_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/symbol_order_book_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/SymbolOrderBookTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/SymbolOrderBookTicker/SymbolOrderBookTicker.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/SymbolOrderBookTickerExample.php
      x-weight: |-
        **2** for a single symbol;
        **5** when the symbol parameter is omitted
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
      x-parameters-notes: |-
        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.
        - The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.
      x-parameters-notes-cn: |-
        - 不发送交易对参数，则会返回所有交易对信息
        - 该接口返回头中的`X-MBX-USED-WEIGHT-1M`参数不准确，可以忽略
      responses:
        "200":
          description: Symbol Order Book Ticker
          x-description-cn: 交易对 订单 最优挂单
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                        x-description-cn: 交易对
                        description: Symbol.
                      bidPrice:
                        type: string
                        example: "4.00000000"
                        x-description-cn: 最优买单价
                        description: Bid Price.
                      bidQty:
                        type: string
                        example: "431.00000000"
                        x-description-cn: 挂单量
                        description: Bid Qty.
                      askPrice:
                        type: string
                        example: "4.00000200"
                        x-description-cn: 最优卖单价
                        description: Ask Price.
                      askQty:
                        type: string
                        example: "9.00000000"
                        x-description-cn: 挂单量
                        description: Ask Qty.
                      time:
                        type: integer
                        example: 1589437530011
                        format: int64
                        description: Transaction time
                        x-description-cn: 撮合引擎时间
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          x-description-cn: 交易对
                          description: Symbol.
                        bidPrice:
                          type: string
                          example: "4.00000000"
                          x-description-cn: 最优买单价
                          description: Bid Price.
                        bidQty:
                          type: string
                          example: "431.00000000"
                          x-description-cn: 挂单量
                          description: Bid Qty.
                        askPrice:
                          type: string
                          example: "4.00000200"
                          x-description-cn: 最优卖单价
                          description: Ask Price.
                        askQty:
                          type: string
                          example: "9.00000000"
                          x-description-cn: 挂单量
                          description: Ask Qty.
                        time:
                          type: integer
                          example: 1589437530011
                          format: int64
                          description: Transaction time
                          x-description-cn: 撮合引擎时间
  /fapi/v1/ticker/price:
    get:
      summary: Symbol Price Ticker
      x-summary-cn: 最新价格
      description: Latest price for a symbol or symbols.
      x-description-cn: 返回最近价格
      deprecated: true
      tags:
        - market-data
      operationId: symbolPriceTicker
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#symbol-price-ticker
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/symbolPriceTicker.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/symbol_price_ticker.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/symbol_price_ticker.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/SymbolPriceTickerExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/SymbolPriceTicker/SymbolPriceTicker.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/SymbolPriceTickerExample.php
      x-weight: |-
        1 for a single symbol;
        2 when the symbol parameter is omitted
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
      x-parameters-notes: "- If the symbol is not sent, prices for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 不发送交易对参数，则会返回所有交易对信息"
      responses:
        "200":
          description: Symbol Price Ticker
          x-description-cn: 交易对 价格 行情
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                        x-description-cn: 交易对
                        description: Symbol.
                      price:
                        type: string
                        example: "6000.01"
                        x-description-cn: 价格
                        description: Price.
                      time:
                        type: integer
                        example: 1589437530011
                        format: int64
                        description: Transaction time
                        x-description-cn: 撮合引擎时间
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          x-description-cn: 交易对
                          description: Symbol.
                        price:
                          type: string
                          example: "6000.01"
                          x-description-cn: 价格
                          description: Price.
                        time:
                          type: integer
                          example: 1589437530011
                          format: int64
                          description: Transaction time
                          x-description-cn: 撮合引擎时间
  /fapi/v2/ticker/price:
    get:
      summary: Symbol Price Ticker V2
      x-summary-cn: 最新价格V2
      description: Latest price for a symbol or symbols.
      x-description-cn: 返回最近价格
      tags:
        - market-data
      operationId: symbolPriceTickerV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#symbol-price-ticker-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/symbolPriceTickerV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/symbol_price_ticker_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/symbol_price_ticker_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/SymbolPriceTickerV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/SymbolPriceTickerV2/SymbolPriceTickerV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/SymbolPriceTickerV2Example.php
      x-weight: |-
        1 for a single symbol;
        2 when the symbol parameter is omitted
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
      x-parameters-notes: |-
        - If the symbol is not sent, prices for all symbols will be returned in an array.
        - The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.
      x-parameters-notes-cn: |-
        - 不发送交易对参数，则会返回所有交易对信息
        - 该接口返回头中的`X-MBX-USED-WEIGHT-1M`参数不准确，可以忽略
      responses:
        "200":
          description: Symbol Price Ticker V2
          x-description-cn: 交易对 价格 行情 V2
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                        x-description-cn: 交易对
                        description: Symbol.
                      price:
                        type: string
                        example: "6000.01"
                        x-description-cn: 价格
                        description: Price.
                      time:
                        type: integer
                        example: 1589437530011
                        format: int64
                        description: Transaction time
                        x-description-cn: 撮合引擎时间
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          x-description-cn: 交易对
                          description: Symbol.
                        price:
                          type: string
                          example: "6000.01"
                          x-description-cn: 价格
                          description: Price.
                        time:
                          type: integer
                          example: 1589437530011
                          format: int64
                          description: Transaction time
                          x-description-cn: 撮合引擎时间
  /futures/data/takerlongshortRatio:
    get:
      summary: Taker Buy/Sell Volume
      x-summary-cn: 合约主动买卖量
      description: Taker Buy/Sell Volume
      x-description-cn: 合约主动买卖量
      tags:
        - market-data
      operationId: takerBuySellVolume
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#taker-buy-sell-volume
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/takerBuySellVolume.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/taker_buy_sell_volume.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/taker_buy_sell_volume.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/TakerBuySellVolumeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/TakerBuySellVolume/TakerBuySellVolume.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/TakerBuySellVolumeExample.php
      x-ip-weight: 0
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
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
            example: 50
            format: int64
            default: 30
            maximum: 500
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
        - IP rate limit 1000 requests/5min
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的 limit 值
        - 仅支持最近 30 天的数据
        - IP限频为1000次/5min
      responses:
        "200":
          description: Taker Buy/Sell Volume
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    buySellRatio:
                      type: string
                      example: "1.5586"
                    buyVol:
                      type: string
                      example: "387.3300"
                    sellVol:
                      type: string
                      example: "248.5030"
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: Start time of the period, in milliseconds.
                      x-description-cn: 该周期的开始时间，单位为毫秒。
  /fapi/v1/ping:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#test-connectivity
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/testConnectivity.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/test_connectivity.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/test_connectivity.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/TestConnectivityExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/TestConnectivity/TestConnectivity.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/TestConnectivityExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: OK
          x-description-cn: 成功
  /fapi/v1/ticker/24hr:
    get:
      summary: 24hr Ticker Price Change Statistics
      x-summary-cn: 24hr价格变动情况
      description: |-
        24 hour rolling window price change statistics.
        **Careful** when accessing this with no symbol.
      x-description-cn: 请注意，不携带symbol参数会返回全部交易对数据，不仅数据庞大，而且权重极高
      tags:
        - market-data
      operationId: ticker24hrPriceChangeStatistics
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#ticker24hr-price-change-statistics
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/ticker24hrPriceChangeStatistics.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/ticker24hr_price_change_statistics.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/ticker24hr_price_change_statistics.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/Ticker24hrPriceChangeStatisticsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/Ticker24hrPriceChangeStatistics/Ticker24hrPriceChangeStatistics.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/Ticker24hrPriceChangeStatisticsExample.php
      x-weight: |-
        **1** for a single symbol;
        **40** when the symbol parameter is omitted
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
      x-parameters-notes: "- If the symbol is not sent, tickers for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 不发送交易对参数，则会返回所有交易对信息"
      responses:
        "200":
          description: 24hr Ticker Price Change Statistics
          x-description-cn: 24hr 行情 价格 修改Statistics
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      priceChange:
                        type: string
                        example: "-94.99999800"
                        x-description-cn: 24小时价格变动
                        description: Price Change.
                      priceChangePercent:
                        type: string
                        example: "-95.960"
                        x-description-cn: 24小时价格变动百分比
                        description: Price Change Percent.
                      weightedAvgPrice:
                        type: string
                        example: "0.29628482"
                        x-description-cn: 加权平均价
                        description: Weighted Avg Price.
                      lastPrice:
                        type: string
                        example: "4.00000200"
                        x-description-cn: 最近一次成交价
                        description: Last Price.
                      lastQty:
                        type: string
                        example: "200.00000000"
                        x-description-cn: 最近一次成交额
                        description: Last Qty.
                      openPrice:
                        type: string
                        example: "99.00000000"
                        x-description-cn: 24小时内第一次成交的价格
                        description: Open Price.
                      highPrice:
                        type: string
                        example: "100.00000000"
                        x-description-cn: 24小时最高价
                        description: High Price.
                      lowPrice:
                        type: string
                        example: "0.10000000"
                        x-description-cn: 24小时最低价
                        description: Low Price.
                      volume:
                        type: string
                        example: "8913.30000000"
                        x-description-cn: 24小时成交量
                        description: Volume.
                      quoteVolume:
                        type: string
                        example: "15.30000000"
                        x-description-cn: 24小时成交额
                        description: Quote Volume.
                      openTime:
                        type: integer
                        example: 1499783499040
                        format: int64
                        x-description-cn: 24小时内，第一笔交易的发生时间
                        description: Open Time.
                      closeTime:
                        type: integer
                        example: 1499869899040
                        format: int64
                        x-description-cn: 24小时内，最后一笔交易的发生时间
                        description: Close Time.
                      firstId:
                        type: integer
                        example: 28385
                        format: int64
                        description: First tradeId
                        x-description-cn: 首笔成交id
                      lastId:
                        type: integer
                        example: 28460
                        format: int64
                        description: Last tradeId
                        x-description-cn: 末笔成交id
                      count:
                        type: integer
                        example: 76
                        format: int64
                        description: Trade count
                        x-description-cn: 成交笔数
                  - type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                        priceChange:
                          type: string
                          example: "-94.99999800"
                          x-description-cn: 24小时价格变动
                          description: Price Change.
                        priceChangePercent:
                          type: string
                          example: "-95.960"
                          x-description-cn: 24小时价格变动百分比
                          description: Price Change Percent.
                        weightedAvgPrice:
                          type: string
                          example: "0.29628482"
                          x-description-cn: 加权平均价
                          description: Weighted Avg Price.
                        lastPrice:
                          type: string
                          example: "4.00000200"
                          x-description-cn: 最近一次成交价
                          description: Last Price.
                        lastQty:
                          type: string
                          example: "200.00000000"
                          x-description-cn: 最近一次成交额
                          description: Last Qty.
                        openPrice:
                          type: string
                          example: "99.00000000"
                          x-description-cn: 24小时内第一次成交的价格
                          description: Open Price.
                        highPrice:
                          type: string
                          example: "100.00000000"
                          x-description-cn: 24小时最高价
                          description: High Price.
                        lowPrice:
                          type: string
                          example: "0.10000000"
                          x-description-cn: 24小时最低价
                          description: Low Price.
                        volume:
                          type: string
                          example: "8913.30000000"
                          x-description-cn: 24小时成交量
                          description: Volume.
                        quoteVolume:
                          type: string
                          example: "15.30000000"
                          x-description-cn: 24小时成交额
                          description: Quote Volume.
                        openTime:
                          type: integer
                          example: 1499783499040
                          format: int64
                          x-description-cn: 24小时内，第一笔交易的发生时间
                          description: Open Time.
                        closeTime:
                          type: integer
                          example: 1499869899040
                          format: int64
                          x-description-cn: 24小时内，最后一笔交易的发生时间
                          description: Close Time.
                        firstId:
                          type: integer
                          example: 28385
                          format: int64
                          description: First tradeId
                          x-description-cn: 首笔成交id
                        lastId:
                          type: integer
                          example: 28460
                          format: int64
                          description: Last tradeId
                          x-description-cn: 末笔成交id
                        count:
                          type: integer
                          example: 76
                          format: int64
                          description: Trade count
                          x-description-cn: 成交笔数
  /futures/data/topLongShortAccountRatio:
    get:
      summary: Top Trader Long/Short Account Ratio (MARKET_DATA)
      x-summary-cn: 大户账户数多空比 (MARKET_DATA)
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#top-trader-long-short-ratio-accounts
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/topTraderLongShortRatioAccounts.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/top_trader_long_short_ratio_accounts.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/top_trader_long_short_ratio_accounts.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/TopTraderLongShortRatioAccountsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/TopTraderLongShortRatioAccounts/TopTraderLongShortRatioAccounts.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/TopTraderLongShortRatioAccountsExample.php
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
            example: BTCUSDT
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
            example: 50
            format: int64
            default: 30
            maximum: 500
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
        - IP rate limit 1000 requests/5min
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
        - IP限频为1000次/5min
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
                    symbol:
                      type: string
                      example: BTCUSDT
                    longShortRatio:
                      type: string
                      example: "1.8105"
                      description: long/short account num ratio of top traders
                      x-description-cn: 大户多空账户数比值
                    longAccount:
                      type: string
                      example: "0.6442"
                      description: long account num ratio of top traders
                      x-description-cn: 大户多仓账户数比例
                    shortAccount:
                      type: string
                      example: "0.3558"
                      description: long account num ratio of top traders
                      x-description-cn: 大户空仓账户数比例
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /futures/data/topLongShortPositionRatio:
    get:
      summary: Top Trader Long/Short Position Ratio (MARKET_DATA)
      x-summary-cn: 大户持仓量多空比 (MARKET_DATA)
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#top-trader-long-short-ratio-positions
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/topTraderLongShortRatioPositions.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/top_trader_long_short_ratio_positions.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/top_trader_long_short_ratio_positions.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/TopTraderLongShortRatioPositionsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/TopTraderLongShortRatioPositions/TopTraderLongShortRatioPositions.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/TopTraderLongShortRatioPositionsExample.php
      x-ip-weight: 0
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
            example: BTCUSDT
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
            example: 50
            format: int64
            default: 30
            maximum: 500
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
        - IP rate limit 1000 requests/5min
      x-parameters-notes-cn: |-
        - 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
        - 仅支持最近30天的数据
        - IP限频为1000次/5min
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
                    symbol:
                      type: string
                      example: BTCUSDT
                    longShortRatio:
                      type: string
                      example: "1.4342"
                      description: long/short position ratio of top traders
                      x-description-cn: 大户多空持仓量比值
                    longAccount:
                      type: string
                      example: "0.5344"
                      description: long positions ratio of top traders
                      x-description-cn: 大户多仓持仓量比例
                    shortAccount:
                      type: string
                      example: "0.4238"
                      description: short positions ratio of top traders
                      x-description-cn: 大户空仓持仓量比例
                    timestamp:
                      type: integer
                      example: 1591261042378
                      format: int64
                      description: End time of the period, in milliseconds.
                      x-description-cn: 该周期的结束时间，单位为毫秒。
  /fapi/v1/tradingSchedule:
    get:
      summary: Trading Schedule
      x-summary-cn: 交易时段
      description: >-
        Trading session schedules for the underlying assets of TradFi Perps are provided for a one-week period forward
        and one-week period backward starting from the day prior to the query time, covering the U.S. equity market,
        Korean equity market, Hong Kong equity market, China equity market, the commodity market, and the FX market.


        Session types per market:

        - U.S. equity market: "PRE_MARKET", "REGULAR", "AFTER_MARKET", "OVERNIGHT", "NO_TRADING".

        - Commodity market: "REGULAR", "NO_TRADING".

        - Korean equity market: "REGULAR", "NO_TRADING".

        - Hong Kong equity market: "REGULAR", "NO_TRADING".

        - China equity market: "REGULAR", "NO_TRADING".

        - FX market: "REGULAR", "NO_TRADING".
      x-description-cn: |-
        从查询时间的前一日起算、返回往后为期一周以及往前为期一周的传统金融合约标的资产的交易时段信息，覆盖美国股票市场，韩国股票市场，香港股票市场，中国股票市场，商品市场和外汇市场。

        各市场时段类型：
        - 美股市场："PRE_MARKET"、"REGULAR"、"AFTER_MARKET"、"OVERNIGHT"、"NO_TRADING"。
        - 商品市场："REGULAR"、"NO_TRADING"。
        - 韩国股票市场："REGULAR"、"NO_TRADING"。
        - 香港股票市场："REGULAR"、"NO_TRADING"。
        - 中国股票市场："REGULAR"、"NO_TRADING"。
        - 外汇市场："REGULAR"、"NO_TRADING"。
      tags:
        - market-data
      operationId: tradingSchedule
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data#trading-schedule
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/MarketDataApi/tradingSchedule.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/market_data_api/trading_schedule.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/MarketData/trading_schedule.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/marketdata/TradingScheduleExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/MarketDataAPI/TradingSchedule/TradingSchedule.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/marketdata/TradingScheduleExample.php
      x-ip-weight: 5
      parameters: []
      responses:
        "200":
          description: Trading Schedule
          x-description-cn: 请参见英文说明：Trading Schedule
          content:
            application/json:
              schema:
                type: object
                properties:
                  updateTime:
                    type: integer
                    example: 1761286643918
                    format: int64
                  marketSchedules:
                    type: object
                    example: {}
                    properties:
                      EQUITY:
                        type: object
                        example: {}
                        properties:
                          sessions:
                            type: array
                            example: []
                            items:
                              type: object
                              properties:
                                startTime:
                                  type: integer
                                  example: 1761177600000
                                  format: int64
                                endTime:
                                  type: integer
                                  example: 1761206400000
                                  format: int64
                                type:
                                  type: string
                                  example: OVERNIGHT
                      COMMODITY:
                        type: object
                        example: {}
                        properties:
                          sessions:
                            type: array
                            example: []
                            items:
                              type: object
                              properties:
                                startTime:
                                  type: integer
                                  example: 1761724800000
                                  format: int64
                                endTime:
                                  type: integer
                                  example: 1761744600000
                                  format: int64
                                type:
                                  type: string
                                  example: NO_TRADING
                      KR_EQUITY:
                        type: object
                        example: {}
                        properties:
                          sessions:
                            type: array
                            example: []
                            items:
                              type: object
                              properties:
                                startTime:
                                  type: integer
                                  example: 1779958800000
                                  format: int64
                                endTime:
                                  type: integer
                                  example: 1780009200000
                                  format: int64
                                type:
                                  type: string
                                  example: NO_TRADING
                      HK_EQUITY:
                        type: object
                        example: {}
                        properties:
                          sessions:
                            type: array
                            example: []
                            items:
                              type: object
                              properties:
                                startTime:
                                  type: integer
                                  example: 1779955200000
                                  format: int64
                                endTime:
                                  type: integer
                                  example: 1780018200000
                                  format: int64
                                type:
                                  type: string
                                  example: NO_TRADING
                      CN_EQUITY:
                        type: object
                        example: {}
                        properties:
                          sessions:
                            type: array
                            example: []
                            items:
                              type: object
                              properties:
                                startTime:
                                  type: integer
                                  example: 1779955200000
                                  format: int64
                                endTime:
                                  type: integer
                                  example: 1780018200000
                                  format: int64
                                type:
                                  type: string
                                  example: NO_TRADING
                      FX:
                        type: object
                        example: {}
                        properties:
                          sessions:
                            type: array
                            example: []
                            items:
                              type: object
                              properties:
                                startTime:
                                  type: integer
                                  example: 1779966000000
                                  format: int64
                                endTime:
                                  type: integer
                                  example: 1780027200000
                                  format: int64
                                type:
                                  type: string
                                  example: NO_TRADING
  /fapi/v1/pmAccountInfo:
    get:
      summary: Classic Portfolio Margin Account Information (USER_DATA)
      x-summary-cn: Classic Portfolio 杠杆 账户 信息 (USER_DATA)
      description: Get Classic Portfolio Margin current account information.
      x-description-cn: 查询经典统一账户当前账户信息
      tags:
        - portfolio-margin-endpoints
      operationId: classicPortfolioMarginAccountInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/portfolio-margin-endpoints#classic-portfolio-margin-account-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/PortfolioMarginEndpointsApi/classicPortfolioMarginAccountInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/portfolio_margin_endpoints_api/classic_portfolio_margin_account_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/PortfolioMarginEndpoints/classic_portfolio_margin_account_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/portfoliomarginendpoints/ClassicPortfolioMarginAccountInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/PortfolioMarginEndpointsAPI/ClassicPortfolioMarginAccountInformation/ClassicPortfolioMarginAccountInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/portfoliomarginendpoints/ClassicPortfolioMarginAccountInformationExample.php
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
            example: BTC
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
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- maxWithdrawAmount is for asset transfer out to the spot wallet."
      x-parameters-notes-cn: "- 最大可转出余额指可以转出到现货钱包到金额。"
      responses:
        "200":
          description: Classic Portfolio Margin Account Information
          x-description-cn: Classic Portfolio 杠杆 账户 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  maxWithdrawAmountUSD:
                    type: string
                    example: "1627523.32459208"
                    description: Classic Portfolio margin maximum virtual amount for transfer out in USD
                    x-description-cn: Classic Portfolio 杠杆账户最大可转出金额，单位为美元
                  asset:
                    type: string
                    example: BTC
                    description: asset name
                    x-description-cn: 资产
                  maxWithdrawAmount:
                    type: string
                    example: "27.43689636"
                    description: maximum amount for transfer out
                    x-description-cn: 最大可转出余额
  /fapi/v1/userTrades:
    get:
      summary: Account Trade List (USER_DATA)
      x-summary-cn: 账户成交历史 (USER_DATA)
      description: Get trades for a specific account and symbol.
      x-description-cn: 获取某交易对的成交历史
      tags:
        - trade
      operationId: accountTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#account-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/accountTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/account_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/account_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/AccountTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/AccountTradeList/AccountTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/AccountTradeListExample.php
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
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 25851813
            format: int64
          description: Must be used together with parameter `symbol`.
          x-description-cn: 必须要和参数`symbol`一起使用
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
            example: 1
            format: int64
          description: Trade id to fetch from. Default gets most recent trades.
          x-description-cn: 从该交易ID开始获取数据. 默认获取最近的交易数据.
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 50
            format: int64
            default: 500
            maximum: 1000
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
        - If `startTime` and `endTime` are both not sent, then the last 7 days' data will be returned.
        - The time between `startTime` and `endTime` cannot be longer than 7 days.
        - The parameter `fromId` cannot be sent with `startTime` or `endTime`.
        - Only support querying trade in the past 3 months
      x-parameters-notes-cn: |-
        - 如果`startTime` 和 `endTime` 均未发送, 只会返回最近7天的数据。
        - startTime 和 endTime 的最大间隔为7天
        - 参数 fromId 不能和startTime 与 endTime一起发送
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
                    buyer:
                      type: boolean
                      example: false
                      x-description-cn: 是否是买方
                      description: Buyer.
                    commission:
                      type: string
                      example: "0.07819010"
                      x-description-cn: 手续费
                      description: Commission.
                    commissionAsset:
                      type: string
                      example: USDT
                      x-description-cn: 手续费计价单位
                      description: Commission Asset.
                    id:
                      type: integer
                      example: 698759
                      format: int64
                      x-description-cn: 交易ID
                      description: Id.
                    maker:
                      type: boolean
                      example: false
                      x-description-cn: 是否是挂单方
                      description: Maker.
                    orderId:
                      type: integer
                      example: 25851813
                      format: int64
                      x-description-cn: 订单编号
                      description: Order Id.
                    price:
                      type: string
                      example: "7819.01"
                      x-description-cn: 成交价
                      description: Price.
                    qty:
                      type: string
                      example: "0.002"
                      x-description-cn: 成交量
                      description: Qty.
                    quoteQty:
                      type: string
                      example: "15.63802"
                      x-description-cn: 计价资产成交额。U 本位合约交易对返回该值；币本位合约交易对返回 "0"。
                      description: Quote asset quantity. Populated for USDⓈ-M symbols; returns "0" for COIN-M symbols.
                    baseQty:
                      type: string
                      example: "0"
                      x-description-cn: 标的资产成交量。币本位合约交易对返回该值；U 本位合约交易对返回 "0"。
                      description: Base asset quantity. Populated for COIN-M symbols; returns "0" for USDⓈ-M symbols.
                    marginAsset:
                      type: string
                      example: USDT
                      x-description-cn: 保证金币种
                      description: Margin Asset.
                    realizedPnl:
                      type: string
                      example: "-0.91539999"
                      x-description-cn: 实现盈亏
                      description: Realized Pnl.
                    side:
                      type: string
                      example: SELL
                      x-description-cn: 买卖方向
                      description: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      x-description-cn: 持仓方向
                      description: Position Side.
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    pair:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 标的交易对
                      description: Pair.
                    time:
                      type: integer
                      example: 1569514978020
                      format: int64
                      x-description-cn: 时间
                      description: Time.
  /fapi/v1/allOrders:
    get:
      summary: All Orders (USER_DATA)
      x-summary-cn: 查询所有订单(包括历史订单) (USER_DATA)
      description: |-
        Get all account orders; active, canceled, or filled.

        - These orders will not be found:
          - order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
          - order create time + 90 days < current time
      x-description-cn: |-
        查询所有订单(包括历史订单)

        - 请注意，如果订单满足如下条件，不会被查询到：
          - 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
          - 订单创建时间 + 90天 < 当前时间
      tags:
        - trade
      operationId: allOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#all-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/allOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/all_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/all_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/AllOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/AllOrders/AllOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/AllOrdersExample.php
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
            example: 50
            format: int64
            default: 500
            maximum: 1000
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
        - If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
        - The query time period must be less then 7 days( default as the recent 7 days).
      x-parameters-notes-cn: |-
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
                      example: "0.00000"
                      x-description-cn: 平均成交价
                      description: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      x-description-cn: 用户自定义的订单号
                      description: Client Order Id.
                    cumQuote:
                      type: string
                      example: "0"
                      x-description-cn: 成交金额
                      description: Cum Quote.
                    cumBase:
                      type: string
                      example: "0"
                      x-description-cn: 成交金额(标的数量)
                      description: Cum Base.
                    executedQty:
                      type: string
                      example: "0"
                      x-description-cn: 成交量
                      description: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      x-description-cn: 系统订单号
                      description: Order Id.
                    origQty:
                      type: string
                      example: "0.40"
                      x-description-cn: 原始委托数量
                      description: Orig Qty.
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 触发前订单类型
                      description: Orig Type.
                    price:
                      type: string
                      example: "0"
                      x-description-cn: 委托价格
                      description: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      x-description-cn: 是否仅减仓
                      description: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      x-description-cn: 买卖方向
                      description: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      x-description-cn: 持仓方向
                      description: Position Side.
                    status:
                      type: string
                      example: NEW
                      x-description-cn: 订单状态
                      description: Status.
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    pair:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 标的交易对
                      description: Pair.
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: 订单时间
                    timeInForce:
                      type: string
                      example: GTC
                      x-description-cn: 有效方法
                      description: Time In Force.
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 订单类型
                      description: Type.
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
                      x-description-cn: 条件价格触发类型
                      description: Working Type.
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
                      example: 0
                      format: int64
                      description: order pre-set auot cancel time for TIF GTD order
                      x-description-cn: 订单TIF为GTD时的自动取消时间
  /fapi/v1/countdownCancelAll:
    post:
      summary: Auto-Cancel All Open Orders (TRADE)
      x-summary-cn: 倒计时撤销所有订单 (TRADE)
      description: |-
        Cancel all open orders of the specified symbol at the end of the specified countdown.

        The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and
        replaced by a new one.

        Example usage:

        Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
        If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically
        canceled.
        If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.

        The system will check all countdowns **approximately every 10 milliseconds**, so please note that sufficient
        redundancy should be considered when using this function. We do not recommend setting the countdown time to be
        too precise or too small.
      x-description-cn: |-
        * 该接口可以被用于确保在倒计时结束时撤销指定symbol上的所有挂单。 在使用这个功能时，接口应像心跳一样在倒计时内被反复调用，以便可以取消既有的倒计时并开始新的倒数计时设置。

        * 用法示例：
        以30s的间隔重复此接口，每次倒计时countdownTime设置为120000(120s)。
        如果在120秒内未再次调用此接口，则您指定symbol上的所有挂单都会被自动撤销。
        如果在120秒内以将countdownTime设置为0，则倒数计时器将终止，自动撤单功能取消。

        * 系统会**大约每10毫秒**检查一次所有倒计时情况，因此请注意，使用此功能时应考虑足够的冗余。
        我们不建议将倒记时设置得太精确或太小。
      tags:
        - trade
      operationId: autoCancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#auto-cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/autoCancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/auto_cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/auto_cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/AutoCancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/AutoCancelAllOpenOrders/AutoCancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/AutoCancelAllOpenOrdersExample.php
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
                  example: BTCUSDT
                countdownTime:
                  type: integer
                  example: 1000
                  format: int64
                  description: Countdown in milliseconds. `1000` means 1 second; `0` disables countdown cancel-all.
                  x-description-cn: 倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
          description: Auto-Cancel All Open Orders
          x-description-cn: Auto-取消All 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  symbol:
                    type: string
                    example: BTCUSDT
                  countdownTime:
                    type: string
                    example: "100000"
  /fapi/v1/algoOrder:
    delete:
      summary: Cancel Algo Order (TRADE)
      x-summary-cn: 撤销条件订单 (TRADE)
      description: >-
        Cancel an active algo (conditional) order, including TP/SL (Take Profit / Stop Loss) and trailing stop orders on
        USD-M Futures.
      x-description-cn: 撤销当前有效的条件单（Algo / Conditional Order），覆盖 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。
      tags:
        - trade
      operationId: cancelAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#cancel-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/cancelAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/cancel_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/cancel_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CancelAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CancelAlgoOrder/CancelAlgoOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CancelAlgoOrderExample.php
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
        - name: clientAlgoId
          in: query
          required: false
          schema:
            type: string
            example: 6B2I9XVcJpCjqPAJ4YoFX7
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
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- Either `algoId` or `clientAlgoId` must be sent."
      x-parameters-notes-cn: "- `algoId` 与 `clientAlgoId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel Algo Order
          x-description-cn: 取消Algo 订单
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
                  code:
                    type: string
                    example: "200"
                  msg:
                    type: string
                    example: success
    post:
      summary: New Algo Order (TRADE)
      x-summary-cn: 下条件单 (TRADE)
      description: >-
        Send in a new algo (conditional) order. Use this endpoint to place **TP/SL (Take Profit / Stop Loss)** and
        trailing stop orders on USD-M Futures. Supported order types under `algoType=CONDITIONAL` are `STOP_MARKET`,
        `TAKE_PROFIT_MARKET`, `STOP`, `TAKE_PROFIT`, and `TRAILING_STOP_MARKET`.
      x-description-cn: >-
        下新的条件单（Algo / Conditional Order），用于 U 本位合约的**止盈止损（TP/SL, Take Profit / Stop Loss）**和追踪止损（Trailing Stop）。在
        `algoType=CONDITIONAL` 下，支持的订单类型为
        `STOP_MARKET`、`TAKE_PROFIT_MARKET`、`STOP`、`TAKE_PROFIT`、`TRAILING_STOP_MARKET`。
      tags:
        - trade
      operationId: newAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#new-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/newAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/new_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/new_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/NewAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/NewAlgoOrder/NewAlgoOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/NewAlgoOrderExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
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
      x-parameters-notes: >-
        - Algo order with type `STOP`, parameter `timeInForce` can be sent (default `GTC`).

        - Algo order with type `TAKE_PROFIT`, parameter `timeInForce` can be sent ( default `GTC`).

        - Condition orders will be triggered when:
          - If parameter`priceProtect`is sent as true:
            - when price reaches the `triggerPrice` ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
            - "triggerProtect" of a symbol can be got from `GET /fapi/v1/exchangeInfo`
          - `STOP`, `STOP_MARKET`:
            - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `triggerPrice`
            - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `triggerPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`:
            - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `triggerPrice`
            - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `triggerPrice`
          - `TRAILING_STOP_MARKET`:
            - BUY: the lowest price after order placed <= `activatePrice`, and the latest price >= the lowest price * (1 + `callbackRate`)
            - SELL: the highest price after order placed >= `activatePrice`, and the latest price <= the highest price * (1 - `callbackRate`)
        - For `TRAILING_STOP_MARKET`, if you got such error code. > `{"code": -2021, "msg": "Order would immediately
        trigger."}` > means that the parameters you send do not meet the following requirements:
          - BUY: `activatePrice` should be smaller than latest price.
          - SELL: `activatePrice` should be larger than latest price.
        - `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`:
          - Follow the same rules for condition orders.
          - If triggered，**close all** current long position( if `SELL`) or current short position( if `BUY`).
          - Cannot be used with `quantity` paremeter
          - Cannot be used with `reduceOnly` parameter
          - In Hedge Mode,cannot be used with `BUY` orders in `LONG` position side. and cannot be used with `SELL` orders in `SHORT` position side
        - `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.
      x-parameters-notes-cn: |-
        - 类型为 `STOP` 的条件订单可以传入参数 `timeInForce`（默认值为 `GTC`）。
        - 类型为 `TAKE_PROFIT` 的条件订单可以传入参数 `timeInForce`（默认值为 `GTC`）。
        - 条件单的触发必须:
          - 如果订单参数`priceProtect`为true:
            - 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
            - 触发保护阈值请参考接口`GET /fapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
          - `STOP`, `STOP_MARKET` 止损单:
            - 买入: 最新合约价格/标记价格高于等于触发价`triggerPrice`
            - 卖出: 最新合约价格/标记价格低于等于触发价`triggerPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单:
            - 买入: 最新合约价格/标记价格低于等于触发价`triggerPrice`
            - 卖出: 最新合约价格/标记价格高于等于触发价`triggerPrice`
          - `TRAILING_STOP_MARKET` 跟踪止损单:
            - 买入: 当合约价格/标记价格区间最低价格低于激活价格`activatePrice`,且最新合约价格/标记价高于等于最低价设定回调幅度。
            - 卖出: 当合约价格/标记价格区间最高价格高于激活价格`activatePrice`,且最新合约价格/标记价低于等于最高价设定回调幅度。
        - `TRAILING_STOP_MARKET` 跟踪止损单如果遇到报错 `{"code": -2021, "msg": "Order would immediately trigger."}` > 表示订单不满足以下条件:
          - 买入: 指定的`activatePrice` 必须小于 latest price
          - 卖出: 指定的`activatePrice` 必须大于 latest price
        - `STOP_MARKET`, `TAKE_PROFIT_MARKET` 配合 `closePosition`=`true`:
          - 条件单触发依照上述条件单触发逻辑
          - 条件触发后，平掉当时持有所有多头仓位(若为卖单)或当时持有所有空头仓位(若为买单)
          - 不支持 `quantity` 参数
          - 自带只平仓属性，不支持`reduceOnly`参数
          - 双开模式下,`LONG`方向上不支持`BUY`; `SHORT` 方向上不支持`SELL`
        - `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
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
                symbol:
                  type: string
                  example: BNBUSDT
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                positionSide:
                  type: string
                  example: BOTH
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
                type:
                  type: string
                  example: STOP_MARKET
                  enum:
                    - LIMIT
                    - MARKET
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
                    - GTD
                    - RPI
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                  description: Cannot be sent with `closePosition`=`true`(Close-All)
                  x-description-cn: 下单数量,使用`closePosition`不支持此参数。
                price:
                  type: number
                  example: "1.0"
                  format: float
                triggerPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: Trigger price
                  x-description-cn: 触发价
                workingType:
                  type: string
                  example: MARK_PRICE
                  default: CONTRACT_PRICE
                  enum:
                    - MARK_PRICE
                    - CONTRACT_PRICE
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
                  x-description-cn: 仅 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单类型可用；不能与 `price` 参数同时使用
                closePosition:
                  type: string
                  example: "true"
                  enum:
                    - "true"
                    - "false"
                  description: Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.
                  x-description-cn: 触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用"
                priceProtect:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: >-
                    Used with `STOP_MARKET` or `TAKE_PROFIT_MARKET` order. when price reaches the triggerPrice ，the
                    difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the Price Protection
                    Threshold of the symbol.'
                  x-description-cn: 仅 `STOP_MARKET` 和 `TAKE_PROFIT_MARKET` 订单类型可用。当价格达到触发价时，标记价格与合约最新价之间的价差不能超过该symbol的触发保护阈值。
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`'
                  x-description-cn: 双开模式下不接受此参数； 使用`closePosition`不支持此参数。"
                activatePrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: >-
                    Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different
                    `workingType`)
                  x-description-cn: 追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)
                callbackRate:
                  type: number
                  example: 1
                  format: float
                  minimum: 0.1
                  maximum: 20
                  description: Used with `TRAILING_STOP_MARKET` orders
                  x-description-cn: 追踪止损回调比例，可取值范围[0.1, 20],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数
                clientAlgoId:
                  type: string
                  example: "1"
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Can only be string following the
                    rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                  x-description-cn: 用户自定义的条件订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                newOrderRespType:
                  type: string
                  example: ACK
                  default: ACK
                  enum:
                    - ACK
                    - RESULT
                selfTradePreventionMode:
                  type: string
                  example: EXPIRE_TAKER
                  default: NONE
                  enum:
                    - NONE
                    - EXPIRE_TAKER
                    - EXPIRE_BOTH
                    - EXPIRE_MAKER
                  description: >-
                    `EXPIRE_TAKER`: expire taker order when STP triggers / `EXPIRE_MAKER`: expire taker order when STP
                    triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`
                  x-description-cn: 订单自成交保护模式，默认 `NONE`。
                goodTillDate:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                    timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp
                    must be greater than the current time plus 600 seconds and smaller than 253402300799000
                  x-description-cn: >-
                    TIF为GTD时订单的自动取消时间，
                    当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000
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
          description: New Algo Order
          x-description-cn: New Algo 订单
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
    get:
      summary: Query Algo Order (USER_DATA)
      x-summary-cn: 查询条件订单 (USER_DATA)
      description: >-
        Check the status of an algo (conditional) order, such as TP/SL (Take Profit / Stop Loss) or trailing stop orders
        on USD-M Futures.


        * These orders will not be found:
          * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
          * order create time + 90 days < current time
      x-description-cn: |-
        查询条件订单（Algo / Conditional Order）的状态，包括 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。

        * 请注意，如果订单满足如下条件，不会被查询到：
          * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
          * 订单创建时间 + 90天 < 当前时间
      tags:
        - trade
      operationId: queryAlgoOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#query-algo-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/queryAlgoOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/query_algo_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/query_algo_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/QueryAlgoOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/QueryAlgoOrder/QueryAlgoOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/QueryAlgoOrderExample.php
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
            example: 1
            format: int64
          description: Order ID
          x-description-cn: 系统订单号
        - name: clientAlgoId
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
        - Either `algoId` or `clientAlgoId` must be sent.
        - `algoId` is self-increment for each specific `symbol`
      x-parameters-notes-cn: |-
        - 至少需要发送 `algoId` 与 `clientAlgoId`中的一个
        - `algoId`在`symbol`维度是自增的
      responses:
        "200":
          description: Algo Order
          x-description-cn: Algo 订单
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
                    description: Empty string if not triggered; orderId if triggered.
                    x-description-cn: 未触发时为空字符串；触发后为 orderId。
                  actualPrice:
                    type: string
                    example: "0.00000"
                    description: 0 if not triggered; average price if filled/partially filled.
                    x-description-cn: 未触发时为 0；成交或部分成交后为平均成交价。
                  actualType:
                    type: string
                    example: LIMIT
                    description: Optional field, only present when triggered.
                    x-description-cn: 仅在触发后返回的可选字段。
                  actualQty:
                    type: string
                    example: "0.01"
                    description: Optional field, only present when filled/partially filled.
                    x-description-cn: 仅在成交或部分成交后返回的可选字段。
                  triggerPrice:
                    type: string
                    example: "750.000"
                  price:
                    type: string
                    example: "750.000"
                  icebergQuantity:
                    type: string
                    example: "null"
                    description: Reserved field, ignore.
                    x-description-cn: 预留字段，请忽略。
                  tpOrderType:
                    type: string
                    example: ""
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
  /fapi/v1/algoOpenOrders:
    delete:
      summary: Cancel All Algo Open Orders (TRADE)
      x-summary-cn: 撤销全部条件订单 (TRADE)
      description: >-
        Cancel all open algo (conditional) orders on a symbol, including TP/SL (Take Profit / Stop Loss) and trailing
        stop orders on USD-M Futures.
      x-description-cn: 撤销某个交易对下的全部条件挂单（Algo / Conditional Order），覆盖 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing Stop）订单。
      tags:
        - trade
      operationId: cancelAllAlgoOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#cancel-all-algo-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/cancelAllAlgoOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/cancel_all_algo_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/cancel_all_algo_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CancelAllAlgoOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CancelAllAlgoOpenOrders/CancelAllAlgoOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CancelAllAlgoOpenOrdersExample.php
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
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Cancel All Algo Open Orders
          x-description-cn: 取消All Algo 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                  msg:
                    type: string
                    example: The operation of cancel all open order is done.
  /fapi/v1/allOpenOrders:
    delete:
      summary: Cancel All Open Orders (TRADE)
      x-summary-cn: 撤销全部订单 (TRADE)
      description: Cancel All Open Orders
      x-description-cn: 撤销全部订单 (TRADE)
      tags:
        - trade
      operationId: cancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/cancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CancelAllOpenOrders/CancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CancelAllOpenOrdersExample.php
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
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
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
                  msg:
                    type: string
                    example: The operation of cancel all open order is done.
  /fapi/v1/batchOrders:
    delete:
      summary: Cancel Multiple Orders (TRADE)
      x-summary-cn: 批量撤销订单 (TRADE)
      description: Cancel Multiple Orders
      x-description-cn: 批量撤销订单 (TRADE)
      tags:
        - trade
      operationId: cancelMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#cancel-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/cancelMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/cancel_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/cancel_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CancelMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CancelMultipleOrders/CancelMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CancelMultipleOrdersExample.php
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
        - name: orderIdList
          in: query
          required: false
          schema:
            type: array
            example:
              - 1234567
            maxLength: 10
            items:
              type: integer
              format: int64
              example: 1234567
        - name: origClientOrderIdList
          in: query
          required: false
          schema:
            type: array
            example:
              - my_id_1
            maxLength: 10
            items:
              type: string
              example: my_id_1
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
      x-parameters-notes: "- Either `orderIdList` or `origClientOrderIdList ` must be sent."
      x-parameters-notes-cn: "- `orderIdList` 与 `origClientOrderIdList` 必须至少发送一个，不可同时发送"
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
                      x-description-cn: 用户自定义的订单号
                      description: Client Order Id.
                    cumQty:
                      type: string
                      example: "0"
                    executedQty:
                      type: string
                      example: "0"
                      x-description-cn: 成交量
                      description: Executed Qty.
                    orderId:
                      type: integer
                      example: 283194212
                      format: int64
                      x-description-cn: 系统订单号
                      description: Order Id.
                    origQty:
                      type: string
                      example: "11"
                      x-description-cn: 原始委托数量
                      description: Orig Qty.
                    price:
                      type: string
                      example: "0"
                      x-description-cn: 委托价格
                      description: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      x-description-cn: 仅减仓
                      description: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      x-description-cn: 买卖方向
                      description: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      x-description-cn: 持仓方向
                      description: Position Side.
                    status:
                      type: string
                      example: CANCELED
                      x-description-cn: 订单状态
                      description: Status.
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    timeInForce:
                      type: string
                      example: GTC
                      x-description-cn: 有效方法
                      description: Time In Force.
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 触发前订单类型
                      description: Orig Type.
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 订单类型
                      description: Type.
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
                      x-description-cn: 更新时间
                      description: Update Time.
                    workingType:
                      type: string
                      example: CONTRACT_PRICE
                      x-description-cn: 条件价格触发类型
                      description: Working Type.
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
                      example: 0
                      format: int64
                      description: order pre-set auot cancel time for TIF GTD order
                      x-description-cn: 订单TIF为GTD时的自动取消时间
                    code:
                      type: integer
                      example: -2011
                      format: int64
                    msg:
                      type: string
                      example: Unknown order sent.
    put:
      summary: Modify Multiple Orders (TRADE)
      x-summary-cn: 批量修改订单 (TRADE)
      description: Modify Multiple Orders (TRADE)
      x-description-cn: 批量修改订单
      tags:
        - trade
      operationId: modifyMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#modify-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/modifyMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/modify_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/modify_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ModifyMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ModifyMultipleOrders/ModifyMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ModifyMultipleOrdersExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        5 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
        5 on IP rate limit(x-mbx-used-weight-1m);
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
        - Parameter rules are same with `Modify Order`
        - Batch modify orders are processed concurrently, and the order of matching is not guaranteed.
        - The order of returned contents for batch modify orders is the same as the order of the order list.
        - One order can only be modfied for less than 10000 times
      x-parameters-notes-cn: |-
        - 具体订单条件规则,与普通修改订单一致
        - 批量修改订单采取并发处理,不保证订单撮合顺序
        - 批量修改订单的返回内容顺序,与订单列表顺序一致
        - 同一订单修改次数最多10000次
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
                  example: []
                  items:
                    type: object
                    properties:
                      orderId:
                        type: integer
                        format: int64
                        example: 20072994037
                      origClientOrderId:
                        type: string
                        example: LJ9R4QZDihCaS8UAOOLpgW
                      symbol:
                        type: string
                        example: BTCUSDT
                      side:
                        type: string
                        example: BUY
                        enum:
                          - BUY
                          - SELL
                      quantity:
                        type: number
                        format: float
                        example: "1"
                        description: Order quantity, cannot be sent with closePosition=true
                        x-description-cn: 委托数量, 不能与 closePosition=true 同时传入
                      price:
                        type: number
                        format: float
                        example: 30005
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
                        description: Only avaliable for LIMIT/STOP/TAKE_PROFIT order; Cannot be sent together with `price`.
                        x-description-cn: 仅适用于LIMIT/STOP/TAKE_PROFIT订单; 不能与 `price` 同时传入.
                      stopPrice:
                        type: number
                        format: float
                        example: 0
                        description: stop price, only STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET need
                        x-description-cn: 止损价, 仅 STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET 订单需要
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
                        format: int64
                        example: 5000
                        maximum: 60000
                        description: Validity window in milliseconds.
                        x-description-cn: 请求有效时间窗口（毫秒）。
                      timestamp:
                        type: integer
                        format: int64
                        example: 1770736694138
                        description: Unix timestamp in milliseconds.
                        x-description-cn: Unix 时间戳（毫秒）。
                  description: order list. Max 5 orders
                  x-description-cn: 订单列表,最多支持5个订单
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
                    symbol:
                      type: string
                      example: BTCUSDT
                    pair:
                      type: string
                      example: BTCUSDT
                    status:
                      type: string
                      example: NEW
                    clientOrderId:
                      type: string
                      example: LJ9R4QZDihCaS8UAOOLpgW
                    modifyId:
                      type: integer
                      example: 1
                      format: int64
                      description: user-defined modification identifier, only returned if provided in the request
                      x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                    price:
                      type: string
                      example: "30005"
                    origQty:
                      type: string
                      example: "1"
                    executedQty:
                      type: string
                      example: "0"
                    cumQty:
                      type: string
                      example: "0"
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
                      example: LONG
                    stopPrice:
                      type: string
                      example: "0"
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
                      description: price match mode
                      x-description-cn: 盘口价格下单模式
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading preventation mode
                      x-description-cn: 订单自成交保护模式
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
                      description: order pre-set auot cancel time for TIF GTD order
                      x-description-cn: 订单TIF为GTD时的自动取消时间
                    updateTime:
                      type: integer
                      example: 1629182711600
                      format: int64
                    code:
                      type: integer
                      example: -2022
                      format: int64
                    msg:
                      type: string
                      example: ReduceOnly Order is rejected.
    post:
      summary: Place Multiple Orders (TRADE)
      x-summary-cn: 批量下单 (TRADE)
      description: Place Multiple Orders
      x-description-cn: 批量下单
      tags:
        - trade
      operationId: placeMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#place-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/placeMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/place_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/place_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/PlaceMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/PlaceMultipleOrders/PlaceMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/PlaceMultipleOrdersExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        5 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
        5 on IP rate limit(x-mbx-used-weight-1m);
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
        - Paremeter rules are same with `New Order`
        - Batch orders are processed concurrently, and the order of matching is not guaranteed.
        - The order of returned contents for batch orders is the same as the order of the order list.
      x-parameters-notes-cn: |-
        - 具体订单条件规则，与普通下单一致
        - 批量下单采取并发处理，不保证订单撮合顺序
        - 批量下单的返回内容顺序，与订单列表顺序一致
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
                  example: []
                  items:
                    type: object
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
                      positionSide:
                        type: string
                        example: BOTH
                        enum:
                          - BOTH
                          - LONG
                          - SHORT
                        description: Default `BOTH` for One-way Mode; `LONG` or `SHORT` for Hedge Mode.
                        x-description-cn: 持仓方向，单向持仓模式默认 `BOTH`；双向持仓模式可选 `LONG` 或 `SHORT`。
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
                      quantity:
                        type: number
                        format: float
                        example: "0.001"
                      reduceOnly:
                        type: string
                        example: "false"
                        default: "false"
                        enum:
                          - "true"
                          - "false"
                      price:
                        type: number
                        format: float
                        example: "10001"
                      newClientOrderId:
                        type: string
                        example: "1"
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
                        description: only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price
                        x-description-cn: 盘口价格下单模式，不能与 `price` 同时传入。
                      selfTradePreventionMode:
                        type: string
                        example: NONE
                        enum:
                          - NONE
                          - EXPIRE_TAKER
                          - EXPIRE_BOTH
                          - EXPIRE_MAKER
                        description: >-
                          EXPIRE_TAKER: expire taker order when STP triggers/ EXPIRE_MAKER: expire taker order when STP
                          triggers/ EXPIRE_BOTH: expire both orders when STP triggers; default NONE
                        x-description-cn: 订单自成交保护模式，默认 `NONE`。
                      goodTillDate:
                        type: integer
                        format: int64
                        example: 1693207680000
                        description: Auto-cancel time for `GTD` orders.
                        x-description-cn: "`GTD` 订单的自动取消时间。"
                  description: order list. Max 5 orders
                  x-description-cn: 订单列表，最多支持5个订单
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
                      x-description-cn: 用户自定义的订单号
                      description: Client Order Id.
                    cumQty:
                      type: string
                      example: "0"
                    executedQty:
                      type: string
                      example: "0"
                      x-description-cn: 成交量
                      description: Executed Qty.
                    orderId:
                      type: integer
                      example: 22542179
                      format: int64
                      x-description-cn: 系统订单号
                      description: Order Id.
                    origQty:
                      type: string
                      example: "10"
                      x-description-cn: 原始委托数量
                      description: Orig Qty.
                    price:
                      type: string
                      example: "0"
                      x-description-cn: 委托价格
                      description: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      x-description-cn: 仅减仓
                      description: Reduce Only.
                    side:
                      type: string
                      example: SELL
                      x-description-cn: 买卖方向
                      description: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      x-description-cn: 持仓方向
                      description: Position Side.
                    status:
                      type: string
                      example: NEW
                      x-description-cn: 订单状态
                      description: Status.
                    stopPrice:
                      type: string
                      example: "0"
                    closePosition:
                      type: boolean
                      example: false
                      x-description-cn: 是否条件全平仓
                      description: Close Position.
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    timeInForce:
                      type: string
                      example: GTC
                      x-description-cn: 有效方法
                      description: Time In Force.
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 订单类型
                      description: Type.
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 触发前订单类型
                      description: Orig Type.
                    updateTime:
                      type: integer
                      example: 1566818724722
                      format: int64
                      x-description-cn: 更新时间
                      description: Update Time.
                    workingType:
                      type: string
                      example: CONTRACT_PRICE
                      x-description-cn: 条件价格触发类型
                      description: Working Type.
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
                      example: 1693207680000
                      format: int64
                      description: order pre-set auto cancel time for TIF GTD order
                      x-description-cn: 订单TIF为GTD时的自动取消时间
                    code:
                      type: integer
                      example: -2022
                      format: int64
                    msg:
                      type: string
                      example: ReduceOnly Order is rejected.
  /fapi/v1/order:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#cancel-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/cancelOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/cancel_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/cancel_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CancelOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CancelOrder/CancelOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CancelOrderExample.php
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
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 283194212
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: myOrder1
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
                    x-description-cn: 用户自定义的订单号
                    description: Client Order Id.
                  cumQty:
                    type: string
                    example: "0"
                  executedQty:
                    type: string
                    example: "0"
                    x-description-cn: 成交量
                    description: Executed Qty.
                  orderId:
                    type: integer
                    example: 283194212
                    format: int64
                    x-description-cn: 系统订单号
                    description: Order Id.
                  origQty:
                    type: string
                    example: "11"
                    x-description-cn: 原始委托数量
                    description: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    x-description-cn: 委托价格
                    description: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    x-description-cn: 仅减仓
                    description: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    x-description-cn: 买卖方向
                    description: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    x-description-cn: 持仓方向
                    description: Position Side.
                  status:
                    type: string
                    example: CANCELED
                    x-description-cn: 订单状态
                    description: Status.
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
                  timeInForce:
                    type: string
                    example: GTC
                    x-description-cn: 有效方法
                    description: Time In Force.
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 触发前订单类型
                    description: Orig Type.
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 订单类型
                    description: Type.
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
                    x-description-cn: 更新时间
                    description: Update Time.
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    x-description-cn: 条件价格触发类型
                    description: Working Type.
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
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: 订单TIF为GTD时的自动取消时间
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#modify-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/modifyOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/modify_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/modify_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ModifyOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ModifyOrder/ModifyOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ModifyOrderExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
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
      x-parameters-notes: >-
        - Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.

        - Both `quantity` and `price` must be sent, which is different from dapi modify order endpoint.

        - When the new `quantity` or `price` doesn't satisfy PRICE_FILTER / PERCENT_FILTER / LOT_SIZE, amendment will be
        rejected and the order will stay as it is.

        - However the order will be cancelled by the amendment in the following situations:
          - when the order is in partially filled status and the new `quantity` <= `executedQty`
          - When the order is `GTX` and the new price will cause it to be executed immediately
        - One order can only be modfied for less than 10000 times

        - `reduceOnly` behavior:
          - `false` or omitted: behave as today — `min_notional` is enforced on the modified order.
          - `true` and the original order's `reduceOnly` attribute is also `true` (consistent): the `min_notional` check is skipped on the modified order, matching placement semantics.
          - `true` but the original order's `reduceOnly` attribute is `false` (inconsistent): the modify request is rejected with error code `-5047`, "The original order is not a reduce-only order".
          - `reduceOnly` is used purely for validation — passing `true` does not change the original order's `reduceOnly` attribute; that flag remains whatever it was set to at placement time.
      x-parameters-notes-cn: |-
        - `orderId` 与 `origClientOrderId` 必须至少发送一个，同时发送则以 order id为准
        - `quantity` 与 `price` 均必须发送，这点和 dapi 修改订单不同
        - 当新订单的`quantity` 或 `price`不满足PRICE_FILTER / PERCENT_FILTER / LOT_SIZE限制，修改会被拒绝，原订单依旧被保留
        - 订单会在下列情况下被取消：
          - 原订单被部分执行且新订单`quantity` <= `executedQty`
          - 原订单是`GTX`，新订单的价格会导致订单立刻执行
        - 同一订单修改次数最多10000次
        - `reduceOnly` 行为说明：
          - `false` 或不传：与当前行为一致——对修改后的订单执行 `min_notional` 校验。
          - `true` 且原订单的 `reduceOnly` 属性也为 `true`（一致）：跳过修改后订单的 `min_notional` 校验，与下单语义对齐。
          - `true` 但原订单的 `reduceOnly` 属性为 `false`（不一致）：拒绝本次改单请求，返回错误码 `-5047`，"The original order is not a reduce-only order"。
          - `reduceOnly` 仅用于校验——传 `true` 不会改变原订单的 `reduceOnly` 属性，该属性仍保持下单时设定的值。
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
                  example: 20072994037
                  format: int64
                origClientOrderId:
                  type: string
                  example: LJ9R4QZDihCaS8UAOOLpgW
                symbol:
                  type: string
                  example: BTCUSDT
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
                  x-description-cn: 下单数量,使用`closePosition`不支持此参数。
                price:
                  type: number
                  example: 30005
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
                  x-description-cn: 仅适用于`LIMIT`/`STOP`/`TAKE_PROFIT`订单; 不能与`price`参数同时传入
                modifyId:
                  type: integer
                  example: 1
                  format: int64
                  description: >-
                    User-defined modification identifier, returned as-is in the response. Optional; not validated for
                    uniqueness.
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
                  symbol:
                    type: string
                    example: BTCUSDT
                  pair:
                    type: string
                    example: BTCUSDT
                  status:
                    type: string
                    example: NEW
                  clientOrderId:
                    type: string
                    example: LJ9R4QZDihCaS8UAOOLpgW
                  modifyId:
                    type: integer
                    example: 1
                    format: int64
                    description: user-defined modification identifier, only returned if provided in the request
                    x-description-cn: 用户自定义的改单标识，仅当请求中传入时返回
                  price:
                    type: string
                    example: "30005"
                  origQty:
                    type: string
                    example: "1"
                  executedQty:
                    type: string
                    example: "0"
                  cumQty:
                    type: string
                    example: "0"
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
                    example: LONG
                  stopPrice:
                    type: string
                    example: "0"
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
                    description: price match mode
                    x-description-cn: 盘口价格下单模式
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading preventation mode
                    x-description-cn: 订单自成交保护模式
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: 订单TIF为GTD时的自动取消时间
                  updateTime:
                    type: integer
                    example: 1629182711600
                    format: int64
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#new-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/newOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/new_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/new_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/NewOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/NewOrder/NewOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/NewOrderExample.php
      x-security-type: TRADE
      x-signed: true
      x-weight: |-
        1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
        1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
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
      x-parameters-notes: >-
        Additional mandatory parameters based on `type`:


        | Type | Additional mandatory parameters |

        |------|----------------------------------|

        | `LIMIT` | `timeInForce`, `quantity`, `price` |

        | `MARKET` | `quantity` |


        - If `newOrderRespType` is sent as `RESULT`:
          - `MARKET` order: the final FILLED result of the order will be returned directly.
          - `LIMIT` order with special `timeInForce`: the final status result of the order (FILLED or EXPIRED) will be returned directly.
        - `selfTradePreventionMode` is only effective when `timeInForce` is set to `IOC`, `GTC`, or `GTD`.

        - In extreme market conditions, `timeInForce` `GTD` order auto-cancel time might be delayed compared to
        `goodTillDate`.
      x-parameters-notes-cn: |-
        根据 order `type`的不同，某些参数强制要求，具体如下:

        | Type                                | 强制要求的参数                     |
        | ----------------------------------- | ---------------------------------- |
        | `LIMIT`                             | `timeInForce`, `quantity`, `price` |
        | `MARKET`                            | `quantity`                         |

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
                side:
                  type: string
                  example: BUY
                  enum:
                    - BUY
                    - SELL
                positionSide:
                  type: string
                  example: BOTH
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
                type:
                  type: string
                  example: LIMIT
                  description: Order type
                  x-description-cn: 订单类型 `LIMIT`, `MARKET`
                  enum:
                    - LIMIT
                    - MARKET
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
                    - GTD
                    - RPI
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: Cannot be sent in Hedge Mode
                  x-description-cn: 双开模式下不接受此参数
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                price:
                  type: number
                  example: "1.0"
                  format: float
                newClientOrderId:
                  type: string
                  example: "1"
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Can only be string following the
                    rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                  x-description-cn: 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`
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
                  description: only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`
                  x-description-cn: 仅对`LIMIT`/`STOP`/`TAKE_PROFIT`订单有效；不能与`price`参数同时传入
                selfTradePreventionMode:
                  type: string
                  example: EXPIRE_TAKER
                  enum:
                    - EXPIRE_TAKER
                    - EXPIRE_BOTH
                    - EXPIRE_MAKER
                  description: >-
                    `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP
                    triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `EXPIRE_MAKER`
                  x-description-cn: "`EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`； 默认`EXPIRE_MAKER`"
                goodTillDate:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                    timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp
                    must be greater than the current time plus 600 seconds and smaller than 253402300799000
                  x-description-cn: >-
                    TIF为GTD时订单的自动取消时间，
                    当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000
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
                    x-description-cn: 用户自定义的订单号
                    description: Client Order Id.
                  cumQty:
                    type: string
                    example: "0"
                  executedQty:
                    type: string
                    example: "0"
                    x-description-cn: 成交量
                    description: Executed Qty.
                  orderId:
                    type: integer
                    example: 22542179
                    format: int64
                    x-description-cn: 系统订单号
                    description: Order Id.
                  origQty:
                    type: string
                    example: "10"
                    x-description-cn: 原始委托数量
                    description: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    x-description-cn: 委托价格
                    description: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    x-description-cn: 仅减仓
                    description: Reduce Only.
                  side:
                    type: string
                    example: SELL
                    x-description-cn: 买卖方向
                    description: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    x-description-cn: 持仓方向
                    description: Position Side.
                  status:
                    type: string
                    example: NEW
                    x-description-cn: 订单状态
                    description: Status.
                  stopPrice:
                    type: string
                    example: "0"
                    description: ignored for LIMIT / MARKET orders
                    x-description-cn: 触发价，`LIMIT`/`MARKET` 订单忽略此字段
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
                  timeInForce:
                    type: string
                    example: GTD
                    x-description-cn: 有效方法
                    description: Time In Force.
                  type:
                    type: string
                    example: LIMIT
                    x-description-cn: 订单类型
                    description: Type.
                  origType:
                    type: string
                    example: LIMIT
                    x-description-cn: 触发前订单类型
                    description: Orig Type.
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    x-description-cn: 更新时间
                    description: Update Time.
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    x-description-cn: 条件价格触发类型
                    description: Working Type.
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
                    example: 1693207680000
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: 订单TIF为GTD时的自动取消时间
    get:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#query-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/queryOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/query_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/query_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/QueryOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/QueryOrder/QueryOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/QueryOrderExample.php
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
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1917641
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: abc
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
        - `orderId` is self-increment for each specific `symbol`
      x-parameters-notes-cn: |-
        - 至少需要发送 `orderId` 与 `origClientOrderId`中的一个
        - `orderId`在`symbol`维度是自增的
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
                    example: "0.00000"
                    x-description-cn: 平均成交价
                    description: Avg Price.
                  clientOrderId:
                    type: string
                    example: abc
                    x-description-cn: 用户自定义的订单号
                    description: Client Order Id.
                  cumQuote:
                    type: string
                    example: "0"
                    x-description-cn: 成交金额
                    description: Cum Quote.
                  executedQty:
                    type: string
                    example: "0"
                    x-description-cn: 成交量
                    description: Executed Qty.
                  orderId:
                    type: integer
                    example: 1573346959
                    format: int64
                    x-description-cn: 系统订单号
                    description: Order Id.
                  origQty:
                    type: string
                    example: "0.40"
                    x-description-cn: 原始委托数量
                    description: Orig Qty.
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 触发前订单类型
                    description: Orig Type.
                  price:
                    type: string
                    example: "0"
                    x-description-cn: 委托价格
                    description: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    x-description-cn: 是否仅减仓
                    description: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    x-description-cn: 买卖方向
                    description: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    x-description-cn: 持仓方向
                    description: Position Side.
                  status:
                    type: string
                    example: NEW
                    x-description-cn: 订单状态
                    description: Status.
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: order time
                    x-description-cn: 订单时间
                  timeInForce:
                    type: string
                    example: GTC
                    x-description-cn: 有效方法
                    description: Time In Force.
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 订单类型
                    description: Type.
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
                    x-description-cn: 条件价格触发类型
                    description: Working Type.
                  priceProtect:
                    type: boolean
                    example: false
                    description: if conditional order trigger is protected
                    x-description-cn: 是否开启条件单触发保护
                  priceMatch:
                    type: string
                    example: NONE
                    x-description-cn: 盘口价格下单模式
                    description: Price Match.
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    x-description-cn: 订单自成交保护模式
                    description: Self Trade Prevention Mode.
                  goodTillDate:
                    type: integer
                    example: 0
                    format: int64
                    x-description-cn: 订单TIF为GTD时的自动取消时间
                    description: Good Till Date.
  /fapi/v1/leverage:
    post:
      summary: Change Initial Leverage (TRADE)
      x-summary-cn: 调整开仓杠杆 (TRADE)
      description: Change user's initial leverage of specific symbol market.
      x-description-cn: 调整用户在指定symbol合约的开仓杠杆。
      tags:
        - trade
      operationId: changeInitialLeverage
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#change-initial-leverage
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/changeInitialLeverage.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/change_initial_leverage.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/change_initial_leverage.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ChangeInitialLeverageExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ChangeInitialLeverage/ChangeInitialLeverage.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ChangeInitialLeverageExample.php
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
                  example: 1
                  format: int64
                  minimum: 1
                  description: >-
                    Target initial leverage. The maximum is symbol-specific: use `initialLeverage` of bracket 1 from
                    `GET /fapi/v1/leverageBracket`.
                  x-description-cn: 目标杠杆倍数。最大值因交易对而异，以 `GET /fapi/v1/leverageBracket` 返回的第 1 档 `initialLeverage` 为准。
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
                    x-description-cn: 杠杆倍数
                    description: Leverage.
                  maxNotionalValue:
                    type: string
                    example: "1000000"
                    x-description-cn: 当前杠杆倍数下允许的最大名义价值
                    description: Max Notional Value.
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
  /fapi/v1/marginType:
    post:
      summary: Change Margin Type (TRADE)
      x-summary-cn: 变换逐全仓模式 (TRADE)
      description: Change symbol level margin type
      x-description-cn: 变换用户在指定symbol合约上的保证金模式：逐仓或全仓。
      tags:
        - trade
      operationId: changeMarginType
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#change-margin-type
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/changeMarginType.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/change_margin_type.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/change_margin_type.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ChangeMarginTypeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ChangeMarginType/ChangeMarginType.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ChangeMarginTypeExample.php
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
                  example: BTCUSDT
                marginType:
                  type: string
                  example: ISOLATED
                  enum:
                    - ISOLATED
                    - CROSSED
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
                  msg:
                    type: string
                    example: success
  /fapi/v1/openAlgoOrders:
    get:
      summary: Current All Algo Open Orders (USER_DATA)
      x-summary-cn: 查看当前全部条件挂单 (USER_DATA)
      description: >-
        Get all open algo (conditional) orders on a symbol, including TP/SL (Take Profit / Stop Loss) and trailing stop
        orders on USD-M Futures.
      x-description-cn: >-
        查看某个交易对下当前所有的条件挂单（Algo / Conditional Order），包括 U 本位合约的止盈止损（TP/SL, Take Profit / Stop Loss）与追踪止损（Trailing
        Stop）订单。
      tags:
        - trade
      operationId: currentAllAlgoOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#current-all-algo-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/currentAllAlgoOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/current_all_algo_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/current_all_algo_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CurrentAllAlgoOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CurrentAllAlgoOpenOrders/CurrentAllAlgoOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CurrentAllAlgoOpenOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        **1** for a single symbol; **40** when the symbol parameter is omitted

        **Careful** when accessing this with no symbol.
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
            example: BTCUSDT
        - name: algoId
          in: query
          required: false
          schema:
            type: integer
            example: 2148627
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
      x-parameters-notes: "- If the symbol is not sent, orders for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 不带symbol参数，会返回所有交易对的挂单"
      responses:
        "200":
          description: Current All Algo Open Orders
          x-description-cn: 当前 All Algo 未完成订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    algoId:
                      type: integer
                      example: 2148627
                      format: int64
                    clientAlgoId:
                      type: string
                      example: MRumok0dkhrP4kCm12AHaB
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
                    icebergQuantity:
                      type: string
                      example: "null"
                      description: Reserved field, ignore.
                      x-description-cn: 预留字段，请忽略。
                    tpTriggerPrice:
                      type: string
                      example: "0.000"
                    tpPrice:
                      type: string
                      example: "0.000"
                    slTriggerPrice:
                      type: string
                      example: "0.000"
                    slPrice:
                      type: string
                      example: "0.000"
                    tpOrderType:
                      type: string
                      example: ""
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
                      example: 1750514941540
                      format: int64
                    updateTime:
                      type: integer
                      example: 1750514941540
                      format: int64
                    triggerTime:
                      type: integer
                      example: 0
                      format: int64
                    goodTillDate:
                      type: integer
                      example: 0
                      format: int64
  /fapi/v1/openOrders:
    get:
      summary: Current All Open Orders (USER_DATA)
      x-summary-cn: 查看当前全部挂单 (USER_DATA)
      description: Get all open orders on a symbol.
      x-description-cn: 查看当前全部挂单
      tags:
        - trade
      operationId: currentAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#current-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/currentAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/current_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/current_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/CurrentAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/CurrentAllOpenOrders/CurrentAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/CurrentAllOpenOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: |-
        **1** for a single symbol; **40** when the symbol parameter is omitted

        **Careful** when accessing this with no symbol.
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
      x-parameters-notes: "- If the symbol is not sent, orders for all symbols will be returned in an array."
      x-parameters-notes-cn: "- 不带symbol参数，会返回所有交易对的挂单"
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
                      example: "0.00000"
                      x-description-cn: 平均成交价
                      description: Avg Price.
                    clientOrderId:
                      type: string
                      example: abc
                      x-description-cn: 用户自定义的订单号
                      description: Client Order Id.
                    cumQuote:
                      type: string
                      example: "0"
                      x-description-cn: 成交金额
                      description: Cum Quote.
                    executedQty:
                      type: string
                      example: "0"
                      x-description-cn: 成交量
                      description: Executed Qty.
                    orderId:
                      type: integer
                      example: 1917641
                      format: int64
                      x-description-cn: 系统订单号
                      description: Order Id.
                    origQty:
                      type: string
                      example: "0.40"
                      x-description-cn: 原始委托数量
                      description: Orig Qty.
                    origType:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 触发前订单类型
                      description: Orig Type.
                    price:
                      type: string
                      example: "0"
                      x-description-cn: 委托价格
                      description: Price.
                    reduceOnly:
                      type: boolean
                      example: false
                      x-description-cn: 是否仅减仓
                      description: Reduce Only.
                    side:
                      type: string
                      example: BUY
                      x-description-cn: 买卖方向
                      description: Side.
                    positionSide:
                      type: string
                      example: SHORT
                      x-description-cn: 持仓方向
                      description: Position Side.
                    status:
                      type: string
                      example: NEW
                      x-description-cn: 订单状态
                      description: Status.
                    stopPrice:
                      type: string
                      example: "9300"
                      description: please ignore when order type is TRAILING_STOP_MARKET
                      x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                    closePosition:
                      type: boolean
                      example: false
                      description: if Close-All
                      x-description-cn: 是否条件全平仓
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    time:
                      type: integer
                      example: 1579276756075
                      format: int64
                      description: order time
                      x-description-cn: 订单时间
                    timeInForce:
                      type: string
                      example: GTC
                      x-description-cn: 有效方法
                      description: Time In Force.
                    type:
                      type: string
                      example: TRAILING_STOP_MARKET
                      x-description-cn: 订单类型
                      description: Type.
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
                      x-description-cn: 条件价格触发类型
                      description: Working Type.
                    priceProtect:
                      type: boolean
                      example: false
                      description: if conditional order trigger is protected
                      x-description-cn: 是否开启条件单触发保护
                    priceMatch:
                      type: string
                      example: NONE
                      description: price match mode
                      x-description-cn: price match mode
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
  /fapi/v1/stock/contract:
    post:
      summary: Futures TradFi Perps Contract (USER_DATA)
      x-summary-cn: 传统金融合约协议 (USER_DATA)
      description: Sign TradFi-Perps agreement contract
      x-description-cn: 签署 TradFi-Perps 协议合约
      tags:
        - trade
      operationId: futuresTradfiPerpsContract
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#futures-tradfi-perps-contract
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/futuresTradfiPerpsContract.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/futures_tradfi_perps_contract.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/futures_tradfi_perps_contract.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/FuturesTradfiPerpsContractExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/FuturesTradfiPerpsContract/FuturesTradfiPerpsContract.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/FuturesTradfiPerpsContractExample.php
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
                  description: |-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Futures TradFi Perps Contract
          x-description-cn: 合约 Trad Fi Perps Contract
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                  msg:
                    type: string
                    example: success
  /fapi/v1/orderAmendment:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#get-order-modify-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/getOrderModifyHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/get_order_modify_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/get_order_modify_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/GetOrderModifyHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/GetOrderModifyHistory/GetOrderModifyHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/GetOrderModifyHistoryExample.php
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
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 20072994037
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: LJ9R4QZDihCaS8UAOOLpgW
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
            example: 50
            format: int64
            default: 50
            maximum: 100
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
        - Either `orderId` or `origClientOrderId` must be sent, and the
        `orderId` will prevail if both are sent.

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
                      example: BTCUSDT
                    pair:
                      type: string
                      example: BTCUSDT
                    orderId:
                      type: integer
                      example: 20072994037
                      format: int64
                    clientOrderId:
                      type: string
                      example: LJ9R4QZDihCaS8UAOOLpgW
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
                            after:
                              type: string
                              example: "30003.2"
                        origQty:
                          type: object
                          properties:
                            before:
                              type: string
                              example: "1"
                            after:
                              type: string
                              example: "1"
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
  /fapi/v1/positionMargin/history:
    get:
      summary: Get Position Margin Change History (TRADE)
      x-summary-cn: 逐仓保证金变动历史 (TRADE)
      description: Get Position Margin Change History
      x-description-cn: 查询逐仓保证金变动历史
      tags:
        - trade
      operationId: getPositionMarginChangeHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#get-position-margin-change-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/getPositionMarginChangeHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/get_position_margin_change_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/get_position_margin_change_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/GetPositionMarginChangeHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/GetPositionMarginChangeHistory/GetPositionMarginChangeHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/GetPositionMarginChangeHistoryExample.php
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
        - name: type
          in: query
          required: false
          schema:
            type: string
            example: 1
          description: "1: Add position margin，2: Reduce position margin"
          x-description-cn: "调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金"
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
            default: current
          description: time if not pass
          x-description-cn: 结束时间，默认为当前时间
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 50
            format: int64
            default: 500
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
        - Support querying future histories that are not older than 30 days
        - The time between `startTime` and `endTime`can't be more than 30 days
      x-parameters-notes-cn: |-
        - `startTime`与`endTime`间隔不能超过30天
        - 支持查询不超过1个月的合约数据
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
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    type:
                      type: integer
                      example: 1
                      format: int64
                      x-description-cn: 调整方向
                      description: Type.
                    deltaType:
                      type: string
                      example: USER_ADJUST
                      x-description-cn: 划转类型
                      description: Delta Type.
                    amount:
                      type: string
                      example: "23.36332311"
                      x-description-cn: 数量
                      description: Amount.
                    asset:
                      type: string
                      example: USDT
                      x-description-cn: 资产
                      description: Asset.
                    time:
                      type: integer
                      example: 1578047897183
                      format: int64
                      x-description-cn: 时间
                      description: Time.
                    positionSide:
                      type: string
                      example: BOTH
                      x-description-cn: 持仓方向
                      description: Position Side.
  /fapi/v1/positionMargin:
    post:
      summary: Modify Isolated Position Margin (TRADE)
      x-summary-cn: 调整逐仓保证金 (TRADE)
      description: Modify Isolated Position Margin
      x-description-cn: 针对逐仓模式下的仓位，调整其逐仓保证金资金。
      tags:
        - trade
      operationId: modifyIsolatedPositionMargin
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#modify-isolated-position-margin
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/modifyIsolatedPositionMargin.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/modify_isolated_position_margin.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/modify_isolated_position_margin.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/ModifyIsolatedPositionMarginExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/ModifyIsolatedPositionMargin/ModifyIsolatedPositionMargin.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/ModifyIsolatedPositionMarginExample.php
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
      x-parameters-notes-cn: "- 只针对逐仓symbol 与 positionSide(如有)"
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
                positionSide:
                  type: string
                  example: BOTH
                  description: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode.
                  x-description-cn: 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`
                amount:
                  type: number
                  example: "1.0"
                  format: float
                  description: Margin asset
                  x-description-cn: 保证金资金
                type:
                  type: integer
                  example: 1
                  description: "1: Add position margin，2: Reduce position margin"
                  x-description-cn: "调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金"
                recvWindow:
                  type: integer
                  example: 5000
                  maximum: 60000
                  format: int64
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
                  code:
                    type: integer
                    example: 200
                    format: int64
                  msg:
                    type: string
                    example: Successfully modify position margin.
                  type:
                    type: integer
                    example: 1
                    format: int64
  /fapi/v1/adlQuantile:
    get:
      summary: Position ADL Quantile Estimation (USER_DATA)
      x-summary-cn: 持仓ADL队列估算 (USER_DATA)
      description: >-
        Position ADL Quantile Estimation


        * Values update every 30s.

        * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.

        * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and
        "BOTH" will be returned to show the positions' adl quantiles of different position sides.

        * If the positions of the symbol are crossed margined in Hedge Mode:
          * "HEDGE" as a sign will be returned instead of "BOTH";
          * A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
      x-description-cn: |-
        持仓ADL队列估算

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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#position-adl-quantile-estimation
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/positionAdlQuantileEstimation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/position_adl_quantile_estimation.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/position_adl_quantile_estimation.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/PositionAdlQuantileEstimationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/PositionAdlQuantileEstimation/PositionAdlQuantileEstimation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/PositionAdlQuantileEstimationExample.php
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
                      example: ETHUSDT
                    adlQuantile:
                      type: object
                      example: {}
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
  /fapi/v2/positionRisk:
    get:
      summary: Position Information V2 (USER_DATA)
      x-summary-cn: 用户持仓风险V2 (USER_DATA)
      description: Get current position information.
      x-description-cn: 查询持仓风险
      tags:
        - trade
      operationId: positionInformationV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#position-information-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/positionInformationV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/position_information_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/position_information_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/PositionInformationV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/PositionInformationV2/PositionInformationV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/PositionInformationV2Example.php
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
      x-parameters-notes: "- Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs."
      x-parameters-notes-cn: "- 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。"
      responses:
        "200":
          description: Position Information V2
          x-description-cn: 持仓 信息 V2
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
                      x-description-cn: 开仓均价
                      description: Entry Price.
                    breakEvenPrice:
                      type: string
                      example: "0.0"
                      x-description-cn: 盈亏平衡价
                      description: Break Even Price.
                    marginType:
                      type: string
                      example: isolated
                      x-description-cn: 逐仓模式或全仓模式
                      description: Margin Type.
                    isAutoAddMargin:
                      type: string
                      example: "false"
                    isolatedMargin:
                      type: string
                      example: "0.00000000"
                      x-description-cn: 逐仓保证金
                      description: Isolated Margin.
                    leverage:
                      type: string
                      example: "10"
                      x-description-cn: 当前杠杆倍数
                      description: Leverage.
                    liquidationPrice:
                      type: string
                      example: "0"
                      x-description-cn: 参考强平价格
                      description: Liquidation Price.
                    markPrice:
                      type: string
                      example: "6679.50671178"
                      x-description-cn: 当前标记价格
                      description: Mark Price.
                    maxNotionalValue:
                      type: string
                      example: "20000000"
                      x-description-cn: 当前杠杆倍数允许的名义价值上限
                      description: Max Notional Value.
                    positionAmt:
                      type: string
                      example: "0.000"
                      x-description-cn: 头寸数量，符号代表多空方向, 正数为多，负数为空
                      description: Position Amt.
                    notional:
                      type: string
                      example: "0"
                    isolatedWallet:
                      type: string
                      example: "0"
                    symbol:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 交易对
                      description: Symbol.
                    unRealizedProfit:
                      type: string
                      example: "0.00000000"
                      x-description-cn: 持仓未实现盈亏
                      description: Un Realized Profit.
                    positionSide:
                      type: string
                      example: BOTH
                      x-description-cn: 持仓方向
                      description: Position Side.
                    updateTime:
                      type: integer
                      example: 1625474304765
                      format: int64
                      x-description-cn: 更新时间
                      description: Update Time.
  /fapi/v3/positionRisk:
    get:
      summary: Position Information V3 (USER_DATA)
      x-summary-cn: 用户持仓风险V3 (USER_DATA)
      description: |-
        Get current position information(only symbol that has position or open
        orders will be returned).
      x-description-cn: 查询持仓风险，仅返回有持仓或挂单的交易对
      tags:
        - trade
      operationId: positionInformationV3
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#position-information-v3
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/positionInformationV3.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/position_information_v3.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/position_information_v3.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/PositionInformationV3Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/PositionInformationV3/PositionInformationV3.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/PositionInformationV3Example.php
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
      x-parameters-notes: "- Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs."
      x-parameters-notes-cn: "- 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。"
      responses:
        "200":
          description: Position Information V3
          x-description-cn: 持仓 信息 V3
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: ADAUSDT
                      description: symbol
                      x-description-cn: 交易对
                    positionSide:
                      type: string
                      example: BOTH
                      description: position side
                      x-description-cn: 持仓方向
                    positionAmt:
                      type: string
                      example: "30"
                      description: position amount, positive for long, negative for short
                      x-description-cn: 头寸数量，符号代表多空方向, 正数为多，负数为空
                    entryPrice:
                      type: string
                      example: "0.385"
                      description: entry price
                      x-description-cn: 开仓均价
                    breakEvenPrice:
                      type: string
                      example: "0.385077"
                      description: break-even price
                      x-description-cn: 盈亏平衡价
                    markPrice:
                      type: string
                      example: "0.41047590"
                      description: current mark price
                      x-description-cn: 当前标记价格
                    unRealizedProfit:
                      type: string
                      example: "0.76427700"
                      description: unrealized profit
                      x-description-cn: 持仓未实现盈亏
                    liquidationPrice:
                      type: string
                      example: "0"
                      description: liquidation price
                      x-description-cn: 参考强平价格
                    isolatedMargin:
                      type: string
                      example: "0"
                      description: isolated margin
                      x-description-cn: 逐仓保证金
                    notional:
                      type: string
                      example: "12.31427700"
                      description: notional value of position
                      x-description-cn: 名义价值
                    marginAsset:
                      type: string
                      example: USDT
                      description: margin asset
                      x-description-cn: 保证金资产
                    isolatedWallet:
                      type: string
                      example: "0"
                      description: isolated wallet (if isolated position)
                      x-description-cn: 逐仓钱包余额
                    initialMargin:
                      type: string
                      example: "0.61571385"
                      description: initial margin required with current mark price
                      x-description-cn: 初始保证金
                    maintMargin:
                      type: string
                      example: "0.08004280"
                      description: maintenance margin required
                      x-description-cn: 维持保证金
                    positionInitialMargin:
                      type: string
                      example: "0.61571385"
                      description: initial margin required for positions with current mark price
                      x-description-cn: 仓位初始保证金
                    openOrderInitialMargin:
                      type: string
                      example: "0"
                      description: initial margin required for open orders with current mark price
                      x-description-cn: 订单初始保证金
                    adl:
                      type: integer
                      example: 2
                      format: int64
                      description: auto-deleverage ranking
                      x-description-cn: 自动减仓等级
                    bidNotional:
                      type: string
                      example: "0"
                      description: ignore
                      x-description-cn: 忽略
                    askNotional:
                      type: string
                      example: "0"
                      description: ignore
                      x-description-cn: 忽略
                    updateTime:
                      type: integer
                      example: 1720736417660
                      format: int64
                      description: update time
                      x-description-cn: 更新时间
  /fapi/v1/allAlgoOrders:
    get:
      summary: Query All Algo Orders (USER_DATA)
      x-summary-cn: 查询所有条件订单(包括历史订单) (USER_DATA)
      description: >-
        Get all algo (conditional) orders — active, CANCELED, TRIGGERED, or FINISHED — including TP/SL (Take Profit /
        Stop Loss) and trailing stop orders on USD-M Futures.


        * These orders will not be found:
          * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
          * order create time + 90 days < current time
      x-description-cn: >-
        查询所有条件订单（Algo / Conditional Order），包括活跃、已撤销、已触发与已完成订单，覆盖 U 本位合约的止盈止损（TP/SL, Take Profit / Stop
        Loss）与追踪止损（Trailing Stop）。


        * 请注意，如果订单满足如下条件，不会被查询到：
          * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
          * 订单创建时间 + 90天 < 当前时间
      tags:
        - trade
      operationId: queryAllAlgoOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#query-all-algo-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/queryAllAlgoOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/query_all_algo_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/query_all_algo_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/QueryAllAlgoOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/QueryAllAlgoOrders/QueryAllAlgoOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/QueryAllAlgoOrdersExample.php
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
        - name: algoId
          in: query
          required: false
          schema:
            type: integer
            example: 2146760
            format: int64
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
            example: 50
            format: int64
            default: 500
            maximum: 1000
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
        - If `algoId` is set, it will get orders >= that `algoId`. Otherwise most recent orders are returned.
        - The query time period must be less then 7 days( default as the recent 7 days).
      x-parameters-notes-cn: |-
        - 查询时间范围最大不得超过7天
        - 默认查询最近7天内的数据
      responses:
        "200":
          description: All Algo Orders
          x-description-cn: All Algo 订单
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
                    icebergQuantity:
                      type: string
                      example: "null"
                      description: Reserved field, ignore.
                      x-description-cn: 预留字段，请忽略。
                    tpTriggerPrice:
                      type: string
                      example: "0.000"
                    tpPrice:
                      type: string
                      example: "0.000"
                    slTriggerPrice:
                      type: string
                      example: "0.000"
                    slPrice:
                      type: string
                      example: "0.000"
                    tpOrderType:
                      type: string
                      example: ""
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
  /fapi/v1/openOrder:
    get:
      summary: Query Current Open Order (USER_DATA)
      x-summary-cn: 查询当前挂单 (USER_DATA)
      description: Query open order
      x-description-cn: 请小心使用不带symbol参数的调用
      tags:
        - trade
      operationId: queryCurrentOpenOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#query-current-open-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/queryCurrentOpenOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/query_current_open_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/query_current_open_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/QueryCurrentOpenOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/QueryCurrentOpenOrder/QueryCurrentOpenOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/QueryCurrentOpenOrderExample.php
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
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 1917641
            format: int64
        - name: origClientOrderId
          in: query
          required: false
          schema:
            type: string
            example: abc
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
        - Either`orderId` or `origClientOrderId` must be sent
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
      x-parameters-notes-cn: |-
        - `orderId` 与 `origClientOrderId` 中的一个为必填参数
        - 查询的订单如果已经成交或取消，将返回报错 "Order does not exist."
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
                    example: "0.00000"
                    x-description-cn: 平均成交价
                    description: Avg Price.
                  clientOrderId:
                    type: string
                    example: abc
                    x-description-cn: 用户自定义的订单号
                    description: Client Order Id.
                  cumQuote:
                    type: string
                    example: "0"
                    x-description-cn: 成交金额
                    description: Cum Quote.
                  executedQty:
                    type: string
                    example: "0"
                    x-description-cn: 成交量
                    description: Executed Qty.
                  orderId:
                    type: integer
                    example: 1917641
                    format: int64
                    x-description-cn: 系统订单号
                    description: Order Id.
                  origQty:
                    type: string
                    example: "0.40"
                    x-description-cn: 原始委托数量
                    description: Orig Qty.
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 触发前订单类型
                    description: Orig Type.
                  price:
                    type: string
                    example: "0"
                    x-description-cn: 委托价格
                    description: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    x-description-cn: 是否仅减仓
                    description: Reduce Only.
                  side:
                    type: string
                    example: BUY
                    x-description-cn: 买卖方向
                    description: Side.
                  status:
                    type: string
                    example: NEW
                    x-description-cn: 订单状态
                    description: Status.
                  positionSide:
                    type: string
                    example: SHORT
                    x-description-cn: 持仓方向
                    description: Position Side.
                  stopPrice:
                    type: string
                    example: "9300"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
                  time:
                    type: integer
                    example: 1579276756075
                    format: int64
                    description: order time
                    x-description-cn: 订单时间
                  timeInForce:
                    type: string
                    example: GTC
                    x-description-cn: 有效方法
                    description: Time In Force.
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 订单类型
                    description: Type.
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
                    x-description-cn: 更新时间
                    description: Update Time.
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    x-description-cn: 条件价格触发类型
                    description: Working Type.
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
                    example: 0
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: 订单TIF为GTD时的自动取消时间
  /fapi/v1/order/test:
    post:
      summary: Test Order (TRADE)
      x-summary-cn: 下单测试 (TRADE)
      description: Testing order request, this order will not be submitted to matching engine
      x-description-cn: 用于测试订单请求，但不会提交到撮合引擎
      tags:
        - trade
      operationId: testOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#test-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/testOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/test_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/test_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/TestOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/TestOrder/TestOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/TestOrderExample.php
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
        Additional mandatory parameters based on `type`:


        | Type                             | Additional mandatory parameters    |

        | -------------------------------- | ---------------------------------- |

        | `LIMIT`                          | `timeInForce`, `quantity`, `price` |

        | `MARKET`                         | `quantity`                         |

        | `STOP/TAKE_PROFIT`               | `quantity`,  `price`, `stopPrice`  |

        | `STOP_MARKET/TAKE_PROFIT_MARKET` | `stopPrice`                        |

        | `TRAILING_STOP_MARKET`           | `callbackRate`                     |


        - Order with type `STOP`, parameter `timeInForce` can be sent ( default `GTC`).

        - Order with type `TAKE_PROFIT`, parameter `timeInForce` can be sent (default `GTC`).

        - Condition orders will be triggered when:
          - If parameter`priceProtect`is sent as true:
            - when price reaches the `stopPrice` ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
            - "triggerProtect" of a symbol can be got from `GET /fapi/v1/exchangeInfo`
          - `STOP`, `STOP_MARKET`:
            - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
            - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`:
            - BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
            - SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
          - `TRAILING_STOP_MARKET`:
            - BUY: the lowest price after order placed <= `activationPrice`, and the latest price >= the lowest price * (1 + `callbackRate`)
            - SELL: the highest price after order placed >= `activationPrice`, and the latest price <= the highest price * (1 - `callbackRate`)
        - For `TRAILING_STOP_MARKET`, if you got such error code. > `{"code": -2021, "msg": "Order would immediately
        trigger."}` > means that the parameters you send do not meet the following requirements:
          - BUY: `activationPrice` should be smaller than latest price.
          - SELL: `activationPrice` should be larger than latest price.
        - If `newOrderRespType ` is sent as `RESULT` :
          - `MARKET` order: the final FILLED result of the order will be return directly.
          - `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
        - `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`:
          - Follow the same rules for condition orders.
          - If triggered，**close all** current long position( if `SELL`) or current short position( if `BUY`).
          - Cannot be used with `quantity` paremeter
          - Cannot be used with `reduceOnly` parameter
          - In Hedge Mode,cannot be used with `BUY` orders in `LONG` position side. and cannot be used with `SELL` orders in `SHORT` position side
        - `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.

        - In extreme market conditions, timeInForce `GTD` order auto cancel time might be delayed comparing to
        `goodTillDate`
      x-parameters-notes-cn: |-
        根据 order `type` 的不同，某些参数强制要求如下：

        | Type                                | 强制要求的参数                     |
        | ----------------------------------- | ---------------------------------- |
        | `LIMIT`                             | `timeInForce`, `quantity`, `price` |
        | `MARKET`                            | `quantity`                         |
        | `STOP`, `TAKE_PROFIT`               | `quantity`, `price`, `stopPrice`   |
        | `STOP_MARKET`, `TAKE_PROFIT_MARKET` | `stopPrice`                        |
        | `TRAILING_STOP_MARKET`              | `callbackRate`                     |

        - 条件单触发规则：
          - 若 `priceProtect=true`，达到触发价时，`MARK_PRICE` 与 `CONTRACT_PRICE` 的价差不能超过 `triggerProtect`（可通过 `GET /fapi/v1/exchangeInfo` 获取）。
          - `STOP`, `STOP_MARKET`：
            - 买入：最新价 >= `stopPrice`
            - 卖出：最新价 <= `stopPrice`
          - `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`：
            - 买入：最新价 <= `stopPrice`
            - 卖出：最新价 >= `stopPrice`
          - `TRAILING_STOP_MARKET`：
            - 买入：区间最低价 <= `activationPrice` 且最新价相对最低价达到回调幅度
            - 卖出：区间最高价 >= `activationPrice` 且最新价相对最高价达到回调幅度
        - `TRAILING_STOP_MARKET` 若报错 `{"code": -2021, "msg": "Order would immediately trigger."}`：
          - 买入：`activationPrice` 必须小于最新价
          - 卖出：`activationPrice` 必须大于最新价
        - `newOrderRespType=RESULT` 时：
          - `MARKET` 订单将直接返回最终成交结果
          - 特殊 `timeInForce` 的 `LIMIT` 订单将直接返回最终状态（`FILLED` 或 `EXPIRED`）
        - `STOP_MARKET`、`TAKE_PROFIT_MARKET` 配合 `closePosition=true` 时：
          - 按条件单规则触发
          - 触发后全部平仓（卖单平多，买单平空）
          - 不支持 `quantity`
          - 不支持 `reduceOnly`
          - 双向持仓模式下，`LONG` 不支持 `BUY`，`SHORT` 不支持 `SELL`
        - `selfTradePreventionMode` 仅在 `timeInForce` 为 `IOC`、`GTC` 或 `GTD` 时生效。
        - 极端行情下，`timeInForce=GTD` 订单的自动取消时间可能相对 `goodTillDate` 延迟。
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
                positionSide:
                  type: string
                  example: BOTH
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
                    - STOP
                    - STOP_MARKET
                    - TAKE_PROFIT
                    - TAKE_PROFIT_MARKET
                    - TRAILING_STOP_MARKET
                reduceOnly:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
                  description: Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`
                  x-description-cn: 双开模式下不接受此参数；使用`closePosition`不支持此参数。
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                  description: Cannot be sent with `closePosition`=`true`(Close-All)
                  x-description-cn: 下单数量,使用`closePosition`不支持此参数。
                price:
                  type: number
                  example: "1.0"
                  format: float
                newClientOrderId:
                  type: string
                  example: "1"
                  description: >-
                    A unique id among open orders. Automatically generated if not sent. Can only be string following the
                    rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                  x-description-cn: 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`
                stopPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
                  x-description-cn: 触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数
                closePosition:
                  type: string
                  example: "false"
                  enum:
                    - "true"
                    - "false"
                  description: Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`."
                  x-description-cn: 触发后全部平仓，仅支持 `STOP_MARKET` 和 `TAKE_PROFIT_MARKET`。
                activationPrice:
                  type: number
                  example: "1.0"
                  format: float
                  description: >-
                    Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different
                    `workingType`)
                  x-description-cn: 追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)
                callbackRate:
                  type: number
                  example: 1
                  minimum: 0.1
                  maximum: 5
                  format: float
                  description: Used with `TRAILING_STOP_MARKET` orders
                  x-description-cn: 追踪止损回调比例，仅 `TRAILING_STOP_MARKET` 使用。
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
                workingType:
                  type: string
                  example: MARK_PRICE
                  default: CONTRACT_PRICE
                  enum:
                    - MARK_PRICE
                    - CONTRACT_PRICE
                priceProtect:
                  type: string
                  example: "true"
                  default: "false"
                  enum:
                    - "true"
                    - "false"
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
                  description: only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`
                  x-description-cn: 盘口价格下单模式，不能与 `price` 同时传入。
                selfTradePreventionMode:
                  type: string
                  example: EXPIRE_TAKER
                  default: NONE
                  enum:
                    - NONE
                    - EXPIRE_TAKER
                    - EXPIRE_BOTH
                    - EXPIRE_MAKER
                  description: >-
                    `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker
                    order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`
                  x-description-cn: 订单自成交保护模式，默认 `NONE`。
                goodTillDate:
                  type: integer
                  example: 1770736694138
                  format: int64
                  description: >-
                    order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the
                    timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp
                    must be greater than the current time plus 600 seconds and smaller than 253402300799000
                  x-description-cn: >-
                    TIF为GTD时订单的自动取消时间，
                    当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000
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
          description: Test Order
          x-description-cn: Test 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientOrderId:
                    type: string
                    example: testOrder
                    x-description-cn: 用户自定义的订单号
                    description: Client Order Id.
                  cumQty:
                    type: string
                    example: "0"
                  cumQuote:
                    type: string
                    example: "0"
                    x-description-cn: 成交金额
                    description: Cum Quote.
                  executedQty:
                    type: string
                    example: "0"
                    x-description-cn: 成交量
                    description: Executed Qty.
                  orderId:
                    type: integer
                    example: 22542179
                    format: int64
                    x-description-cn: 系统订单号
                    description: Order Id.
                  avgPrice:
                    type: string
                    example: "0.00000"
                    x-description-cn: 平均成交价
                    description: Avg Price.
                  origQty:
                    type: string
                    example: "10"
                    x-description-cn: 原始委托数量
                    description: Orig Qty.
                  price:
                    type: string
                    example: "0"
                    x-description-cn: 委托价格
                    description: Price.
                  reduceOnly:
                    type: boolean
                    example: false
                    x-description-cn: 仅减仓
                    description: Reduce Only.
                  side:
                    type: string
                    example: SELL
                    x-description-cn: 买卖方向
                    description: Side.
                  positionSide:
                    type: string
                    example: SHORT
                    x-description-cn: 持仓方向
                    description: Position Side.
                  status:
                    type: string
                    example: NEW
                    x-description-cn: 订单状态
                    description: Status.
                  stopPrice:
                    type: string
                    example: "0"
                    description: please ignore when order type is TRAILING_STOP_MARKET
                    x-description-cn: 触发价，对`TRAILING_STOP_MARKET`无效
                  closePosition:
                    type: boolean
                    example: false
                    description: if Close-All
                    x-description-cn: 是否条件全平仓
                  symbol:
                    type: string
                    example: BTCUSDT
                    x-description-cn: 交易对
                    description: Symbol.
                  timeInForce:
                    type: string
                    example: GTD
                    x-description-cn: 有效方法
                    description: Time In Force.
                  type:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 订单类型
                    description: Type.
                  origType:
                    type: string
                    example: TRAILING_STOP_MARKET
                    x-description-cn: 触发前订单类型
                    description: Orig Type.
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
                    x-description-cn: 更新时间
                    description: Update Time.
                  workingType:
                    type: string
                    example: CONTRACT_PRICE
                    x-description-cn: 条件价格触发类型
                    description: Working Type.
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
                    example: 1693207680000
                    format: int64
                    description: order pre-set auot cancel time for TIF GTD order
                    x-description-cn: 订单TIF为GTD时的自动取消时间
  /fapi/v1/forceOrders:
    get:
      summary: User's Force Orders (USER_DATA)
      x-summary-cn: 用户强平单历史 (USER_DATA)
      description: Query user's Force Orders
      x-description-cn: 查询用户强平单历史
      tags:
        - trade
      operationId: usersForceOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade#users-force-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/TradeApi/usersForceOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/trade_api/users_force_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/Trade/users_force_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/trade/UsersForceOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/TradeAPI/UsersForceOrders/UsersForceOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/trade/UsersForceOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: "**20** with symbol, **50** without symbol"
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
          description: '"LIQUIDATION" for liquidation orders, "ADL" for ADL orders.'
          x-description-cn: '"LIQUIDATION": 强平单, "ADL": ADL 减仓单.'
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
            example: 50
            format: int64
            default: 50
            maximum: 100
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
        - If "autoCloseType" is not sent, orders with both of the types will be returned
        - If "startTime" is not sent, data within 7 days before "endTime" can be queried
      x-parameters-notes-cn: |-
        - 如果没有传 "autoCloseType", 强平单和 ADL 减仓单都会被返回
        - 如果没有传"startTime", 只会返回"endTime"之前 7 天内的数据
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
                      example: 6071832819
                      format: int64
                    symbol:
                      type: string
                      example: BTCUSDT
                    pair:
                      type: string
                      example: BTCUSDT
                      x-description-cn: 标的交易对
                      description: Pair.
                    status:
                      type: string
                      example: FILLED
                    clientOrderId:
                      type: string
                      example: autoclose-1596107620040000020
                    price:
                      type: string
                      example: "10871.09"
                    avgPrice:
                      type: string
                      example: "10913.21000"
                    origQty:
                      type: string
                      example: "0.001"
                    executedQty:
                      type: string
                      example: "0.001"
                    cumQuote:
                      type: string
                      example: "10.91321"
                    cumBase:
                      type: string
                      example: "0.001"
                      x-description-cn: 成交金额(标的数量)
                      description: Cum Base.
                    timeInForce:
                      type: string
                      example: IOC
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
                      example: BOTH
                    stopPrice:
                      type: string
                      example: "0"
                    workingType:
                      type: string
                      example: CONTRACT_PRICE
                    origType:
                      type: string
                      example: LIMIT
                    time:
                      type: integer
                      example: 1596107620044
                      format: int64
                    updateTime:
                      type: integer
                      example: 1596107620087
                      format: int64
  /fapi/v1/listenKey:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/user-data-streams#close-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/UserDataStreamsApi/closeUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/user_data_streams_api/close_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/UserDataStreams/close_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/userdatastreams/CloseUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/UserDataStreamsAPI/CloseUserDataStream/CloseUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/userdatastreams/CloseUserDataStreamExample.php
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/user-data-streams#keepalive-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/UserDataStreamsApi/keepaliveUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/user_data_streams_api/keepalive_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/UserDataStreams/keepalive_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/userdatastreams/KeepaliveUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/UserDataStreamsAPI/KeepaliveUserDataStream/KeepaliveUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/userdatastreams/KeepaliveUserDataStreamExample.php
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
                    example: 3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg
                    description: the listenkey which got extended
                    x-description-cn: 被延长有效期的 listenKey
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
        stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。
      tags:
        - user-data-streams
      operationId: startUserDataStream
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/user-data-streams#start-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-usds-futures/examples/rest-api/UserDataStreamsApi/startUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_usds_futures/rest_api/user_data_streams_api/start_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_usds_futures/examples/rest_api/UserDataStreams/start_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-usds-futures/src/main/java/com/binance/connector/client/derivatives_trading_usds_futures/rest/userdatastreams/StartUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingusdsfutures/examples/restapi/UserDataStreamsAPI/StartUserDataStream/StartUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-usds-futures/userdatastreams/StartUserDataStreamExample.php
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
```