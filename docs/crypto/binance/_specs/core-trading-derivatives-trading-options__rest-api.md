---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:41.819798
---

# core-trading-derivatives-trading-options__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Options REST API
  description: Access market data, manage accounts, and trade Binance Options.
  x-description-cn: 访问市场数据、管理账户，并交易 Binance 期权。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/derivatives-trading-options/general-info#limits
x-rate-limits-guide-cn: products/derivatives-trading-options/general-info#访问限制
x-security-guide: products/derivatives-trading-options/general-info#endpoint-security-type
x-security-guide-cn: products/derivatives-trading-options/general-info#接口鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Options docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-options/general-info
  x-description-cn: Options docs
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: market-maker-block-trade
    x-displayName: Market Maker Block Trade
    x-displayName-cn: 大宗交易
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 行情接口
  - name: market-maker-endpoints
    x-displayName: Market Maker Endpoints
    x-displayName-cn: 做市商接口
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易接口
  - name: user-data-streams
    x-displayName: User Data Streams
    x-displayName-cn: Websocket账户信息推送
servers:
  - url: https://eapi.binance.com
  - url: https://testnet.binancefuture.com
paths:
  /eapi/v1/bill:
    get:
      summary: Account Funding Flow (USER_DATA)
      x-summary-cn: 获取账户资金流水 (USER_DATA)
      description: Query account funding flows.
      x-description-cn: 获取期权账户资金流水
      tags:
        - account
      operationId: accountFundingFlow
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/account#account-funding-flow
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/AccountApi/accountFundingFlow.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/account_api/account_funding_flow.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Account/account_funding_flow.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/account/AccountFundingFlowExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/AccountAPI/AccountFundingFlow/AccountFundingFlow.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/account/AccountFundingFlowExample.php
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
        - name: currency
          in: query
          required: true
          schema:
            type: string
            example: USDT
            enum:
              - USDT
          description: Asset type, only support USDT  as of now
          x-description-cn: 资产类型目前仅支持USDT
        - name: recordId
          in: query
          required: false
          schema:
            type: integer
            example: 100000
            format: int64
          description: Return the recordId and subsequent data, the latest data is returned by default
          x-description-cn: 返回该`recordId`及之后的成交，缺省返回最近的成交
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 1000
            format: int64
          description: Number of result sets returned
          x-description-cn: 返回结果集数量
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
      x-parameters-notes: "- Only support querying data in the past 3 months"
      x-parameters-notes-cn: "- 仅支持查询最近3个月的数据"
      responses:
        "200":
          description: Account Funding Flow
          x-description-cn: 账户 Funding Flow
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1125899906842624000
                      format: int64
                      description: id
                      x-description-cn: ID
                    asset:
                      type: string
                      example: USDT
                      description: Asset type
                      x-description-cn: 资产类型
                    amount:
                      type: string
                      example: "-0.552"
                      description: Amount (positive numbers represent inflow, negative numbers represent outflow)
                      x-description-cn: 数量 (正数为流入，负数为流出)
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: >-
                        Option symbol the record relates to. Returned only for contract-related types (e.g. `CONTRACT`,
                        `FEE`, `EXERCISE_PNL`, `EXERCISE_FEE`); omitted for other types such as `TRANSFER`. Older
                        records may not include this field.
                      x-description-cn: >-
                        该记录对应的期权交易对。仅在合约相关类型（如 `CONTRACT`、`FEE`、`EXERCISE_PNL`、`EXERCISE_FEE`）中返回；其他类型（如
                        `TRANSFER`）不返回该字段。较早的记录可能不包含该字段。
                    type:
                      type: string
                      example: FEE
                      description: type (fees)
                      x-description-cn: 类型 (手续费)
                    createDate:
                      type: integer
                      example: 1592449456000
                      format: int64
                      description: Time
                      x-description-cn: 时间
  /eapi/v1/marginAccount:
    get:
      summary: Option Margin Account Information (USER_DATA)
      x-summary-cn: 保证金账户信息 (USER_DATA)
      description: Get current account information.
      x-description-cn: 获取保证金账户信息
      tags:
        - account
      operationId: optionMarginAccountInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/account#option-margin-account-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/AccountApi/optionMarginAccountInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/account_api/option_margin_account_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Account/option_margin_account_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/account/OptionMarginAccountInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/AccountAPI/OptionMarginAccountInformation/OptionMarginAccountInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/account/OptionMarginAccountInformationExample.php
      x-ip-weight: 3
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
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Option Margin Account Information
          x-description-cn: Option 杠杆 账户 信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  asset:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                          description: asset
                          x-description-cn: 资产
                        marginBalance:
                          type: string
                          example: "10099.448"
                          description: margin Balance
                          x-description-cn: 账户余额
                        equity:
                          type: string
                          example: "10094.44662"
                          description: equity
                          x-description-cn: 账户权益
                        available:
                          type: string
                          example: "8725.92524"
                          description: available
                          x-description-cn: 账户可用
                        initialMargin:
                          type: string
                          example: "1084.52138"
                          description: initial Margin
                          x-description-cn: 初始保证金
                        maintMargin:
                          type: string
                          example: "151.00138"
                          description: maint Margin
                          x-description-cn: 维持保证金
                        unrealizedPNL:
                          type: string
                          example: "-5.00138"
                          description: unrealized PNL
                          x-description-cn: 未实现盈亏
                        adjustedEquity:
                          type: string
                          example: "34.13282285"
                          description: adjusted Equity
                          x-description-cn: margin balance + BTC多仓价值
                    description: asset
                    x-description-cn: 资产
                  greek:
                    type: array
                    items:
                      type: object
                      properties:
                        underlying:
                          type: string
                          example: BTCUSDT
                          description: underlying
                          x-description-cn: 标的资产
                        delta:
                          type: string
                          example: "-0.05"
                          description: delta
                          x-description-cn: Delta
                        gamma:
                          type: string
                          example: "-0.002"
                          description: gamma
                          x-description-cn: Gamma
                        theta:
                          type: string
                          example: "-0.05"
                          description: theta
                          x-description-cn: Theta
                        vega:
                          type: string
                          example: "-0.002"
                          description: vega
                          x-description-cn: Vega
                    description: greek
                    x-description-cn: greek
                  time:
                    type: integer
                    example: 1762843368098
                    format: int64
                    description: time
                    x-description-cn: 时间
                  canTrade:
                    type: boolean
                    example: true
                    description: can Trade
                    x-description-cn: 是否可交易
                  canDeposit:
                    type: boolean
                    example: true
                    description: can Deposit
                    x-description-cn: 是否可入金
                  canWithdraw:
                    type: boolean
                    example: true
                    description: can Withdraw
                    x-description-cn: 是否可出金
                  reduceOnly:
                    type: boolean
                    example: false
                    description: reduce Only
                    x-description-cn: 仅减仓
                  tradeGroupId:
                    type: integer
                    example: -1
                    format: int64
                    description: Trade group ID
                    x-description-cn: 交易组 ID
  /eapi/v1/time:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#check-server-time
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/checkServerTime.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/check_server_time.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/check_server_time.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/CheckServerTimeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/CheckServerTime/CheckServerTime.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/CheckServerTimeExample.php
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
                    example: 1592387156596
                    format: int64
                    description: server Time
                    x-description-cn: 当前的系统时间
  /eapi/v1/exchangeInfo:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#exchange-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/exchangeInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/exchange_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/exchange_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/ExchangeInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/ExchangeInformation/ExchangeInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/ExchangeInformationExample.php
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
                  timezone:
                    type: string
                    example: UTC
                    description: Time zone used by the server
                    x-description-cn: 服务器时区
                  serverTime:
                    type: integer
                    example: 1592387337630
                    format: int64
                    description: Current system time
                    x-description-cn: 请忽略。如果需要获取当前系统时间，请查询接口 “GET /eapi/v1/time”
                  optionContracts:
                    type: array
                    items:
                      type: object
                      properties:
                        baseAsset:
                          type: string
                          example: BTC
                          description: Base currency
                          x-description-cn: 标的资产
                        quoteAsset:
                          type: string
                          example: USDT
                          description: Quotation asset
                          x-description-cn: 报价资产
                        underlying:
                          type: string
                          example: BTCUSDT
                          description: Name of the underlying asset of the option contract
                          x-description-cn: 期权合约底层资产
                        settleAsset:
                          type: string
                          example: USDT
                          description: Settlement currency
                          x-description-cn: 结算资产
                    description: Option contract underlying asset info
                    x-description-cn: 期权合约底层资产信息
                  optionAssets:
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                          example: USDT
                          description: Asset name
                          x-description-cn: 资产名
                    description: Option asset info
                    x-description-cn: 期权系统支持资产
                  optionSymbols:
                    type: array
                    items:
                      type: object
                      properties:
                        expiryDate:
                          type: integer
                          example: 1660521600000
                          format: int64
                          description: expiry time
                          x-description-cn: 到期时间
                        filters:
                          type: array
                          items:
                            type: object
                            properties:
                              filterType:
                                type: string
                                example: PRICE_FILTER
                                description: filter Type
                                x-description-cn: filter Type
                              minPrice:
                                type: string
                                example: "0.02"
                                description: min Price
                                x-description-cn: 最小价格
                              maxPrice:
                                type: string
                                example: "80000.01"
                                description: max Price
                                x-description-cn: 最大价格
                              tickSize:
                                type: string
                                example: "0.01"
                                description: tick Size
                                x-description-cn: 最小价格精度
                              minQty:
                                type: string
                                example: "0.01"
                                description: Minimum order quantity
                                x-description-cn: 最小下单数量
                              maxQty:
                                type: string
                                example: "100"
                                description: Maximum order quantity
                                x-description-cn: 最大下单数量
                              stepSize:
                                type: string
                                example: "0.01"
                                description: step Size
                                x-description-cn: 数量步长
                          description: filters
                          x-description-cn: filters
                        symbol:
                          type: string
                          example: BTC-220815-50000-C
                          description: Trading pair name
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: CALL
                          description: "Direction: CALL long, PUT short"
                          x-description-cn: 期权方向
                        strikePrice:
                          type: string
                          example: "50000"
                          description: Strike price
                          x-description-cn: 行权价
                        underlying:
                          type: string
                          example: BTCUSDT
                          description: Name of the underlying asset of the option contract
                          x-description-cn: 期权合约底层资产
                        unit:
                          type: integer
                          example: 1
                          format: int64
                          description: Contract unit, the quantity of the underlying asset represented by a single contract.
                          x-description-cn: 合约单位, 单一合约代表的底层资产数量
                        liquidationFeeRate:
                          type: string
                          example: "0.0019000"
                          description: liquidation fee rate
                          x-description-cn: 爆仓手续费
                        minQty:
                          type: string
                          example: "0.01"
                          description: Minimum order quantity
                          x-description-cn: 最小下单数量
                        maxQty:
                          type: string
                          example: "100"
                          description: Maximum order quantity
                          x-description-cn: 最大下单数量
                        initialMargin:
                          type: string
                          example: "0.15"
                          description: Initial Magin Ratio
                          x-description-cn: 初始保证金率
                        maintenanceMargin:
                          type: string
                          example: "0.075"
                          description: Maintenance Margin Ratio
                          x-description-cn: 维持保证金率
                        minInitialMargin:
                          type: string
                          example: "0.1"
                          description: Min Initial Margin Ratio
                          x-description-cn: 最低初始保证金率
                        minMaintenanceMargin:
                          type: string
                          example: "0.05"
                          description: Min Maintenance Margin Ratio
                          x-description-cn: 最低维持保证金率
                        priceScale:
                          type: integer
                          example: 2
                          format: int64
                          description: price precision
                          x-description-cn: 价格精度
                        quantityScale:
                          type: integer
                          example: 2
                          format: int64
                          description: quantity precision
                          x-description-cn: 数量精度
                        quoteAsset:
                          type: string
                          example: USDT
                          description: Quotation asset
                          x-description-cn: 报价资产
                        contractType:
                          type: string
                          example: CRYPTO_OPTIONS
                          description: Contract type
                          x-description-cn: 合约类型
                        underlyingType:
                          type: string
                          example: CRYPTO
                          description: Underlying type
                          x-description-cn: 标的类型
                        nakedSell:
                          type: boolean
                          example: false
                          description: Whether naked selling is allowed for this symbol
                          x-description-cn: 是否允许该交易对进行裸卖空
                        status:
                          type: string
                          example: TRADING
                          description: Trading Status
                          x-description-cn: 状态
                    description: Option trading pair info
                    x-description-cn: 期权交易对信息
                  rateLimits:
                    type: array
                    items:
                      type: object
                      properties:
                        rateLimitType:
                          type: string
                          example: REQUEST_WEIGHT
                          description: rate Limit Type
                          x-description-cn: 限频类型
                        interval:
                          type: string
                          example: MINUTE
                          description: interval
                          x-description-cn: 时间区间
                        intervalNum:
                          type: integer
                          example: 1
                          format: int64
                          description: interval Num
                          x-description-cn: 区间数量
                        limit:
                          type: integer
                          example: 2400
                          format: int64
                          description: limit
                          x-description-cn: 限制值
                    description: rate Limits
                    x-description-cn: rate Limits
  /eapi/v1/exerciseHistory:
    get:
      summary: Historical Exercise Records
      x-summary-cn: 历史行权记录
      description: |-
        Get historical exercise records.

        * REALISTIC_VALUE_STRICKEN -> Exercised
        * EXTRINSIC_VALUE_EXPIRED -> Expired OTM
      x-description-cn: |-
        查询行权记录

        * REALISTIC_VALUE_STRICKEN 行权
        * EXTRINSIC_VALUE_EXPIRED 未行权
      tags:
        - market-data
      operationId: historicalExerciseRecords
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#historical-exercise-records
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/historicalExerciseRecords.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/historical_exercise_records.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/historical_exercise_records.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/HistoricalExerciseRecordsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/HistoricalExerciseRecords/HistoricalExerciseRecords.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/HistoricalExerciseRecordsExample.php
      x-ip-weight: 3
      parameters:
        - name: underlying
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 100
            format: int64
          description: Number of result sets returned
          x-description-cn: 返回结果集数量，默认值100，最大值100
      responses:
        "200":
          description: Historical Exercise Records
          x-description-cn: 请参见英文说明：Historical Exercise Records
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTC-220121-60000-P
                      description: symbol
                      x-description-cn: 交易对
                    strikePrice:
                      type: string
                      example: "60000"
                      description: strike price
                      x-description-cn: 行权价
                    realStrikePrice:
                      type: string
                      example: "38844.69652571"
                      description: real strike price
                      x-description-cn: 行权结算价格
                    expiryDate:
                      type: integer
                      example: 1642752000000
                      format: int64
                      description: Exercise time
                      x-description-cn: 行权时间
                    strikeResult:
                      type: string
                      example: REALISTIC_VALUE_STRICKEN
                      description: strike result
                      x-description-cn: 行权结果
  /eapi/v1/index:
    get:
      summary: Index Price
      x-summary-cn: 标的指数价格
      description: Get spot index price for option underlying.
      x-description-cn: 返回指数价格
      tags:
        - market-data
      operationId: indexPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#index-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/indexPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/index_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/index_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/IndexPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/IndexPrice/IndexPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/IndexPriceExample.php
      x-ip-weight: 1
      parameters:
        - name: underlying
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
      responses:
        "200":
          description: Index Price
          x-description-cn: Index 价格
          content:
            application/json:
              schema:
                type: object
                properties:
                  time:
                    type: integer
                    example: 1656647305000
                    format: int64
                    description: time
                    x-description-cn: 时间
                  indexPrice:
                    type: string
                    example: "105917.75"
                    description: index Price
                    x-description-cn: 指数价格
  /eapi/v1/klines:
    get:
      summary: Kline/Candlestick Data
      x-summary-cn: K线数据
      description: Kline/candlestick bars for an option symbol. Klines are uniquely identified by their open time.
      x-description-cn: K线数据，每根K线的开盘时间可视为唯一ID
      tags:
        - market-data
      operationId: klineCandlestickData
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#kline-candlestick-data
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/klineCandlestickData.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/kline_candlestick_data.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/kline_candlestick_data.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/KlineCandlestickDataExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/KlineCandlestickData/KlineCandlestickData.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/KlineCandlestickDataExample.php
      x-ip-weight: 1
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTC-200730-9000-C
          description: Option trading pair
          x-description-cn: 交易对
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
          description: Time interval
          x-description-cn: 时间间隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 500
            maximum: 1500
            format: int64
          description: Number of result sets returned
          x-description-cn: 返回结果集数量
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
                      example: 1762779600000
                    - type: string
                      description: Open
                      x-description-cn: 开盘价
                      example: "1300.000"
                    - type: string
                      description: High
                      x-description-cn: 最高价
                      example: "1300.000"
                    - type: string
                      description: Low
                      x-description-cn: 最低价
                      example: "1300.000"
                    - type: string
                      description: Close
                      x-description-cn: 收盘价
                      example: "1300.000"
                    - type: string
                      description: Volume
                      x-description-cn: 成交量
                      example: "0.1000"
                    - type: integer
                      format: int64
                      description: Close time
                      x-description-cn: 收盘时间
                      example: 1762780499999
                    - type: string
                      description: Quote asset volume
                      x-description-cn: 成交额
                      example: "130.0000000"
                    - type: integer
                      description: Number of trades
                      x-description-cn: 成交笔数
                      example: 1
                    - type: string
                      description: Taker buy base asset volume
                      x-description-cn: 主动买入成交量
                      example: "0.1000"
                    - type: string
                      description: Taker buy quote asset volume
                      x-description-cn: 主动买入成交额
                      example: "130.0000000"
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
                        example: 1762779600000
                      - type: string
                        description: Open
                        x-description-cn: 开盘价
                        example: "1300.000"
                      - type: string
                        description: High
                        x-description-cn: 最高价
                        example: "1300.000"
                      - type: string
                        description: Low
                        x-description-cn: 最低价
                        example: "1300.000"
                      - type: string
                        description: Close
                        x-description-cn: 收盘价
                        example: "1300.000"
                      - type: string
                        description: Volume
                        x-description-cn: 成交量
                        example: "0.1000"
                      - type: integer
                        format: int64
                        description: Close time
                        x-description-cn: 收盘时间
                        example: 1762780499999
                      - type: string
                        description: Quote asset volume
                        x-description-cn: 成交额
                        example: "130.0000000"
                      - type: integer
                        description: Number of trades
                        x-description-cn: 成交笔数
                        example: 1
                      - type: string
                        description: Taker buy base asset volume
                        x-description-cn: 主动买入成交量
                        example: "0.1000"
                      - type: string
                        description: Taker buy quote asset volume
                        x-description-cn: 主动买入成交额
                        example: "130.0000000"
                      - type: string
                        description: Ignore
                        x-description-cn: 忽略字段
                        example: "0"
  /eapi/v1/openInterest:
    get:
      summary: Open Interest
      x-summary-cn: 合约持仓量
      description: Get open interest for specific underlying asset on specific expiration date.
      x-description-cn: 获取期权持仓量。
      tags:
        - market-data
      operationId: openInterest
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#open-interest
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/openInterest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/open_interest.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/open_interest.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/OpenInterestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/OpenInterest/OpenInterest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/OpenInterestExample.php
      x-ip-weight: 0
      parameters:
        - name: underlyingAsset
          in: query
          required: true
          schema:
            type: string
            example: ETH/BTC
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: expiration
          in: query
          required: true
          schema:
            type: string
            example: 221225
          description: expiration date
          x-description-cn: 到期日
      responses:
        "200":
          description: Open Interest
          x-description-cn: 未完成利息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: ETH-221119-1175-P
                      description: symbol
                      x-description-cn: 交易对
                    sumOpenInterest:
                      type: string
                      example: "4.01"
                      description: sum Open Interest
                      x-description-cn: 总持仓量
                    sumOpenInterestUsd:
                      type: string
                      example: "4880.2985615624"
                      description: sum Open Interest Usd
                      x-description-cn: 总持仓量(USD)
                    timestamp:
                      type: string
                      example: "1668754020000"
                      description: timestamp
                      x-description-cn: 时间戳
  /eapi/v1/mark:
    get:
      summary: Option Mark Price
      x-summary-cn: 查询期权标记价格
      description: Option mark price and greek info.
      x-description-cn: 查询期权标记价格
      tags:
        - market-data
      operationId: optionMarkPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#option-mark-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/optionMarkPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/option_mark_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/option_mark_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/OptionMarkPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/OptionMarkPrice/OptionMarkPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/OptionMarkPriceExample.php
      x-ip-weight: 5
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTC-200730-9000-C
          description: Option trading pair
          x-description-cn: 交易对如
      responses:
        "200":
          description: Option Mark Price
          x-description-cn: Option Mark 价格
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: symbol
                      x-description-cn: 交易对
                    markPrice:
                      type: string
                      example: "1343.2883"
                      description: Mark price
                      x-description-cn: 标记价格
                    bidIV:
                      type: string
                      example: "1.40000077"
                      description: Implied volatility Buy
                      x-description-cn: 买一隐含波动率
                    askIV:
                      type: string
                      example: "1.50000153"
                      description: Implied volatility Sell
                      x-description-cn: 卖一隐含波动率
                    markIV:
                      type: string
                      example: "1.45000000"
                      description: Implied volatility mark
                      x-description-cn: 标记价格隐含波动率
                    delta:
                      type: string
                      example: "0.55937056"
                      description: delta
                      x-description-cn: Delta
                    theta:
                      type: string
                      example: "3739.82509871"
                      description: theta
                      x-description-cn: Theta
                    gamma:
                      type: string
                      example: "0.00010969"
                      description: gamma
                      x-description-cn: Gamma
                    vega:
                      type: string
                      example: "978.58874732"
                      description: vega
                      x-description-cn: Vega
                    highPriceLimit:
                      type: string
                      example: "1618.241"
                      description: Current highest buy price
                      x-description-cn: 买最高限价
                    lowPriceLimit:
                      type: string
                      example: "1068.3356"
                      description: Current lowest sell price
                      x-description-cn: 卖最低限价
                    riskFreeInterest:
                      type: string
                      example: "0.1"
                      description: risk free rate
                      x-description-cn: 无风险利率
  /eapi/v1/depth:
    get:
      summary: Order Book
      x-summary-cn: 深度信息
      description: Check orderbook depth on specific symbol
      x-description-cn: 查询特定交易对深度
      tags:
        - market-data
      operationId: orderBook
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#order-book
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/orderBook.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/order_book.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/order_book.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/OrderBookExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/OrderBook/OrderBook.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/OrderBookExample.php
      x-weight: |-
        limit         | weight
        ------------  | ------------
        5, 10, 20, 50 | 1
        100           | 5
        500           | 10
        1000          | 20
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTC-200730-9000-C
          description: Option trading pair
          x-description-cn: 交易对
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 1000
            format: int64
          description: Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000]
          x-description-cn: 默认值:100 最大值:1000 可选值:[10, 20, 50, 100, 500, 1000]
      responses:
        "200":
          description: Order Book
          x-description-cn: 订单 Book
          content:
            application/json:
              schema:
                type: object
                properties:
                  bids:
                    type: array
                    description: Bid orders. Each entry is [price, quantity].
                    x-description-cn: 买单列表。每项为 [价格, 数量]。
                    example:
                      - - "1000.000"
                        - "0.1000"
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price
                          example: "1000.000"
                        - type: string
                          description: Quantity
                          example: "0.1000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            example: "1000.000"
                          - type: string
                            description: Quantity
                            example: "0.1000"
                  asks:
                    type: array
                    description: Ask orders. Each entry is [price, quantity].
                    x-description-cn: 卖单列表。每项为 [价格, 数量]。
                    example:
                      - - "1900.000"
                        - "0.1000"
                    items:
                      type: array
                      minItems: 2
                      maxItems: 2
                      x-prefixItems:
                        - type: string
                          description: Price
                          example: "1900.000"
                        - type: string
                          description: Quantity
                          example: "0.1000"
                      items:
                        oneOf:
                          - type: string
                            description: Price
                            example: "1900.000"
                          - type: string
                            description: Quantity
                            example: "0.1000"
                  T:
                    type: integer
                    example: 1762780909676
                    format: int64
                    description: transaction time
                    x-description-cn: 撮合引擎时间
                  lastUpdateId:
                    type: integer
                    example: 361
                    format: int64
                    description: update id
                    x-description-cn: 更新id
  /eapi/v1/blockTrades:
    get:
      summary: Recent Block Trades List
      x-summary-cn: 大宗交易历史
      description: Get recent block trades
      x-description-cn: 查询最近的大宗交易历史
      tags:
        - market-data
      operationId: recentBlockTradesList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#recent-block-trades-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/recentBlockTradesList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/recent_block_trades_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/recent_block_trades_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/RecentBlockTradesListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/RecentBlockTradesList/RecentBlockTradesList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/RecentBlockTradesListExample.php
      x-ip-weight: 5
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTC-200730-9000-C
          description: Option trading pair
          x-description-cn: 交易对如
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 500
            format: int64
          description: Number of records
          x-description-cn: 记录数量
      responses:
        "200":
          description: Recent Block Trades List
          x-description-cn: Recent Block 交易s 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1125899906901081100
                      format: int64
                      description: id
                      x-description-cn: ID
                    tradeId:
                      type: integer
                      example: 389
                      format: int64
                      description: trade Id
                      x-description-cn: 成交ID
                    symbol:
                      type: string
                      example: ETH-250725-1200-P
                      description: symbol
                      x-description-cn: 交易对
                    price:
                      type: string
                      example: "342.40"
                      description: price
                      x-description-cn: 价格
                    qty:
                      type: string
                      example: "-2167.20"
                      description: qty
                      x-description-cn: 数量
                    quoteQty:
                      type: string
                      example: "-4.90"
                      description: quote Qty
                      x-description-cn: 报价资产数量
                    side:
                      type: integer
                      example: -1
                      format: int64
                      description: side
                      x-description-cn: 方向
                    time:
                      type: integer
                      example: 1733950676483
                      format: int64
                      description: time
                      x-description-cn: 时间
  /eapi/v1/trades:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#recent-trades-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/recentTradesList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/recent_trades_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/recent_trades_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/RecentTradesListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/RecentTradesList/RecentTradesList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/RecentTradesListExample.php
      x-ip-weight: 5
      parameters:
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            example: BTC-200730-9000-C
          description: Option trading pair
          x-description-cn: 交易对
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 500
            format: int64
          description: Number of result sets returned
          x-description-cn: 返回结果集数量
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
                      example: 2323857420768529000
                      format: int64
                      description: id
                      x-description-cn: ID
                    tradeId:
                      type: integer
                      example: 1
                      format: int64
                      description: TradeId
                      x-description-cn: 成交ID
                    symbol:
                      type: string
                      example: BTC-251123-126000-C
                      description: Option trading pair
                      x-description-cn: 期权交易对
                    price:
                      type: string
                      example: "1300"
                      description: Completed trade price
                      x-description-cn: 成交价格
                    qty:
                      type: string
                      example: "0.1"
                      description: Completed trade quantity
                      x-description-cn: 成交量
                    quoteQty:
                      type: string
                      example: "130"
                      description: Completed trade amount
                      x-description-cn: 成交额
                    side:
                      type: integer
                      example: -1
                      format: int64
                      description: Completed trade direction（-1 Sell，1 Buy）
                      x-description-cn: 主动成交方方向（-1 Sell，1 Buy）
                    time:
                      type: integer
                      example: 1762780453623
                      format: int64
                      description: Time
                      x-description-cn: 时间
  /eapi/v1/ping:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#test-connectivity
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/testConnectivity.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/test_connectivity.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/test_connectivity.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/TestConnectivityExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/TestConnectivity/TestConnectivity.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/TestConnectivityExample.php
      x-ip-weight: 1
      parameters: []
      responses:
        "200":
          description: OK
          x-description-cn: 成功
  /eapi/v1/ticker:
    get:
      summary: 24hr Ticker Price Change Statistics
      x-summary-cn: 24hr价格变动情况
      description: 24 hour rolling window price change statistics.
      x-description-cn: 24小时期权价格变动
      tags:
        - market-data
      operationId: ticker24hrPriceChangeStatistics
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-data#ticker24hr-price-change-statistics
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketDataApi/ticker24hrPriceChangeStatistics.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_data_api/ticker24hr_price_change_statistics.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketData/ticker24hr_price_change_statistics.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketdata/Ticker24hrPriceChangeStatisticsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketDataAPI/Ticker24hrPriceChangeStatistics/Ticker24hrPriceChangeStatistics.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketdata/Ticker24hrPriceChangeStatisticsExample.php
      x-weight: 1 for a single symbol; 40 when the symbol parameter is omitted
      parameters:
        - name: symbol
          in: query
          required: false
          schema:
            type: string
            example: BTC-200730-9000-C
          description: Option trading pair
          x-description-cn: 交易对如
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
                      example: BTC-200730-9000-C
                      description: symbol
                      x-description-cn: 交易对
                    priceChange:
                      type: string
                      example: "-16.2038"
                      description: 24-hour price change
                      x-description-cn: 24小时价格变动
                    priceChangePercent:
                      type: string
                      example: "-0.0162"
                      description: 24-hour percent price change
                      x-description-cn: 24小时价格变动百分比
                    lastPrice:
                      type: string
                      example: "1000"
                      description: Last trade price
                      x-description-cn: 最近一次成交价
                    lastQty:
                      type: string
                      example: "1000"
                      description: Last trade amount
                      x-description-cn: 最近一次成交额
                    open:
                      type: string
                      example: "1016.2038"
                      description: 24-hour open price
                      x-description-cn: 24小时内第一次成交的价格
                    high:
                      type: string
                      example: "1016.2038"
                      description: 24-hour high
                      x-description-cn: 24小时最高价
                    low:
                      type: string
                      example: "0"
                      description: 24-hour low
                      x-description-cn: 24小时最低价
                    volume:
                      type: string
                      example: "5"
                      description: Trading volume(contracts)
                      x-description-cn: 成交额
                    amount:
                      type: string
                      example: "1"
                      description: Trade amount(in quote asset)
                      x-description-cn: 成交量
                    bidPrice:
                      type: string
                      example: "999.34"
                      description: The best buy price
                      x-description-cn: 最优买价
                    askPrice:
                      type: string
                      example: "1000.23"
                      description: The best sell price
                      x-description-cn: 最优卖价
                    openTime:
                      type: integer
                      example: 1592317127349
                      format: int64
                      description: Time the first trade occurred within the last 24 hours
                      x-description-cn: 24小时内，第一笔交易的发生时间
                    closeTime:
                      type: integer
                      example: 1592380593516
                      format: int64
                      description: Time the last trade occurred within the last 24 hours
                      x-description-cn: 24小时内，最后一笔交易的发生时间
                    firstTradeId:
                      type: integer
                      example: 1
                      format: int64
                      description: First trade ID
                      x-description-cn: 首笔成交ID
                    tradeCount:
                      type: integer
                      example: 5
                      format: int64
                      description: Number of trades
                      x-description-cn: 成交笔数
                    strikePrice:
                      type: string
                      example: "9000"
                      description: Strike price
                      x-description-cn: 行权价
                    exercisePrice:
                      type: string
                      example: "3000.3356"
                      description: return estimated settlement price one hour before exercise, return index price at other times
                      x-description-cn: 行权前半小时返回预估结算价，其他时刻返回指数价格
  /eapi/v1/block/order/execute:
    post:
      summary: Accept Block Trade Order (TRADE)
      x-summary-cn: Accept Block 交易 订单 (TRADE)
      description: Accept a block trade order
      x-description-cn: Accept a block 交易 订单
      tags:
        - market-maker-block-trade
      operationId: acceptBlockTradeOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#accept-block-trade-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/acceptBlockTradeOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/accept_block_trade_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/accept_block_trade_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/AcceptBlockTradeOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/AcceptBlockTradeOrder/AcceptBlockTradeOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/AcceptBlockTradeOrderExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - blockOrderMatchingKey
                - timestamp
              properties:
                blockOrderMatchingKey:
                  type: string
                  example: 7d046e6e-a429-4335-ab9d-6a681febcde5
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
          description: Accept Block Trade Order
          x-description-cn: Accept Block 交易 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  blockTradeSettlementKey:
                    type: string
                    example: 7d046e6e-a429-4335-ab9d-6a681febcde5
                    description: block Trade Settlement Key
                    x-description-cn: block Trade Settlement Key
                  expireTime:
                    type: integer
                    example: 1730172115801
                    format: int64
                    description: expire Time
                    x-description-cn: expire Time
                  liquidity:
                    type: string
                    example: MAKER
                    description: liquidity
                    x-description-cn: liquidity
                  status:
                    type: string
                    example: ACCEPTED
                    description: status
                    x-description-cn: 状态
                  createTime:
                    type: integer
                    example: 1730170315803
                    format: int64
                    description: create Time
                    x-description-cn: create Time
                  legs:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BNB-241101-700-C
                          description: symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: SELL
                          description: side
                          x-description-cn: 方向
                        quantity:
                          type: string
                          example: "1.2"
                          description: quantity
                          x-description-cn: 数量
                        price:
                          type: string
                          example: "2.8"
                          description: price
                          x-description-cn: 价格
                    description: legs
                    x-description-cn: legs
    get:
      summary: Query Block Trade Details (USER_DATA)
      x-summary-cn: 查询Block 交易 Details (USER_DATA)
      description: Query block trade details; returns block trade details from counterparty's perspective.
      x-description-cn: 查询block 交易 details; returns block 交易 details 从 counterparty's perspective.
      tags:
        - market-maker-block-trade
      operationId: queryBlockTradeDetails
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#query-block-trade-details
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/queryBlockTradeDetails.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/query_block_trade_details.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/query_block_trade_details.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/QueryBlockTradeDetailsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/QueryBlockTradeDetails/QueryBlockTradeDetails.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/QueryBlockTradeDetailsExample.php
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
        - name: blockOrderMatchingKey
          in: query
          required: true
          schema:
            type: string
            example: 12b96c28-ba05-8906-c89t-703215cfb2e6
          description: Block trade matching key.
          x-description-cn: 大宗交易撮合键。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Block Trade Details
          x-description-cn: Block 交易 Details
          content:
            application/json:
              schema:
                type: object
                properties:
                  blockTradeSettlementKey:
                    type: string
                    example: 12b96c28-ba05-8906-c89t-703215cfb2e6
                    description: block Trade Settlement Key
                    x-description-cn: block Trade Settlement Key
                  expireTime:
                    type: integer
                    example: 1730171860460
                    format: int64
                    description: expire Time
                    x-description-cn: expire Time
                  liquidity:
                    type: string
                    example: MAKER
                    description: liquidity
                    x-description-cn: liquidity
                  status:
                    type: string
                    example: RECEIVED
                    description: status
                    x-description-cn: 状态
                  createTime:
                    type: integer
                    example: 1730170060462
                    format: int64
                    description: create Time
                    x-description-cn: create Time
                  legs:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BNB-241101-700-C
                          description: symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: SELL
                          description: side
                          x-description-cn: 方向
                        quantity:
                          type: string
                          example: "1.66"
                          description: quantity
                          x-description-cn: 数量
                        price:
                          type: string
                          example: "20"
                          description: price
                          x-description-cn: 价格
                    description: legs
                    x-description-cn: legs
  /eapi/v1/block/user-trades:
    get:
      summary: Account Block Trade List (USER_DATA)
      x-summary-cn: 账户 Block 交易 列表 (USER_DATA)
      description: Gets block trades for a specific account.
      x-description-cn: Gets block trades 用于 a specific 账户.
      tags:
        - market-maker-block-trade
      operationId: accountBlockTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#account-block-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/accountBlockTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/account_block_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/account_block_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/AccountBlockTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/AccountBlockTradeList/AccountBlockTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/AccountBlockTradeListExample.php
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
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: underlying
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Account Block Trade List
          x-description-cn: 账户 Block 交易 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    parentOrderId:
                      type: string
                      example: "4675011431944499201"
                      description: parent Order Id
                      x-description-cn: parent Order Id
                    crossType:
                      type: string
                      example: USER_BLOCK
                      description: cross Type
                      x-description-cn: cross Type
                    legs:
                      type: array
                      items:
                        type: object
                        properties:
                          createTime:
                            type: integer
                            example: 1730170445600
                            format: int64
                            description: create Time
                            x-description-cn: create Time
                          updateTime:
                            type: integer
                            example: 1730170445600
                            format: int64
                            description: update Time
                            x-description-cn: 更新时间
                          symbol:
                            type: string
                            example: BNB-241101-700-C
                            description: symbol
                            x-description-cn: 交易对
                          orderId:
                            type: string
                            example: "4675011431944499203"
                            description: order Id
                            x-description-cn: 订单ID
                          orderPrice:
                            type: number
                            example: 2.8
                            format: float
                            description: order Price
                            x-description-cn: order Price
                          orderQuantity:
                            type: number
                            example: 1.2
                            format: float
                            description: order Quantity
                            x-description-cn: order Quantity
                          orderStatus:
                            type: string
                            example: FILLED
                            description: order Status
                            x-description-cn: order Status
                          executedQty:
                            type: number
                            example: 1.2
                            format: float
                            description: executed Qty
                            x-description-cn: executed Qty
                          executedAmount:
                            type: number
                            example: 3.36
                            format: float
                            description: executed Amount
                            x-description-cn: executed Amount
                          fee:
                            type: number
                            example: 0.336
                            format: float
                            description: fee
                            x-description-cn: fee
                          orderType:
                            type: string
                            example: PREV_QUOTED
                            description: order Type
                            x-description-cn: order Type
                          orderSide:
                            type: string
                            example: BUY
                            description: order Side
                            x-description-cn: order Side
                          id:
                            type: string
                            example: "1125899906900937837"
                            description: id
                            x-description-cn: ID
                          tradeId:
                            type: integer
                            example: 1
                            format: int64
                            description: trade Id
                            x-description-cn: 成交ID
                          tradePrice:
                            type: number
                            example: 2.8
                            format: float
                            description: trade Price
                            x-description-cn: trade Price
                          tradeQty:
                            type: number
                            example: 1.2
                            format: float
                            description: trade Qty
                            x-description-cn: trade Qty
                          tradeTime:
                            type: integer
                            example: 1730170445600
                            format: int64
                            description: trade Time
                            x-description-cn: trade Time
                          liquidity:
                            type: string
                            example: TAKER
                            description: liquidity
                            x-description-cn: liquidity
                          commission:
                            type: number
                            example: 0.336
                            format: float
                            description: commission
                            x-description-cn: commission
                      description: legs
                      x-description-cn: legs
                    blockTradeSettlementKey:
                      type: string
                      example: 7d085e6e-a229-2335-ab9d-6a581febcd25
                      description: block Trade Settlement Key
                      x-description-cn: block Trade Settlement Key
  /eapi/v1/block/order/create:
    delete:
      summary: Cancel Block Trade Order (TRADE)
      x-summary-cn: 取消Block 交易 订单 (TRADE)
      description: Cancel a block trade order.
      x-description-cn: 取消a block 交易 订单.
      tags:
        - market-maker-block-trade
      operationId: cancelBlockTradeOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#cancel-block-trade-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/cancelBlockTradeOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/cancel_block_trade_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/cancel_block_trade_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/CancelBlockTradeOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/CancelBlockTradeOrder/CancelBlockTradeOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/CancelBlockTradeOrderExample.php
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
        - name: blockOrderMatchingKey
          in: query
          required: true
          schema:
            type: string
            example: 7d046e6e-a429-4335-ab9d-6a681febcde5
          description: Block trade matching key.
          x-description-cn: 大宗交易撮合键。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: OK
          x-description-cn: 成功
    put:
      summary: Extend Block Trade Order (TRADE)
      x-summary-cn: Extend Block 交易 订单 (TRADE)
      description: Extends a block trade expire time by 30 mins from the current time.
      x-description-cn: Extends a block 交易 expire 时间 by 30 mins 从 the 当前 时间.
      tags:
        - market-maker-block-trade
      operationId: extendBlockTradeOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#extend-block-trade-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/extendBlockTradeOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/extend_block_trade_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/extend_block_trade_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/ExtendBlockTradeOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/ExtendBlockTradeOrder/ExtendBlockTradeOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/ExtendBlockTradeOrderExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - blockOrderMatchingKey
                - timestamp
              properties:
                blockOrderMatchingKey:
                  type: string
                  example: 3668822b8-1baa-6a2f-adb8-d3de6289b361
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
          description: Extend Block Trade Order
          x-description-cn: Extend Block 交易 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  blockTradeSettlementKey:
                    type: string
                    example: 3668822b8-1baa-6a2f-adb8-d3de6289b361
                    description: block Trade Settlement Key
                    x-description-cn: block Trade Settlement Key
                  expireTime:
                    type: integer
                    example: 1730172007000
                    format: int64
                    description: expire Time
                    x-description-cn: expire Time
                  liquidity:
                    type: string
                    example: TAKER
                    description: liquidity
                    x-description-cn: liquidity
                  status:
                    type: string
                    example: RECEIVED
                    description: status
                    x-description-cn: 状态
                  createTime:
                    type: integer
                    example: 1730170088111
                    format: int64
                    description: create Time
                    x-description-cn: create Time
                  legs:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BNB-241101-700-C
                          description: symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: BUY
                          description: side
                          x-description-cn: 方向
                        quantity:
                          type: string
                          example: "1.2"
                          description: quantity
                          x-description-cn: 数量
                        price:
                          type: string
                          example: "2.8"
                          description: price
                          x-description-cn: 价格
                    description: legs
                    x-description-cn: legs
    post:
      summary: New Block Trade Order (TRADE)
      x-summary-cn: 新建大宗交易订单 (TRADE)
      description: Send in a new block trade order.
      x-description-cn: 提交新的大宗交易订单。
      tags:
        - market-maker-block-trade
      operationId: newBlockTradeOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#new-block-trade-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/newBlockTradeOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/new_block_trade_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/new_block_trade_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/NewBlockTradeOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/NewBlockTradeOrder/NewBlockTradeOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/NewBlockTradeOrderExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - liquidity
                - legs
                - timestamp
              properties:
                liquidity:
                  type: string
                  example: TAKER
                  enum:
                    - MAKER
                    - TAKER
                legs:
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
                        example: BTC-210115-35000-C
                        description: Option trading pair
                        x-description-cn: 期权交易对
                      side:
                        type: string
                        example: BUY
                        enum:
                          - BUY
                          - SELL
                        description: Buy/sell direction
                        x-description-cn: 买卖方向
                      type:
                        type: string
                        example: LIMIT
                        enum:
                          - LIMIT
                        description: Order type
                        x-description-cn: 订单类型
                      quantity:
                        type: string
                        example: "0.0002"
                        description: Order quantity
                        x-description-cn: 下单数量
                      price:
                        type: string
                        example: "100"
                        description: Order price
                        x-description-cn: 订单价格
                  description: >-
                    Max 1 (only single leg supported), list of legs parameters in JSON; example:
                    eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C",
                    "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]
                  x-description-cn: >-
                    最多1条（仅支持单腿），JSON格式的legs参数列表；例如：eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C",
                    "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]
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
          description: New Block Trade Order
          x-description-cn: 新建大宗交易订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  blockTradeSettlementKey:
                    type: string
                    example: 3668822b8-1baa-6a2f-adb8-d3de6289b361
                    description: block Trade Settlement Key
                    x-description-cn: 大宗交易结算键
                  expireTime:
                    type: integer
                    example: 1730171888109
                    format: int64
                    description: expire Time
                    x-description-cn: 过期时间
                  liquidity:
                    type: string
                    example: TAKER
                    description: liquidity
                    x-description-cn: 流动性方向
                  status:
                    type: string
                    example: RECEIVED
                    description: status
                    x-description-cn: 状态
                  legs:
                    type: array
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BNB-241101-700-C
                          description: symbol
                          x-description-cn: 交易对
                        side:
                          type: string
                          example: BUY
                          description: side
                          x-description-cn: 方向
                        quantity:
                          type: string
                          example: "1.2"
                          description: quantity
                          x-description-cn: 数量
                        price:
                          type: string
                          example: "2.8"
                          description: price
                          x-description-cn: 价格
                    description: legs
                    x-description-cn: 订单腿
  /eapi/v1/block/order/orders:
    get:
      summary: Query Block Trade Order (TRADE)
      x-summary-cn: 查询Block 交易 订单 (TRADE)
      description: Check block trade order status.
      x-description-cn: 检查block 交易 订单 状态.
      tags:
        - market-maker-block-trade
      operationId: queryBlockTradeOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-block-trade#query-block-trade-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerBlockTradeApi/queryBlockTradeOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_block_trade_api/query_block_trade_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerBlockTrade/query_block_trade_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerblocktrade/QueryBlockTradeOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerBlockTradeAPI/QueryBlockTradeOrder/QueryBlockTradeOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerblocktrade/QueryBlockTradeOrderExample.php
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
        - name: blockOrderMatchingKey
          in: query
          required: false
          schema:
            type: string
            example: 7d046e6e-a429-4335-ab9d-6a681febcde5
          description: If specified, returns the specific block trade associated with the blockOrderMatchingKey
          x-description-cn: If specified, returns the specific block 交易 associated 带 the block订单Matching Key
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: underlying
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            maximum: 60000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Block Trade Order
          x-description-cn: Block 交易 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    blockTradeSettlementKey:
                      type: string
                      example: 7d046e6e-a429-4335-ab9d-6a681febcde5
                      description: block Trade Settlement Key
                      x-description-cn: block Trade Settlement Key
                    expireTime:
                      type: integer
                      example: 1730172115801
                      format: int64
                      description: expire Time
                      x-description-cn: expire Time
                    liquidity:
                      type: string
                      example: TAKER
                      description: liquidity
                      x-description-cn: liquidity
                    status:
                      type: string
                      example: RECEIVED
                      description: status
                      x-description-cn: 状态
                    createTime:
                      type: integer
                      example: 1730170315803
                      format: int64
                      description: create Time
                      x-description-cn: create Time
                    legs:
                      type: array
                      items:
                        type: object
                        properties:
                          symbol:
                            type: string
                            example: BNB-241101-700-C
                            description: symbol
                            x-description-cn: 交易对
                          side:
                            type: string
                            example: BUY
                            description: side
                            x-description-cn: 方向
                          quantity:
                            type: string
                            example: "1.2"
                            description: quantity
                            x-description-cn: 数量
                          price:
                            type: string
                            example: "2.8"
                            description: price
                            x-description-cn: 价格
                      description: legs
                      x-description-cn: legs
  /eapi/v1/countdownCancelAllHeartBeat:
    post:
      summary: Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
      x-summary-cn: 重置倒计时取消所有订单心跳 (TRADE)
      description: >-
        This endpoint resets the time from which the countdown will begin to the time this messaged is received.  It
        should be called repeatedly as heartbeats.  Multiple heartbeats can be updated at once by specifying the
        underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.
      x-description-cn: 本接口用户更新倒计时取消所有订单心跳。本接口需要作为心跳更新被频繁调用。将多个标的资产以list形式传入`underlyings`可以同时更新多个标的资产的心跳。
      tags:
        - market-maker-endpoints
      operationId: autoCancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-endpoints#auto-cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerEndpointsApi/autoCancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_endpoints_api/auto_cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerEndpoints/auto_cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerendpoints/AutoCancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerEndpointsAPI/AutoCancelAllOpenOrders/AutoCancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerendpoints/AutoCancelAllOpenOrdersExample.php
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
      x-parameters-notes: "- The response will only include underlying symbols where the heartbeat has been successfully updated."
      x-parameters-notes-cn: "- 响应仅包含心跳已被更新的标的资产"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - underlyings
                - timestamp
              properties:
                underlyings:
                  type: string
                  example: BTCUSDT,ETHUSDT
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
          description: Auto-Cancel All Open Orders
          x-description-cn: Auto-取消All 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  underlyings:
                    type: array
                    items:
                      type: string
                      example: BTCUSDT
                    description: underlyings
                    x-description-cn: underlyings
  /eapi/v1/countdownCancelAll:
    get:
      summary: Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
      x-summary-cn: 获得倒计时自动取消所有订单配置 (TRADE)
      description: >-
        This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel
        parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the
        underlying symbol and corresponding countdownTime parameter will not be returned in the response.
      x-description-cn: 本接口用于获得倒计时自动取消所有订单配置。接口仅返回有效的自动取消参数，如果标的资产的`countdownTime`设置为0，该标的资产对应的参数不会被返回。
      tags:
        - market-maker-endpoints
      operationId: getAutoCancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-endpoints#get-auto-cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerEndpointsApi/getAutoCancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_endpoints_api/get_auto_cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerEndpoints/get_auto_cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerendpoints/GetAutoCancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerEndpointsAPI/GetAutoCancelAllOpenOrders/GetAutoCancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerendpoints/GetAutoCancelAllOpenOrdersExample.php
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
        - name: underlying
          in: query
          required: false
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
      x-parameters-notes: "- countdownTime = 0 means the function is disabled."
      x-parameters-notes-cn: "- 当countdownTime = 0时倒计时取消所有订单功能关闭"
      responses:
        "200":
          description: Get Auto-Cancel All Open Orders
          x-description-cn: 获取Auto-取消All 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  underlying:
                    type: string
                    example: ETHUSDT
                    description: underlying
                    x-description-cn: 标的资产
                  countdownTime:
                    type: integer
                    example: 100000
                    format: int64
                    description: countdown Time
                    x-description-cn: countdown Time
    post:
      summary: Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
      x-summary-cn: 设置倒计时取消所有订单配置 (TRADE)
      description: >-
        This endpoint sets the parameters of the auto-cancel feature which cancels all open orders (both market maker
        protection and non market maker protection order types) of the underlying symbol at the end of the specified
        countdown time period if no heartbeat message is sent.  After the countdown time period, all open orders will be
        cancelled. The auto-cancel feature can be turned off by setting countdownTime to 0.
      x-description-cn: >-
        此接口用于设置倒计时取消所有订单（包括做市商保护订单与普通订单）配置，即在倒计时结束前心跳没有更新，特定标的资产的所有订单会被取消。若倒计时结束前心跳没有更新，所有的订单将会被取消。可以通过设置`countdownTime`为0取消此功能。
      tags:
        - market-maker-endpoints
      operationId: setAutoCancelAllOpenOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-endpoints#set-auto-cancel-all-open-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerEndpointsApi/setAutoCancelAllOpenOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_endpoints_api/set_auto_cancel_all_open_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerEndpoints/set_auto_cancel_all_open_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerendpoints/SetAutoCancelAllOpenOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerEndpointsAPI/SetAutoCancelAllOpenOrders/SetAutoCancelAllOpenOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerendpoints/SetAutoCancelAllOpenOrdersExample.php
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
        - This rest endpoint sets up the parameters to cancel your open orders in case of an outage or disconnection.

        - Example usage: > Call this endpoint with a countdownTime value of 10000 (10 seconds) to turn on the
        auto-cancel feature. If the corresponding countdownCancelAllHeartBeat endpoint is not called within 10 seconds
        with the specified underlying symbol, all open orders of the specified symbol will be automatically canceled. If
        this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.

        - The system will check all countdowns approximately every 100 milliseconds, **please note that sufficient
        redundancy should be considered when using this function**. We do not recommend setting the countdown time to be
        too precise or too small.
      x-parameters-notes-cn: >-
        - 本接口用于配置网络中断情况下自动取消已有订单。

        - 使用样例：对特定的标的资产调用本接口（使用参数countdownTime =
        10000，10秒）打开自动取消所有订单功能。如果功能开启后任意10秒内没有对该标的资产调用`countdownCancelAllHeartBeat`接口，则该标的资产上所有订单被去取消。如果调用接口时传参countdownTime
        = 0，倒计时自动取消订单功能关闭。

        - 请注意，系统每隔100ms倒计时是否结束，**使用此功能时应考虑足够的时间冗余**。 我们不建议将倒计时时间设置得太精确或太小。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - underlying
                - countdownTime
                - timestamp
              properties:
                underlying:
                  type: string
                  example: BTCUSDT
                countdownTime:
                  type: integer
                  example: 5000
                  format: int64
                  description: >-
                    Countdown time in milliseconds (ex. 1,000 for 1 second). 0 to disable the timer. Negative values
                    (ex. -10000) are not accepted. Minimum acceptable value is 5,000
                  x-description-cn: 以毫秒计量倒计时长 (1000代表1秒)。 设为0时关闭倒计时。最小设为5000（负值无效）
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
          description: Set Auto-Cancel All Open Orders
          x-description-cn: Set Auto-取消All 未完成订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  underlying:
                    type: string
                    example: ETHUSDT
                    description: underlying
                    x-description-cn: 标的资产
                  countdownTime:
                    type: integer
                    example: 100000
                    format: int64
                    description: countdown Time
                    x-description-cn: countdown Time
  /eapi/v1/mmp:
    get:
      summary: Get Market Maker Protection Config (TRADE)
      x-summary-cn: 获取MMP规则 (TRADE)
      description: Get config for MMP.
      x-description-cn: 获取MMP参数
      tags:
        - market-maker-endpoints
      operationId: getMarketMakerProtectionConfig
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-endpoints#get-market-maker-protection-config
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerEndpointsApi/getMarketMakerProtectionConfig.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_endpoints_api/get_market_maker_protection_config.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerEndpoints/get_market_maker_protection_config.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerendpoints/GetMarketMakerProtectionConfigExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerEndpointsAPI/GetMarketMakerProtectionConfig/GetMarketMakerProtectionConfig.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerendpoints/GetMarketMakerProtectionConfigExample.php
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
        - name: underlying
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Get Market Maker Protection Config
          x-description-cn: 获取MMP规则
          content:
            application/json:
              schema:
                type: object
                properties:
                  underlyingId:
                    type: integer
                    example: 2
                    format: int64
                    description: underlying Id
                    x-description-cn: 标的资产ID
                  underlying:
                    type: string
                    example: BTCUSDT
                    description: underlying
                    x-description-cn: 标的资产
                  windowTimeInMilliseconds:
                    type: integer
                    example: 3000
                    format: int64
                    description: window Time In Milliseconds
                    x-description-cn: 监控时间窗口（毫秒）
                  frozenTimeInMilliseconds:
                    type: integer
                    example: 300000
                    format: int64
                    description: frozen Time In Milliseconds
                    x-description-cn: 冻结时间（毫秒）
                  qtyLimit:
                    type: string
                    example: "2"
                    description: qty Limit
                    x-description-cn: 数量限制
                  deltaLimit:
                    type: string
                    example: "2.3"
                    description: delta Limit
                    x-description-cn: 净Delta限制
                  lastTriggerTime:
                    type: integer
                    example: 0
                    format: int64
                    description: last Trigger Time
                    x-description-cn: 最近触发时间
  /eapi/v1/mmpReset:
    post:
      summary: Reset Market Maker Protection Config (TRADE)
      x-summary-cn: 重置MMP状态 (TRADE)
      description: Reset MMP, start MMP order again.
      x-description-cn: MMP冻结后重置MMP，重新开启MMP下单
      tags:
        - market-maker-endpoints
      operationId: resetMarketMakerProtectionConfig
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-endpoints#reset-market-maker-protection-config
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerEndpointsApi/resetMarketMakerProtectionConfig.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_endpoints_api/reset_market_maker_protection_config.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerEndpoints/reset_market_maker_protection_config.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerendpoints/ResetMarketMakerProtectionConfigExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerEndpointsAPI/ResetMarketMakerProtectionConfig/ResetMarketMakerProtectionConfig.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerendpoints/ResetMarketMakerProtectionConfigExample.php
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
                - underlying
                - timestamp
              properties:
                underlying:
                  type: string
                  example: BTCUSDT
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
          description: Reset Market Maker Protection Config
          x-description-cn: 重置MMP状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  underlyingId:
                    type: integer
                    example: 2
                    format: int64
                    description: underlying Id
                    x-description-cn: 标的资产ID
                  underlying:
                    type: string
                    example: BTCUSDT
                    description: underlying
                    x-description-cn: 标的资产
                  windowTimeInMilliseconds:
                    type: integer
                    example: 3000
                    format: int64
                    description: window Time In Milliseconds
                    x-description-cn: 监控时间窗口（毫秒）
                  frozenTimeInMilliseconds:
                    type: integer
                    example: 300000
                    format: int64
                    description: frozen Time In Milliseconds
                    x-description-cn: 冻结时间（毫秒）
                  qtyLimit:
                    type: string
                    example: "2"
                    description: qty Limit
                    x-description-cn: 数量限制
                  deltaLimit:
                    type: string
                    example: "2.3"
                    description: delta Limit
                    x-description-cn: 净Delta限制
                  lastTriggerTime:
                    type: integer
                    example: 0
                    format: int64
                    description: last Trigger Time
                    x-description-cn: 最近触发时间
  /eapi/v1/mmpSet:
    post:
      summary: Set Market Maker Protection Config (TRADE)
      x-summary-cn: 设置MMP规则 (TRADE)
      description: >-
        Set config for MMP. Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this
        mechanism is able to prevent mass trading in short period time. Once market maker's account branches the
        threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current
        MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate
        market and modify order price.
      x-description-cn: >-
        设置MMP参数。 做市商保护(Market Maker Protection)
        是一种为期权做市商设计的保护机制，该机制能够防止做市商的订单在短时间大量成交。一旦某个账户在短时间内的总交易额超过了配置的限额，该账户的做市商保护将被触发。当做市商保护被触发时，账户现有的做市商保护订单（被标记为做市商保护的订单）将被撮合自动取消，而该账户新的做市商保护订单将在冻结期被拒绝。用户可以利用这段时间重新评估行情并修改报价。
      tags:
        - market-maker-endpoints
      operationId: setMarketMakerProtectionConfig
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/market-maker-endpoints#set-market-maker-protection-config
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/MarketMakerEndpointsApi/setMarketMakerProtectionConfig.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/market_maker_endpoints_api/set_market_maker_protection_config.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/MarketMakerEndpoints/set_market_maker_protection_config.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/marketmakerendpoints/SetMarketMakerProtectionConfigExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/MarketMakerEndpointsAPI/SetMarketMakerProtectionConfig/SetMarketMakerProtectionConfig.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/marketmakerendpoints/SetMarketMakerProtectionConfigExample.php
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
                - underlying
                - windowTimeInMilliseconds
                - frozenTimeInMilliseconds
                - qtyLimit
                - deltaLimit
                - timestamp
              properties:
                underlying:
                  type: string
                  example: BTCUSDT
                windowTimeInMilliseconds:
                  type: integer
                  example: 1000
                  minimum: 0
                  maximum: 5000
                  format: int64
                  description: MMP Interval in milliseconds
                  x-description-cn: MMP监控时间窗口（毫秒）
                frozenTimeInMilliseconds:
                  type: integer
                  example: 1000
                  format: int64
                  description: MMP frozen time in milliseconds, if set to 0 manual reset is required
                  x-description-cn: MMP冻结时间（毫秒），设置为0后代表账号为冻结状态，需要手动重置
                qtyLimit:
                  type: number
                  example: "1.0"
                  format: float
                  description: quantity limit
                  x-description-cn: 数量限制
                deltaLimit:
                  type: number
                  example: "1.0"
                  format: float
                  description: net delta limit
                  x-description-cn: 净delta限制
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
          description: Set Market Maker Protection Config
          x-description-cn: 设置MMP规则
          content:
            application/json:
              schema:
                type: object
                properties:
                  underlyingId:
                    type: integer
                    example: 2
                    format: int64
                    description: underlying Id
                    x-description-cn: 标的资产ID
                  underlying:
                    type: string
                    example: BTCUSDT
                    description: underlying
                    x-description-cn: 标的资产
                  windowTimeInMilliseconds:
                    type: integer
                    example: 3000
                    format: int64
                    description: window Time In Milliseconds
                    x-description-cn: 监控时间窗口（毫秒）
                  frozenTimeInMilliseconds:
                    type: integer
                    example: 300000
                    format: int64
                    description: frozen Time In Milliseconds
                    x-description-cn: 冻结时间（毫秒）
                  qtyLimit:
                    type: string
                    example: "2"
                    description: qty Limit
                    x-description-cn: 数量限制
                  deltaLimit:
                    type: string
                    example: "2.3"
                    description: delta Limit
                    x-description-cn: 净Delta限制
                  lastTriggerTime:
                    type: integer
                    example: 0
                    format: int64
                    description: last Trigger Time
                    x-description-cn: 最近触发时间
  /eapi/v1/userTrades:
    get:
      summary: Account Trade List (USER_DATA)
      x-summary-cn: 账户成交历史 (USER_DATA)
      description: >-
        Get trades for a specific account and symbol. Only supports querying trades in the past 3 months; a
        `startTime`/`endTime` outside that window returns `-6073 SEARCH_WINDOW_RESTRICTED`.
      x-description-cn: 查询账户成交历史。仅支持查询最近3个月的成交记录，`startTime`/`endTime` 超出该范围将返回 `-6073 SEARCH_WINDOW_RESTRICTED`。
      tags:
        - trade
      operationId: accountTradeList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#account-trade-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/accountTradeList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/account_trade_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/account_trade_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/AccountTradeListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/AccountTradeList/AccountTradeList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/AccountTradeListExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: fromId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376
          x-description-cn: 返回该fromId及之后的成交，缺省返回最近的成交
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 1000
            format: int64
          description: Number of result sets returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Account Trade List
          x-description-cn: 账户 交易 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 4611875134427365000
                      format: int64
                      description: unique id
                      x-description-cn: ID
                    tradeId:
                      type: integer
                      example: 239
                      format: int64
                      description: trade id
                      x-description-cn: 交易id
                    orderId:
                      type: integer
                      example: 4611875134427365000
                      format: int64
                      description: order id
                      x-description-cn: 订单id
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: option symbol
                      x-description-cn: 交易对
                    price:
                      type: string
                      example: "100"
                      description: trade price
                      x-description-cn: 成交价
                    quantity:
                      type: string
                      example: "1"
                      description: trade quantity
                      x-description-cn: 成交量
                    fee:
                      type: string
                      example: "-1.04378629"
                      description: fee(negative is fee deduction)
                      x-description-cn: 手续费（负数为扣费）
                    realizedProfit:
                      type: string
                      example: "0.00000000"
                      description: realized profit/loss
                      x-description-cn: 已实现盈亏
                    side:
                      type: string
                      example: BUY
                      description: order side
                      x-description-cn: 订单方向
                    type:
                      type: string
                      example: LIMIT
                      description: order type
                      x-description-cn: 订单类型
                    liquidity:
                      type: string
                      example: TAKER
                      description: TAKER or MAKER
                      x-description-cn: TAKER or MAKER
                    time:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: trade time
                      x-description-cn: 交易时间
                    priceScale:
                      type: integer
                      example: 2
                      format: int64
                      description: price Scale
                      x-description-cn: 价格精度
                    quantityScale:
                      type: integer
                      example: 2
                      format: int64
                      description: quantity Scale
                      x-description-cn: 数量精度
                    optionSide:
                      type: string
                      example: CALL
                      description: option Side
                      x-description-cn: 期权种类
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote Asset
                      x-description-cn: 报价资产
  /eapi/v1/allOpenOrdersByUnderlying:
    delete:
      summary: Cancel All Option Orders By Underlying (TRADE)
      x-summary-cn: 撤销特定标的全部订单 (TRADE)
      description: Cancel all active orders on specified underlying.
      x-description-cn: 撤销特定标的全部订单
      tags:
        - trade
      operationId: cancelAllOptionOrdersByUnderlying
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#cancel-all-option-orders-by-underlying
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/cancelAllOptionOrdersByUnderlying.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/cancel_all_option_orders_by_underlying.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/cancel_all_option_orders_by_underlying.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/CancelAllOptionOrdersByUnderlyingExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/CancelAllOptionOrdersByUnderlying/CancelAllOptionOrdersByUnderlying.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/CancelAllOptionOrdersByUnderlyingExample.php
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
        - name: underlying
          in: query
          required: true
          schema:
            type: string
            example: BTCUSDT
          description: Underlying asset.
          x-description-cn: 标的资产。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Cancel All Option Orders By Underlying
          x-description-cn: 取消All Option 订单 By Underlying
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 0
                    format: int64
                    description: code
                    x-description-cn: code
                  msg:
                    type: string
                    example: success
                    description: msg
                    x-description-cn: msg
  /eapi/v1/allOpenOrders:
    delete:
      summary: Cancel all Option orders on specific symbol (TRADE)
      x-summary-cn: 撤销单交易对全部订单 (TRADE)
      description: Cancel all active order on a symbol.
      x-description-cn: 撤销单交易对全部订单
      tags:
        - trade
      operationId: cancelAllOptionOrdersOnSpecificSymbol
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#cancel-all-option-orders-on-specific-symbol
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/cancelAllOptionOrdersOnSpecificSymbol.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/cancel_all_option_orders_on_specific_symbol.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/cancel_all_option_orders_on_specific_symbol.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/CancelAllOptionOrdersOnSpecificSymbolExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/CancelAllOptionOrdersOnSpecificSymbol/CancelAllOptionOrdersOnSpecificSymbol.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/CancelAllOptionOrdersOnSpecificSymbolExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Cancel all Option orders on specific symbol
          x-description-cn: 取消all Option 订单 on specific 交易对
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "0"
                    description: code
                    x-description-cn: code
                  msg:
                    type: string
                    example: success
                    description: msg
                    x-description-cn: msg
  /eapi/v1/batchOrders:
    delete:
      summary: Cancel Multiple Option Orders (TRADE)
      x-summary-cn: 批量撤销订单 (TRADE)
      description: Cancel multiple orders.
      x-description-cn: 批量撤销订单。
      tags:
        - trade
      operationId: cancelMultipleOptionOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#cancel-multiple-option-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/cancelMultipleOptionOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/cancel_multiple_option_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/cancel_multiple_option_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/CancelMultipleOptionOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/CancelMultipleOptionOrders/CancelMultipleOptionOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/CancelMultipleOptionOrdersExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: orderIds
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
              format: int64
              example: 4611875134427365000
          description: Order ID list.
          x-description-cn: 订单 ID 列表。
        - name: clientOrderIds
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
              example: my_id_1
          description: Client order ID list.
          x-description-cn: 客户端订单 ID 列表。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
      x-parameters-notes: "- At least one instance of `orderId` and `clientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderIds` 与 `clientOrderIds` 必须至少发送一个，不可同时发送"
      responses:
        "200":
          description: Cancel Multiple Option Orders
          x-description-cn: 取消Multiple Option 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 4611875134427365000
                      format: int64
                      description: System order number
                      x-description-cn: 订单Id
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: Option trading pair
                      x-description-cn: 交易对
                    price:
                      type: string
                      example: "100"
                      description: Order Price
                      x-description-cn: 订单价格
                    quantity:
                      type: string
                      example: "1"
                      description: Order Quantity
                      x-description-cn: 订单数量
                    executedQty:
                      type: string
                      example: "0"
                      description: Number of completed quantity
                      x-description-cn: 已经成交数量
                    fee:
                      type: string
                      example: "0"
                      description: fee
                      x-description-cn: 手续费
                    side:
                      type: string
                      example: BUY
                      description: Buy/sell direction
                      x-description-cn: 订单方向
                    type:
                      type: string
                      example: LIMIT
                      description: Order type
                      x-description-cn: 订单类型
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time in force method
                      x-description-cn: 有效时间
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Order is reduce only Y/N
                      x-description-cn: 仅减仓
                    createTime:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: Order Time
                      x-description-cn: 订单创建时间
                    updateTime:
                      type: integer
                      example: 1566818724722
                      format: int64
                      description: Update time
                      x-description-cn: 订单更新时间
                    status:
                      type: string
                      example: ACCEPTED
                      description: Order status
                      x-description-cn: 订单类型
                    avgPrice:
                      type: string
                      example: "0"
                      description: Average price of completed trade
                      x-description-cn: 平均成交价
                    clientOrderId:
                      type: string
                      example: ""
                      description: Client order ID
                      x-description-cn: 用户自定义的订单号
                    priceScale:
                      type: integer
                      example: 3
                      format: int64
                      description: price Scale
                      x-description-cn: price Scale
                    quantityScale:
                      type: integer
                      example: 4
                      format: int64
                      description: quantity Scale
                      x-description-cn: quantity Scale
                    optionSide:
                      type: string
                      example: CALL
                      description: option Side
                      x-description-cn: option Side
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote Asset
                      x-description-cn: 报价资产
                    mmp:
                      type: boolean
                      example: false
                      description: mmp
                      x-description-cn: mmp
                    source:
                      type: string
                      example: API
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading prevention mode
                      x-description-cn: 订单自成交保护模式
    post:
      summary: Place Multiple Orders (TRADE)
      x-summary-cn: 批量下单 (TRADE)
      description: Send multiple option orders.
      x-description-cn: 批量下单。
      tags:
        - trade
      operationId: placeMultipleOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#place-multiple-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/placeMultipleOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/place_multiple_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/place_multiple_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/PlaceMultipleOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/PlaceMultipleOrders/PlaceMultipleOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/PlaceMultipleOrdersExample.php
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
        Some parameters are mandatory depending on the order type as follows:

        Type | Mandatory parameters
        ------------ | ------------ 
        LIMIT | timeInForce, quantity, price

        - Parameter rules are same with New Order
        - Batch orders are processed concurrently, and the order of matching is not guaranteed.
      x-parameters-notes-cn: |-
        某些参数根据订单类型的不同而不同，具体如下：

        类型 | 必填参数
        ------------ | ------------ 
        LIMIT | timeInForce, quantity, price

        - 参数规则同 New Order
        - 批量订单并发处理，撮合顺序不保证。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - orders
                - timestamp
              properties:
                orders:
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
                        example: BTC-200730-9000-C
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
                      quantity:
                        type: number
                        example: "1.0"
                        format: float
                        description: Order Quantity
                        x-description-cn: 下单数量
                      price:
                        type: number
                        example: "1.0"
                        format: float
                        description: Order Price
                        x-description-cn: 订单价格
                      timeInForce:
                        type: string
                        example: GTC
                        default: GTC
                        enum:
                          - GTC
                          - IOC
                          - FOK
                          - GTX
                      reduceOnly:
                        type: boolean
                        example: false
                        default: false
                      postOnly:
                        type: boolean
                        example: false
                        default: false
                      newOrderRespType:
                        type: string
                        example: ACK
                        default: ACK
                        enum:
                          - ACK
                          - RESULT
                      clientOrderId:
                        type: string
                        example: "1"
                        description: User-defined order ID cannot be repeated in pending orders
                        x-description-cn: 用户自定义订单 ID，不可与挂单中的其他订单重复
                      isMmp:
                        type: boolean
                        example: true
                        description: is market maker protection order
                        x-description-cn: 是否为做市商保护订单
                      selfTradePreventionMode:
                        type: string
                        example: NONE
                        default: EXPIRE_MAKER
                        enum:
                          - EXPIRE_TAKER
                          - EXPIRE_MAKER
                          - EXPIRE_BOTH
                        description: >-
                          EXPIRE_TAKER: expire taker order when STP triggers/ EXPIRE_MAKER: expire maker order when STP
                          triggers/ EXPIRE_BOTH: expire both orders when STP triggers; Default EXPIRE_MAKER
                        x-description-cn: >-
                          EXPIRE_TAKER: STP触发时，取消吃单订单/ EXPIRE_MAKER: STP触发时，取消挂单订单/ EXPIRE_BOTH: STP触发时，取消吃单和挂单订单; 默认
                          EXPIRE_MAKER
                  description: order list. Max 10 orders
                  x-description-cn: 订单列表，最多支持10个订单
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
          description: Place Multiple Orders
          x-description-cn: 批量下单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 4611875134427365000
                      format: int64
                      description: System order number
                      x-description-cn: 订单Id
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: Option trading pair
                      x-description-cn: 交易对
                    price:
                      type: string
                      example: "100"
                      description: Order Price
                      x-description-cn: 订单价格
                    quantity:
                      type: string
                      example: "1"
                      description: Order Quantity
                      x-description-cn: 订单数量
                    executedQty:
                      type: string
                      example: "0"
                      description: Number of executed quantity
                      x-description-cn: 执行数量
                    fee:
                      type: integer
                      example: 0
                      format: int64
                      description: fee
                      x-description-cn: 手续费
                    side:
                      type: string
                      example: BUY
                      description: Buy/sell direction
                      x-description-cn: 订单方向
                    type:
                      type: string
                      example: LIMIT
                      description: Order type
                      x-description-cn: 订单类型
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time in force method
                      x-description-cn: 有效时间
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Order is reduce only Y/N
                      x-description-cn: 仅减仓
                    postOnly:
                      type: boolean
                      example: false
                      description: post Only
                      x-description-cn: 仅做maker
                    createTime:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: Order Time
                      x-description-cn: 订单创建时间
                    updateTime:
                      type: integer
                      example: 1566818724722
                      format: int64
                      description: Update time
                      x-description-cn: 订单更新时间
                    status:
                      type: string
                      example: NEW
                      description: Order status
                      x-description-cn: 订单状态
                    avgPrice:
                      type: string
                      example: "0"
                      description: Average price of completed trade
                      x-description-cn: 平均价格
                    clientOrderId:
                      type: string
                      example: ""
                      description: Client order ID
                      x-description-cn: 用户自定义订单Id
                    priceScale:
                      type: integer
                      example: 2
                      format: int64
                      description: price Scale
                      x-description-cn: 价格精度
                    quantityScale:
                      type: integer
                      example: 2
                      format: int64
                      description: quantity Scale
                      x-description-cn: 数量精度
                    optionSide:
                      type: string
                      example: CALL
                      description: option Side
                      x-description-cn: 期权类型
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote Asset
                      x-description-cn: 报价资产
                    mmp:
                      type: boolean
                      example: false
                      description: mmp
                      x-description-cn: 是否为MMP单
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading prevention mode
                      x-description-cn: 订单自成交保护模式
                    source:
                      type: string
                      example: API
  /eapi/v1/order:
    delete:
      summary: Cancel Option Order (TRADE)
      x-summary-cn: 撤销订单 (TRADE)
      description: Cancel an active order.
      x-description-cn: 撤销订单。
      tags:
        - trade
      operationId: cancelOptionOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#cancel-option-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/cancelOptionOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/cancel_option_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/cancel_option_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/CancelOptionOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/CancelOptionOrder/CancelOptionOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/CancelOptionOrderExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 4611875134427365000
            format: int64
          description: Order ID.
          x-description-cn: 订单 ID。
        - name: clientOrderId
          in: query
          required: false
          schema:
            type: string
            example: "10000"
          description: clientOrderId
          x-description-cn: clientOrderId
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
      x-parameters-notes: "- At least one instance of `orderId` and `clientOrderId` must be sent."
      x-parameters-notes-cn: "- `orderId` 与 `origClientOrderId` 必须至少发送一个"
      responses:
        "200":
          description: Cancel Option Order
          x-description-cn: 取消Option 订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 4611875134427365000
                    format: int64
                    description: System order number
                    x-description-cn: 订单ID
                  symbol:
                    type: string
                    example: BTC-200730-9000-C
                    description: Option trading pair
                    x-description-cn: 交易对
                  price:
                    type: string
                    example: "100"
                    description: Order Price
                    x-description-cn: 价格
                  quantity:
                    type: string
                    example: "1"
                    description: Order Quantity
                    x-description-cn: 数量
                  executedQty:
                    type: string
                    example: "0"
                    description: Number of executed quantity
                    x-description-cn: Number of executed quantity
                  side:
                    type: string
                    example: BUY
                    description: Buy/sell direction
                    x-description-cn: 方向
                  type:
                    type: string
                    example: LIMIT
                    description: Order type
                    x-description-cn: 类型
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force method
                    x-description-cn: Time in force method
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Order is reduce only Y/N
                    x-description-cn: 仅减仓
                  createDate:
                    type: integer
                    example: 1592465880683
                    format: int64
                    description: Order Time
                    x-description-cn: 创建时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: Update time
                    x-description-cn: 更新时间
                  status:
                    type: string
                    example: ACCEPTED
                    description: Order status
                    x-description-cn: 状态
                  avgPrice:
                    type: string
                    example: "0"
                    description: Average price of completed trade
                    x-description-cn: Average price of completed trade
                  source:
                    type: string
                    example: API
                    description: source
                    x-description-cn: source
                  clientOrderId:
                    type: string
                    example: ""
                    description: Client order ID
                    x-description-cn: 客户端订单ID
                  priceScale:
                    type: integer
                    example: 4
                    format: int64
                    description: price Scale
                    x-description-cn: price Scale
                  quantityScale:
                    type: integer
                    example: 4
                    format: int64
                    description: quantity Scale
                    x-description-cn: quantity Scale
                  optionSide:
                    type: string
                    example: CALL
                    description: option Side
                    x-description-cn: option Side
                  quoteAsset:
                    type: string
                    example: USDT
                    description: quote Asset
                    x-description-cn: 报价资产
                  mmp:
                    type: boolean
                    example: false
                    description: mmp
                    x-description-cn: mmp
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: self trading prevention mode
                    x-description-cn: 订单自成交保护模式
    post:
      summary: New Order (TRADE)
      x-summary-cn: 下单 (TRADE)
      description: Send a new order.
      x-description-cn: 下单
      tags:
        - trade
      operationId: newOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#new-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/newOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/new_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/new_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/NewOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/NewOrder/NewOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/NewOrderExample.php
      x-ip-weight: 0
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
        Some parameters are mandatory depending on the order type as follows:

        Type | Mandatory parameters
        ------------ | ------------ 
        LIMIT | timeInForce, quantity, price
      x-parameters-notes-cn: |-
        某些参数根据订单类型的不同而不同，具体如下：

        类型 | 必填参数
        ------------ | ------------ 
        LIMIT | timeInForce, quantity, price
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
                  example: BTC-200730-9000-C
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
                quantity:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order Quantity
                  x-description-cn: 下单数量
                price:
                  type: number
                  example: "1.0"
                  format: float
                  description: Order Price
                  x-description-cn: 订单价格
                timeInForce:
                  type: string
                  example: GTC
                  default: GTC
                  enum:
                    - GTC
                    - IOC
                    - FOK
                    - GTX
                reduceOnly:
                  type: boolean
                  example: false
                  default: false
                postOnly:
                  type: boolean
                  example: false
                  default: false
                newOrderRespType:
                  type: string
                  example: ACK
                  default: ACK
                  enum:
                    - ACK
                    - RESULT
                clientOrderId:
                  type: string
                  example: "1"
                  description: User-defined order ID cannot be repeated in pending orders
                  x-description-cn: 用户自定义订单 ID，不可与挂单中的其他订单重复
                isMmp:
                  type: boolean
                  example: true
                  description: is market maker protection order
                  x-description-cn: 是否为做市商保护订单
                selfTradePreventionMode:
                  type: string
                  example: NONE
                  enum:
                    - NONE
                    - EXPIRE_TAKER
                    - EXPIRE_MAKER
                    - EXPIRE_BOTH
                  description: Self-trade prevention mode
                  x-description-cn: 自我交易预防模式
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
          x-description-cn: 新订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 4611875134427365000
                    format: int64
                    description: System order number
                    x-description-cn: 订单Id
                  symbol:
                    type: string
                    example: BTC-200730-9000-C
                    description: Option trading pair
                    x-description-cn: 交易对
                  price:
                    type: string
                    example: "100"
                    description: Order Price
                    x-description-cn: 订单价格
                  quantity:
                    type: string
                    example: "1"
                    description: Order Quantity
                    x-description-cn: 订单数量
                  executedQty:
                    type: string
                    example: "0"
                    description: Number of executed quantity
                    x-description-cn: 执行数量
                  fee:
                    type: integer
                    example: 0
                    format: int64
                    description: fee
                    x-description-cn: 手续费
                  side:
                    type: string
                    example: BUY
                    description: Buy/sell direction
                    x-description-cn: 订单方向
                  type:
                    type: string
                    example: LIMIT
                    description: Order type
                    x-description-cn: 订单类型
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force method
                    x-description-cn: 有效时间
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Order is reduce only Y/N
                    x-description-cn: 仅减仓
                  postOnly:
                    type: boolean
                    example: false
                    description: post Only
                    x-description-cn: 仅做maker
                  createTime:
                    type: integer
                    example: 1592465880683
                    format: int64
                    description: Order Time
                    x-description-cn: 订单创建时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: Update time
                    x-description-cn: 订单更新时间
                  status:
                    type: string
                    example: NEW
                    description: Order status
                    x-description-cn: 订单状态
                  avgPrice:
                    type: string
                    example: "0"
                    description: Average price of completed trade
                    x-description-cn: 平均价格
                  source:
                    type: string
                    example: API
                    description: source
                    x-description-cn: 订单来源
                  clientOrderId:
                    type: string
                    example: ""
                    description: Client order ID
                    x-description-cn: 用户自定义订单Id
                  priceScale:
                    type: integer
                    example: 2
                    format: int64
                    description: price Scale
                    x-description-cn: 价格精度
                  quantityScale:
                    type: integer
                    example: 2
                    format: int64
                    description: quantity Scale
                    x-description-cn: 数量精度
                  optionSide:
                    type: string
                    example: CALL
                    description: option Side
                    x-description-cn: 期权类型
                  quoteAsset:
                    type: string
                    example: USDT
                    description: quote Asset
                    x-description-cn: 报价资产
                  mmp:
                    type: boolean
                    example: false
                    description: mmp
                    x-description-cn: 是否为MMP单
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: Self-trade prevention mode
                    x-description-cn: 自我交易预防模式
    get:
      summary: Query Single Order (TRADE)
      x-summary-cn: 查询单个订单 (TRADE)
      description: |-
        Check an order status.

        * These orders will not be found:
          * order status is `CANCELED` or `REJECTED`, **AND**
          * order has NO filled trade, **AND**
          * created time + 3 days < current time
      x-description-cn: |-
        查询订单状态。

        * 以下订单无法找到:
          * 订单状态为 `CANCELED` or `REJECTED`， **AND**
          * 订单没有成交记录， **AND**
          * 订单生成时间 + 3天 < 当前时间
      tags:
        - trade
      operationId: querySingleOrder
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#query-single-order
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/querySingleOrder.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/query_single_order.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/query_single_order.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/QuerySingleOrderExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/QuerySingleOrder/QuerySingleOrder.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/QuerySingleOrderExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 4611875134427365000
            format: int64
          description: Order ID.
          x-description-cn: 订单 ID。
        - name: clientOrderId
          in: query
          required: false
          schema:
            type: string
            example: abc123
          description: User-defined order ID; cannot be duplicated among open orders.
          x-description-cn: 用户自定义订单 ID；在挂单中不可重复。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
      x-parameters-notes: "- Either `orderId` or `clientOrderId ` must be sent."
      x-parameters-notes-cn: "- 至少需要发送 `orderId` 或 `clientOrderId`"
      responses:
        "200":
          description: Single Order
          x-description-cn: 单个订单
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: integer
                    example: 4611875134427365000
                    format: int64
                    description: System order id
                    x-description-cn: 订单号
                  symbol:
                    type: string
                    example: BTC-200730-9000-C
                    description: Option trading pair
                    x-description-cn: 交易对
                  price:
                    type: string
                    example: "100"
                    description: Order Price
                    x-description-cn: 订单价格
                  quantity:
                    type: string
                    example: "1"
                    description: Order Quantity
                    x-description-cn: 订单数量
                  executedQty:
                    type: string
                    example: "0"
                    description: Number of executed quantity
                    x-description-cn: 执行数量
                  side:
                    type: string
                    example: BUY
                    description: Buy/sell direction
                    x-description-cn: 订单方向
                  type:
                    type: string
                    example: LIMIT
                    description: Order type
                    x-description-cn: 订单类型
                  timeInForce:
                    type: string
                    example: GTC
                    description: Time in force method
                    x-description-cn: 有效时间
                  reduceOnly:
                    type: boolean
                    example: false
                    description: Order is reduce only Y/N
                    x-description-cn: 仅减仓
                  postOnly:
                    type: boolean
                    example: false
                    description: post Only
                    x-description-cn: 仅做maker
                  createTime:
                    type: integer
                    example: 1592465880683
                    format: int64
                    description: Order Time
                    x-description-cn: 下单时间
                  updateTime:
                    type: integer
                    example: 1566818724722
                    format: int64
                    description: Update time
                    x-description-cn: 更新时间
                  status:
                    type: string
                    example: NEW
                    description: Order status
                    x-description-cn: 订单状态
                  avgPrice:
                    type: string
                    example: "0"
                    description: Average price of completed trade
                    x-description-cn: 成交均价
                  clientOrderId:
                    type: string
                    example: ""
                    description: Client order ID
                    x-description-cn: 自定义id
                  priceScale:
                    type: integer
                    example: 2
                    format: int64
                    description: price Scale
                    x-description-cn: 价格精度
                  quantityScale:
                    type: integer
                    example: 2
                    format: int64
                    description: quantity Scale
                    x-description-cn: 数量精度
                  optionSide:
                    type: string
                    example: CALL
                    description: option Side
                    x-description-cn: 期权类型
                  quoteAsset:
                    type: string
                    example: USDT
                    description: quote Asset
                    x-description-cn: 报价资产
                  mmp:
                    type: boolean
                    example: false
                    description: mmp
                    x-description-cn: mmp
                  selfTradePreventionMode:
                    type: string
                    example: EXPIRE_MAKER
                    description: Self trade prevention mode.
                    x-description-cn: 订单自成交保护模式。
  /eapi/v1/position:
    get:
      summary: Option Position Information (USER_DATA)
      x-summary-cn: 仓位信息 (USER_DATA)
      description: Get current position information.
      x-description-cn: 获取仓位信息
      tags:
        - trade
      operationId: optionPositionInformation
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#option-position-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/optionPositionInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/option_position_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/option_position_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/OptionPositionInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/OptionPositionInformation/OptionPositionInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/OptionPositionInformationExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Option Position Information
          x-description-cn: Option 持仓 信息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    entryPrice:
                      type: string
                      example: "1000"
                      description: Average entry price
                      x-description-cn: Average entry price
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: Option trading pair
                      x-description-cn: 交易对
                    side:
                      type: string
                      example: SHORT
                      description: Position direction
                      x-description-cn: 方向
                    quantity:
                      type: string
                      example: "-0.1"
                      description: >-
                        Number of positions (positive numbers represent long positions, negative number represent short
                        positions)
                      x-description-cn: 数量
                    markValue:
                      type: string
                      example: "105.00138"
                      description: Current market value
                      x-description-cn: Current market value
                    unrealizedPNL:
                      type: string
                      example: "-5.00138"
                      description: Unrealized profit/loss
                      x-description-cn: 未实现盈亏
                    markPrice:
                      type: string
                      example: "1050.0138"
                      description: Mark price
                      x-description-cn: 标记价格
                    strikePrice:
                      type: string
                      example: "9000"
                      description: Strike price
                      x-description-cn: 行权价
                    expiryDate:
                      type: integer
                      example: 1593511200000
                      format: int64
                      description: Exercise time
                      x-description-cn: 到期时间
                    priceScale:
                      type: integer
                      example: 2
                      format: int64
                      description: price Scale
                      x-description-cn: price Scale
                    quantityScale:
                      type: integer
                      example: 2
                      format: int64
                      description: quantity Scale
                      x-description-cn: quantity Scale
                    optionSide:
                      type: string
                      example: CALL
                      description: option type
                      x-description-cn: option type
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote asset
                      x-description-cn: 报价资产
                    time:
                      type: integer
                      example: 1762872654561
                      format: int64
                      description: last update time
                      x-description-cn: 时间
                    bidQuantity:
                      type: string
                      example: "0.0000"
                      description: buy order qty
                      x-description-cn: buy order qty
                    askQuantity:
                      type: string
                      example: "0.0000"
                      description: sell order qty
                      x-description-cn: sell order qty
  /eapi/v1/openOrders:
    get:
      summary: Query Current Open Option Orders (USER_DATA)
      x-summary-cn: 查询当前挂单 (USER_DATA)
      description: "Query current all open orders, status: ACCEPTED PARTIALLY_FILLED"
      x-description-cn: 查询当前挂单（包含状态为ACCEPTED/ PARTIALLY_FILLED的订单）
      tags:
        - trade
      operationId: queryCurrentOpenOptionOrders
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#query-current-open-option-orders
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/queryCurrentOpenOptionOrders.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/query_current_open_option_orders.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/query_current_open_option_orders.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/QueryCurrentOpenOptionOrdersExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/QueryCurrentOpenOptionOrders/QueryCurrentOpenOptionOrders.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/QueryCurrentOpenOptionOrdersExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-weight: 1 for a single symbol; 40 when the symbol parameter is omitted
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 4611875134427365000
            format: int64
          description: Order ID.
          x-description-cn: 订单 ID。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Current Open Option Orders
          x-description-cn: 当前 未完成Option 订单
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 4611875134427365000
                      format: int64
                      description: System order number
                      x-description-cn: 订单Id
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: Option trading pair
                      x-description-cn: 交易对
                    price:
                      type: string
                      example: "100"
                      description: Order Price
                      x-description-cn: 订单价格
                    quantity:
                      type: string
                      example: "1"
                      description: Order Quantity
                      x-description-cn: 订单数量
                    executedQty:
                      type: string
                      example: "0"
                      description: Number of completed trades
                      x-description-cn: 已经成交的交易量
                    side:
                      type: string
                      example: BUY
                      description: Buy/sell direction
                      x-description-cn: 订单方向
                    type:
                      type: string
                      example: LIMIT
                      description: Order type
                      x-description-cn: 订单类型
                    timeInForce:
                      type: string
                      example: GTC
                      description: Time in force method
                      x-description-cn: 有效时间
                    reduceOnly:
                      type: boolean
                      example: false
                      description: Order is reduce only Y/N
                      x-description-cn: 仅减仓
                    createTime:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: Order Time
                      x-description-cn: 订单创建时间
                    updateTime:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: Update Time
                      x-description-cn: 订单更新时间
                    status:
                      type: string
                      example: NEW
                      description: Order status
                      x-description-cn: 订单状态
                    avgPrice:
                      type: string
                      example: "0"
                      description: Average price of completed trade
                      x-description-cn: 已成交平均价
                    clientOrderId:
                      type: string
                      example: ""
                      description: Client order ID
                      x-description-cn: 用户自定义订单id
                    priceScale:
                      type: integer
                      example: 2
                      format: int64
                      description: price Scale
                      x-description-cn: 价格精度
                    quantityScale:
                      type: integer
                      example: 2
                      format: int64
                      description: quantity Scale
                      x-description-cn: 数量精度
                    optionSide:
                      type: string
                      example: CALL
                      description: option Side
                      x-description-cn: 期权类型
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote Asset
                      x-description-cn: 报价资产
                    mmp:
                      type: boolean
                      example: false
                      description: mmp
                      x-description-cn: 是否为MMP订单
                    selfTradePreventionMode:
                      type: string
                      example: EXPIRE_MAKER
                      description: self trading prevention mode
                      x-description-cn: 订单自成交保护模式
  /eapi/v1/historyOrders:
    get:
      summary: Query Option Order History (TRADE)
      x-summary-cn: 查询历史订单 (TRADE)
      description: "Query all finished orders within 5 days, finished status: CANCELLED FILLED REJECTED."
      x-description-cn: 查询5天内的历史订单，订单的最终状态为 `CANCELED` 或者 `FILLED` 或者 `REJECTED`
      tags:
        - trade
      operationId: queryOptionOrderHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#query-option-order-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/queryOptionOrderHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/query_option_order_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/query_option_order_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/QueryOptionOrderHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/QueryOptionOrderHistory/QueryOptionOrderHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/QueryOptionOrderHistoryExample.php
      x-ip-weight: 3
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: orderId
          in: query
          required: false
          schema:
            type: integer
            example: 4611875134427365000
            format: int64
          description: Order ID.
          x-description-cn: 订单 ID。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 100
            maximum: 1000
            format: int64
          description: Number of result sets returned
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: Option Order History
          x-description-cn: Option 订单 历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    orderId:
                      type: integer
                      example: 4611875134427365000
                      format: int64
                      description: order Id
                      x-description-cn: 订单Id
                    symbol:
                      type: string
                      example: BTC-200730-9000-C
                      description: symbol
                      x-description-cn: 交易对
                    price:
                      type: string
                      example: "100"
                      description: price
                      x-description-cn: 订单价格
                    quantity:
                      type: string
                      example: "1"
                      description: quantity
                      x-description-cn: 订单数量
                    executedQty:
                      type: string
                      example: "0"
                      description: executed Qty
                      x-description-cn: 已经成交的交易量
                    side:
                      type: string
                      example: BUY
                      description: side
                      x-description-cn: 订单方向
                    type:
                      type: string
                      example: LIMIT
                      description: type
                      x-description-cn: 订单类型
                    timeInForce:
                      type: string
                      example: GTC
                      description: time In Force
                      x-description-cn: 有效时间
                    reduceOnly:
                      type: boolean
                      example: false
                      description: reduce Only
                      x-description-cn: 仅减仓
                    createTime:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: create Time
                      x-description-cn: 订单创建时间
                    updateTime:
                      type: integer
                      example: 1592465880683
                      format: int64
                      description: update Time
                      x-description-cn: 订单更新时间
                    status:
                      type: string
                      example: ACCEPTED
                      description: status
                      x-description-cn: 订单状态
                    avgPrice:
                      type: string
                      example: "0"
                      description: avg Price
                      x-description-cn: 已成交平均价
                    clientOrderId:
                      type: string
                      example: ""
                      description: client Order Id
                      x-description-cn: 用户自定义订单id
                    priceScale:
                      type: integer
                      example: 2
                      format: int64
                      description: price Scale
                      x-description-cn: 价格精度
                    quantityScale:
                      type: integer
                      example: 2
                      format: int64
                      description: quantity Scale
                      x-description-cn: 数量精度
                    optionSide:
                      type: string
                      example: CALL
                      description: option Side
                      x-description-cn: 期权类型
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote Asset
                      x-description-cn: 报价资产
                    mmp:
                      type: boolean
                      example: false
                      description: mmp
                      x-description-cn: 是否为MMP订单
  /eapi/v1/stock/contract:
    post:
      summary: TradFi Options Contract (USER_DATA)
      x-summary-cn: 传统金融期权协议 (USER_DATA)
      description: Sign TradFi Options agreement contract
      x-description-cn: 签署传统金融期权协议
      tags:
        - trade
      operationId: tradfiOptionsContract
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#tradfi-options-contract
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/tradfiOptionsContract.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/tradfi_options_contract.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/tradfi_options_contract.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/TradfiOptionsContractExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/TradfiOptionsContract/TradfiOptionsContract.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/TradfiOptionsContractExample.php
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
          description: TradFi Options Contract
          x-description-cn: 传统金融期权协议
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
  /eapi/v1/commission:
    get:
      summary: User Commission (USER_DATA)
      x-summary-cn: 用户手续费率 (USER_DATA)
      description: Get account commission.
      x-description-cn: 获取用户手续费率.
      tags:
        - trade
      operationId: userCommission
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#user-commission
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/userCommission.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/user_commission.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/user_commission.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/UserCommissionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/UserCommission/UserCommission.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/UserCommissionExample.php
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
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: User Commission
          x-description-cn: 用户 手续费
          content:
            application/json:
              schema:
                type: object
                properties:
                  commissions:
                    type: array
                    items:
                      type: object
                      properties:
                        underlying:
                          type: string
                          example: BTCUSDT
                          description: underlying
                          x-description-cn: 标的资产
                        makerFee:
                          type: string
                          example: "0.000240"
                          description: maker Fee
                          x-description-cn: maker Fee
                        takerFee:
                          type: string
                          example: "0.000240"
                          description: taker Fee
                          x-description-cn: taker Fee
                    description: commissions
                    x-description-cn: commissions
  /eapi/v1/exerciseRecord:
    get:
      summary: User Exercise Record (USER_DATA)
      x-summary-cn: 用户行权历史 (USER_DATA)
      description: Get account exercise records.
      x-description-cn: 获取用户行权历史.
      tags:
        - trade
      operationId: userExerciseRecord
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/trade#user-exercise-record
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/TradeApi/userExerciseRecord.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/trade_api/user_exercise_record.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/Trade/user_exercise_record.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/trade/UserExerciseRecordExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/TradeAPI/UserExerciseRecord/UserExerciseRecord.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/trade/UserExerciseRecordExample.php
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
            example: BTC-200730-9000-C
          description: Option trading pair.
          x-description-cn: 期权交易对。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time, e.g 1593511200000
          x-description-cn: 起始时间如1593511200000
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time, e.g 1593512200000
          x-description-cn: 结束时间如1593512200000
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 20
            default: 1000
            maximum: 1000
            format: int64
          description: Number of result sets returned.
          x-description-cn: 返回结果数量。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
          description: Recv Window.
          x-description-cn: 接收窗口。
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
          description: User Exercise Record
          x-description-cn: 用户 Exercise Record
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      example: "1125899906842624042"
                      description: id
                      x-description-cn: ID
                    currency:
                      type: string
                      example: USDT
                      description: currency
                      x-description-cn: currency
                    symbol:
                      type: string
                      example: BTC-220721-25000-C
                      description: symbol
                      x-description-cn: 交易对
                    exercisePrice:
                      type: string
                      example: "25000.00000000"
                      description: exercise Price
                      x-description-cn: exercise Price
                    quantity:
                      type: string
                      example: "1.00000000"
                      description: quantity
                      x-description-cn: 数量
                    amount:
                      type: string
                      example: "0.00000000"
                      description: amount
                      x-description-cn: 金额
                    fee:
                      type: string
                      example: "0.00000000"
                      description: fee
                      x-description-cn: fee
                    createDate:
                      type: integer
                      example: 1658361600000
                      format: int64
                      description: create Date
                      x-description-cn: 创建时间
                    priceScale:
                      type: integer
                      example: 2
                      format: int64
                      description: price Scale
                      x-description-cn: price Scale
                    quantityScale:
                      type: integer
                      example: 2
                      format: int64
                      description: quantity Scale
                      x-description-cn: quantity Scale
                    optionSide:
                      type: string
                      example: CALL
                      description: option Side
                      x-description-cn: option Side
                    positionSide:
                      type: string
                      example: LONG
                      description: position Side
                      x-description-cn: position Side
                    quoteAsset:
                      type: string
                      example: USDT
                      description: quote Asset
                      x-description-cn: 报价资产
  /eapi/v1/listenKey:
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/user-data-streams#close-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/UserDataStreamsApi/closeUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/user_data_streams_api/close_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/UserDataStreams/close_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/userdatastreams/CloseUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/UserDataStreamsAPI/CloseUserDataStream/CloseUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/userdatastreams/CloseUserDataStreamExample.php
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/user-data-streams#keepalive-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/UserDataStreamsApi/keepaliveUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/user_data_streams_api/keepalive_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/UserDataStreams/keepalive_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/userdatastreams/KeepaliveUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/UserDataStreamsAPI/KeepaliveUserDataStream/KeepaliveUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/userdatastreams/KeepaliveUserDataStreamExample.php
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
          https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-options/api/rest-api/user-data-streams#start-user-data-stream
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-options/examples/rest-api/UserDataStreamsApi/startUserDataStream.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_options/rest_api/user_data_streams_api/start_user_data_stream.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_options/examples/rest_api/UserDataStreams/start_user_data_stream.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-options/src/main/java/com/binance/connector/client/derivatives_trading_options/rest/userdatastreams/StartUserDataStreamExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingoptions/examples/restapi/UserDataStreamsAPI/StartUserDataStream/StartUserDataStream.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-options/userdatastreams/StartUserDataStreamExample.php
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
                    description: listen Key
                    x-description-cn: listen Key
                  expiration:
                    type: integer
                    example: 1762855900452
                    format: int64
                    description: Listen key expiration timestamp in milliseconds
                    x-description-cn: listenKey 过期时间戳（毫秒）
```