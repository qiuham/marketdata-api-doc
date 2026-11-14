---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:04.877457
---

# advanced-trading-derivatives-trading-portfolio-margin-pro__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Portfolio Margin Pro REST API
  description: Access advanced account management and high-frequency trading with Binance Portfolio Margin Pro.
  x-description-cn: 通过 Binance Portfolio Margin Pro 进行高级账户管理和高频交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/derivatives-trading-portfolio-margin-pro/general-info#limits
x-rate-limits-guide-cn: products/derivatives-trading-portfolio-margin-pro/general-info#访问限制
x-security-guide: products/derivatives-trading-portfolio-margin-pro/general-info#endpoint-security-type
x-security-guide-cn: products/derivatives-trading-portfolio-margin-pro/general-info#接口鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Portfolio Margin Pro docs
  url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin-pro/general-info
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: market-data
    x-displayName: Market Data
    x-displayName-cn: 行情接口
  - name: user-data-streams
    x-displayName: Portfolio Margin Pro User Data Stream
    x-displayName-cn: Websocket账户信息推送
servers:
  - url: https://api.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/portfolio/bnb-transfer:
    post:
      summary: BNB transfer (USER_DATA)
      x-summary-cn: BNB划转 (USER_DATA)
      description: BNB transfer can be between Margin Account and USDM Account
      x-description-cn: BNB在杠杆账户和USD-M期货账户划转
      tags:
        - account
      operationId: bnbTransfer
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#bnb-transfer
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/bnbTransfer.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/bnb_transfer.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/bnb_transfer.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/BnbTransferExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/BnbTransfer/BnbTransfer.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/BnbTransferExample.php
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
      x-parameters-notes: "- You can only use this function 2 times per 10 minutes in a rolling manner"
      x-parameters-notes-cn: "- 本接口每10分钟仅可以调用2次"
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
                    description: tran Id.
                    x-description-cn: 请参见英文说明：tran Id.
  /sapi/v1/portfolio/repay-futures-switch:
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
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#change-auto-repay-futures-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/changeAutoRepayFuturesStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/change_auto_repay_futures_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/change_auto_repay_futures_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/ChangeAutoRepayFuturesStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/ChangeAutoRepayFuturesStatus/ChangeAutoRepayFuturesStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/ChangeAutoRepayFuturesStatusExample.php
      x-ip-weight: 1500
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
                    description: msg.
                    x-description-cn: 请参见英文说明：msg.
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
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-auto-repay-futures-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getAutoRepayFuturesStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_auto_repay_futures_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_auto_repay_futures_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetAutoRepayFuturesStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetAutoRepayFuturesStatus/GetAutoRepayFuturesStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetAutoRepayFuturesStatusExample.php
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
  /sapi/v1/portfolio/auto-collection:
    post:
      summary: Fund Auto-collection (USER_DATA)
      x-summary-cn: 资金归集 (USER_DATA)
      description: Transfers all assets from Futures Account to Margin account
      x-description-cn: 将期货账户下所有资产归集至杠杆账户。
      tags:
        - account
      operationId: fundAutoCollection
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#fund-auto-collection
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/fundAutoCollection.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/fund_auto_collection.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/fund_auto_collection.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/FundAutoCollectionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/FundAutoCollection/FundAutoCollection.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/FundAutoCollectionExample.php
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
      x-parameters-notes: |-
        - The BNB would not be collected from UM-PM account to the Portfolio Margin account.
        - You can only use this function 500 times per hour in a rolling manner.
      x-parameters-notes-cn: |-
        - 本接口不会划转BNB资产
        - 本接口每小时仅能被调用500次（滚动计算）
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
                    description: msg.
                    x-description-cn: 请参见英文说明：msg.
  /sapi/v1/portfolio/asset-collection:
    post:
      summary: Fund Collection by Asset (USER_DATA)
      x-summary-cn: 特定资产资金归集 (USER_DATA)
      description: Transfers specific asset from Futures Account to Margin account
      x-description-cn: 特定资产账户资金归集，从合约账户划转到杠杆账户
      tags:
        - account
      operationId: fundCollectionByAsset
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#fund-collection-by-asset
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/fundCollectionByAsset.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/fund_collection_by_asset.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/fund_collection_by_asset.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/FundCollectionByAssetExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/FundCollectionByAsset/FundCollectionByAsset.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/FundCollectionByAssetExample.php
      x-ip-weight: 60
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
                  example: USDT
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
                    description: msg.
                    x-description-cn: 请参见英文说明：msg.
  /sapi/v1/portfolio/delta-mode:
    get:
      summary: Get Delta Mode Status (USER_DATA)
      x-summary-cn: 查询账户Delta模式状态 (USER_DATA)
      description: Query the Delta mode status of current account.
      x-description-cn: 查询账户Delta模式状态
      tags:
        - account
      operationId: getDeltaModeStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-delta-mode-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getDeltaModeStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_delta_mode_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_delta_mode_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetDeltaModeStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetDeltaModeStatus/GetDeltaModeStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetDeltaModeStatusExample.php
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
          description: Get Delta Mode Status
          x-description-cn: 获取Delta Mode 状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  deltaEnabled:
                    type: boolean
                    example: false
                    description: delta Enabled.
                    x-description-cn: 请参见英文说明：delta Enabled.
    post:
      summary: Switch Delta Mode (TRADE)
      x-summary-cn: 切换账户Delta模式 (TRADE)
      description: Switch the Delta mode for existing PM PRO / PM RETAIL accounts.
      x-description-cn: 切换当前 PM PRO / PM RETAIL账户Delta 模式
      tags:
        - account
      operationId: switchDeltaMode
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#switch-delta-mode
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/switchDeltaMode.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/switch_delta_mode.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/switch_delta_mode.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/SwitchDeltaModeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/SwitchDeltaMode/SwitchDeltaMode.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/SwitchDeltaModeExample.php
      x-ip-weight: 1500
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
                - deltaEnabled
                - timestamp
              properties:
                deltaEnabled:
                  type: string
                  example: "true"
                  enum:
                    - "true"
                    - "false"
                  description: "`true` to enable Delta mode; `false` to disable Delta mode"
                  x-description-cn: "`true`为开启Delta模式; `false`代表关闭Delta模式"
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
          description: Switch Delta Mode
          x-description-cn: 请参见英文说明：Switch Delta Mode
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
                    description: msg.
                    x-description-cn: 请参见英文说明：msg.
  /sapi/v1/portfolio/balance:
    get:
      summary: Get Portfolio Margin Pro Account Balance (USER_DATA)
      x-summary-cn: 查询统一账户专业版账户余额 (USER_DATA)
      description: Query Portfolio Margin Pro account balance
      x-description-cn: 查询统一账户专业版账户余额
      tags:
        - account
      operationId: getPortfolioMarginProAccountBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-portfolio-margin-pro-account-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getPortfolioMarginProAccountBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_portfolio_margin_pro_account_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_portfolio_margin_pro_account_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetPortfolioMarginProAccountBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetPortfolioMarginProAccountBalance/GetPortfolioMarginProAccountBalance.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetPortfolioMarginProAccountBalanceExample.php
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
            example: BTC
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
          description: Get Portfolio Margin Pro Account Balance
          x-description-cn: 获取Portfolio 杠杆 Pro 账户 Balance
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
                      description: asset.
                      x-description-cn: 请参见英文说明：asset.
                    totalWalletBalance:
                      type: string
                      example: "122607.35137903"
                      description: total Wallet Balance.
                      x-description-cn: 请参见英文说明：total Wallet Balance.
                    crossMarginAsset:
                      type: string
                      example: "92.27530794"
                      description: cross Margin Asset.
                      x-description-cn: 请参见英文说明：cross Margin Asset.
                    crossMarginBorrowed:
                      type: string
                      example: "10.00000000"
                      description: cross Margin Borrowed.
                      x-description-cn: 请参见英文说明：cross Margin Borrowed.
                    crossMarginFree:
                      type: string
                      example: "100.00000000"
                      description: cross Margin Free.
                      x-description-cn: 请参见英文说明：cross Margin Free.
                    crossMarginInterest:
                      type: string
                      example: "0.72469206"
                      description: cross Margin Interest.
                      x-description-cn: 请参见英文说明：cross Margin Interest.
                    crossMarginLocked:
                      type: string
                      example: "3.00000000"
                      description: cross Margin Locked.
                      x-description-cn: 请参见英文说明：cross Margin Locked.
                    umWalletBalance:
                      type: string
                      example: "0.00000000"
                      description: um Wallet Balance.
                      x-description-cn: 请参见英文说明：um Wallet Balance.
                    umUnrealizedPNL:
                      type: string
                      example: "23.72469206"
                      description: um Unrealized PNL.
                      x-description-cn: 请参见英文说明：um Unrealized PNL.
                    cmWalletBalance:
                      type: string
                      example: "23.72469206"
                      description: cm Wallet Balance.
                      x-description-cn: 请参见英文说明：cm Wallet Balance.
                    cmUnrealizedPNL:
                      type: string
                      example: ""
                      description: cm Unrealized PNL.
                      x-description-cn: 请参见英文说明：cm Unrealized PNL.
                    updateTime:
                      type: integer
                      example: 1617939110373
                      format: int64
                      description: update Time.
                      x-description-cn: 请参见英文说明：update Time.
                    negativeBalance:
                      type: string
                      example: "0"
                      description: negative Balance.
                      x-description-cn: 请参见英文说明：negative Balance.
                    optionWalletBalance:
                      type: string
                      example: "0"
                      description: option Wallet Balance.
                      x-description-cn: 请参见英文说明：option Wallet Balance.
                    optionEquity:
                      type: string
                      example: "0"
                      description: option Equity.
                      x-description-cn: 请参见英文说明：option Equity.
  /sapi/v1/portfolio/account:
    get:
      summary: Get Portfolio Margin Pro Account Info (USER_DATA)
      x-summary-cn: 查询统一账户专业版账户信息 (USER_DATA)
      description: Get Portfolio Margin Pro Account Info
      x-description-cn: 查询统一账户专业版账户信息
      tags:
        - account
      operationId: getPortfolioMarginProAccountInfo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-portfolio-margin-pro-account-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getPortfolioMarginProAccountInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_portfolio_margin_pro_account_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_portfolio_margin_pro_account_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetPortfolioMarginProAccountInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetPortfolioMarginProAccountInfo/GetPortfolioMarginProAccountInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetPortfolioMarginProAccountInfoExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 5
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
          description: Get Portfolio Margin Pro Account Info
          x-description-cn: 获取Portfolio 杠杆 Pro 账户 Info
          content:
            application/json:
              schema:
                type: object
                properties:
                  uniMMR:
                    type: string
                    example: "5167.92171923"
                    description: Classic Portfolio margin account maintenance margin rate
                    x-description-cn: 经典统一账户模式维持保证金率
                  accountEquity:
                    type: string
                    example: "122607.35137903"
                    description: Account equity, unit：USD
                    x-description-cn: 经典统一账户总权益，单位为USD
                  actualEquity:
                    type: string
                    example: "142607.35137903"
                    description: Actual equity, unit：USD
                    x-description-cn: 不考虑质押率经典统一账户总权益，单位为USD
                  accountMaintMargin:
                    type: string
                    example: "23.72469206"
                    description: Classic Portfolio margin account maintenance margin, unit：USD
                    x-description-cn: 经典统一账户维持保证金，即账户开仓及借贷总共需要的维持保证金，单位为USD
                  accountInitialMargin:
                    type: string
                    example: "47.44938412"
                    description: Ignored for PM PRO and PM PRO SPAN
                    x-description-cn: PM PRO and PM PRO SPAN请忽略
                  totalAvailableBalance:
                    type: string
                    example: 122,559.90199491
                    description: Ignored for PM PRO and PM PRO SPAN
                    x-description-cn: PM PRO and PM PRO SPAN请忽略
                  accountStatus:
                    type: string
                    example: NORMAL
                    description: >-
                      Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY",
                      "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"
                    x-description-cn: >-
                      经典统一账户当前账户状态:"NORMAL"正常状态, "MARGIN_CALL"补充保证金, "SUPPLY_MARGIN"再一次补充保证金, "REDUCE_ONLY"触发交易限制,
                      "ACTIVE_LIQUIDATION"手动强制平仓, "FORCE_LIQUIDATION"强制平仓, "BANKRUPTED"破产
                  accountType:
                    type: string
                    example: PM_1
                    description: PM_1 for PM PRO, PM_2 for PM, PM_3 for PM PRO SPAN
                    x-description-cn: PM_1统一账户专业版, PM_2统一账户， PM_2统一账户专业版SPAN
  /sapi/v2/portfolio/account:
    get:
      summary: Get Portfolio Margin Pro SPAN Account Info (USER_DATA)
      x-summary-cn: 查询统一账户专业版SPAN账户信息 (USER_DATA)
      description: Get Portfolio Margin Pro SPAN Account Info (For Portfolio Margin Pro SPAN users only)
      x-description-cn: 查询统一账户专业版SPAN账户信息
      tags:
        - account
      operationId: getPortfolioMarginProSpanAccountInfo
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-portfolio-margin-pro-span-account-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getPortfolioMarginProSpanAccountInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_portfolio_margin_pro_span_account_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_portfolio_margin_pro_span_account_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetPortfolioMarginProSpanAccountInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetPortfolioMarginProSpanAccountInfo/GetPortfolioMarginProSpanAccountInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetPortfolioMarginProSpanAccountInfoExample.php
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
          description: Get Portfolio Margin Pro SPAN Account Info
          x-description-cn: 获取Portfolio 杠杆 Pro SPAN 账户 Info
          content:
            application/json:
              schema:
                type: object
                properties:
                  uniMMR:
                    type: string
                    example: "5167.92171923"
                    description: uni MMR.
                    x-description-cn: 请参见英文说明：uni MMR.
                  accountEquity:
                    type: string
                    example: "122607.35137903"
                    description: Account equity, unit：USD
                    x-description-cn: Account equity, unit：USD
                  actualEquity:
                    type: string
                    example: "142607.35137903"
                    description: Actual equity, unit：USD
                    x-description-cn: Actual equity, unit：USD
                  accountMaintMargin:
                    type: string
                    example: "23.72469206"
                    description: Account maintenance margin, unit：USD
                    x-description-cn: Account maintenance margin, unit：USD
                  riskUnitMMList:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: BTC
                          description: asset.
                          x-description-cn: 请参见英文说明：asset.
                        uniMaintainUsd:
                          type: string
                          example: "23.72469206"
                          description: uni Maintain Usd.
                          x-description-cn: 请参见英文说明：uni Maintain Usd.
                  marginMM:
                    type: string
                    example: "0.00000000"
                    description: margin MM.
                    x-description-cn: 请参见英文说明：margin MM.
                  otherMM:
                    type: string
                    example: "0.00000000"
                    description: other MM.
                    x-description-cn: 请参见英文说明：other MM.
                  accountStatus:
                    type: string
                    example: NORMAL
                    description: >-
                      Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY",
                      "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"
                    x-description-cn: >-
                      Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY",
                      "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"
                  accountType:
                    type: string
                    example: PM_3
                    description: PM_1 for classic PM, PM_2 for PM, PM_3 for PM Pro(SPAN)
                    x-description-cn: PM_1 for classic PM, PM_2 for PM, PM_3 for PM Pro(SPAN)
  /sapi/v1/portfolio/earn-asset-balance:
    get:
      summary: Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA)
      x-summary-cn: 获取划转able Earn 资产 Balance 用于 Portfolio 杠杆 (USER_DATA)
      description: Get transferable earn asset balance for all types of Portfolio Margin account
      x-description-cn: 获取transferable earn 资产 balance 用于 all types of Portfolio 杠杆 账户
      tags:
        - account
      operationId: getTransferableEarnAssetBalanceForPortfolioMargin
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-transferable-earn-asset-balance-for-portfolio-margin
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getTransferableEarnAssetBalanceForPortfolioMargin.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_transferable_earn_asset_balance_for_portfolio_margin.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_transferable_earn_asset_balance_for_portfolio_margin.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetTransferableEarnAssetBalanceForPortfolioMarginExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetTransferableEarnAssetBalanceForPortfolioMargin/GetTransferableEarnAssetBalanceForPortfolioMargin.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetTransferableEarnAssetBalanceForPortfolioMarginExample.php
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
        - name: asset
          in: query
          required: true
          schema:
            type: string
            example: LDUSDT
          description: "`LDUSDT` only"
          x-description-cn: "`LDUSDT` 仅"
        - name: transferType
          in: query
          required: true
          schema:
            type: string
            example: EARN_TO_FUTURE
            enum:
              - EARN_TO_FUTURE
              - FUTURE_TO_EARN
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
          description: Get Transferable Earn Asset Balance for Portfolio Margin
          x-description-cn: 获取划转able Earn 资产 Balance 用于 Portfolio 杠杆
          content:
            application/json:
              schema:
                type: object
                properties:
                  asset:
                    type: string
                    example: LDUSDT
                    description: asset.
                    x-description-cn: 请参见英文说明：asset.
                  amount:
                    type: string
                    example: "0.55"
                    description: amount.
                    x-description-cn: 请参见英文说明：amount.
  /sapi/v1/portfolio/repay:
    post:
      summary: Portfolio Margin Pro Bankruptcy Loan Repay (TRADE)
      x-summary-cn: 偿还统一账户专业版穿仓负债 (TRADE)
      description: Repay Portfolio Margin Pro Bankruptcy Loan
      x-description-cn: 偿还统一账户专业版穿仓负债
      tags:
        - account
      operationId: portfolioMarginProBankruptcyLoanRepay
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#portfolio-margin-pro-bankruptcy-loan-repay
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/portfolioMarginProBankruptcyLoanRepay.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/portfolio_margin_pro_bankruptcy_loan_repay.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/portfolio_margin_pro_bankruptcy_loan_repay.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/PortfolioMarginProBankruptcyLoanRepayExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/PortfolioMarginProBankruptcyLoanRepay/PortfolioMarginProBankruptcyLoanRepay.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/PortfolioMarginProBankruptcyLoanRepayExample.php
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
        - Please note that the API Key has enabled Spot & Margin Trading permissions to access this endpoint.
        - USDT is taken from the Spot account and transferred to the Cross Margin account to repay the loan.
      x-parameters-notes-cn: |-
        - 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。
        - 还款时，系统将从现货账户划转USDT至全仓杠杆账户偿还负债。
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
          description: Portfolio Margin Pro Bankruptcy Loan Repay
          x-description-cn: Portfolio 杠杆 Pro Bankruptcy 借贷 还款
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 58203331886213500
                    format: int64
                    description: tran Id.
                    x-description-cn: 请参见英文说明：tran Id.
  /sapi/v1/portfolio/pmLoan:
    get:
      summary: Query Portfolio Margin Pro Bankruptcy Loan Amount (USER_DATA)
      x-summary-cn: 查询统一账户专业版穿仓借贷金额 (USER_DATA)
      description: Query Portfolio Margin Pro Bankruptcy Loan Amount
      x-description-cn: 查询统一账户专业版穿仓借贷金额
      tags:
        - account
      operationId: queryPortfolioMarginProBankruptcyLoanAmount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#query-portfolio-margin-pro-bankruptcy-loan-amount
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/queryPortfolioMarginProBankruptcyLoanAmount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/query_portfolio_margin_pro_bankruptcy_loan_amount.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/query_portfolio_margin_pro_bankruptcy_loan_amount.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/QueryPortfolioMarginProBankruptcyLoanAmountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/QueryPortfolioMarginProBankruptcyLoanAmount/QueryPortfolioMarginProBankruptcyLoanAmount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/QueryPortfolioMarginProBankruptcyLoanAmountExample.php
      x-security-type: USER_DATA
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
      x-parameters-notes: "- If there’s no classic portfolio margin bankruptcy loan, the amount would be 0"
      x-parameters-notes-cn: "- 如果不存在统一账户专业版穿仓负债，amount显示为0"
      responses:
        "200":
          description: Portfolio Margin Pro Bankruptcy Loan Amount
          x-description-cn: Portfolio 杠杆 Pro Bankruptcy 借贷 数量
          content:
            application/json:
              schema:
                type: object
                properties:
                  asset:
                    type: string
                    example: BUSD
                    description: asset.
                    x-description-cn: 请参见英文说明：asset.
                  amount:
                    type: string
                    example: "579.45"
                    description: portfolio margin bankruptcy loan amount in BUSD
                    x-description-cn: 统一账户用户强平穿仓负债，单位为BUSD
  /sapi/v1/portfolio/pmloan-history:
    get:
      summary: Query Portfolio Margin Pro Bankruptcy Loan Repay History (USER_DATA)
      x-summary-cn: 查询经典统一账户专业版穿仓借贷偿还历史 (USER_DATA)
      description: Query repay history of pmloan for portfolio margin pro.
      x-description-cn: 查询统一账户专业版穿仓借贷偿还历史
      tags:
        - account
      operationId: queryPortfolioMarginProBankruptcyLoanRepayHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#query-portfolio-margin-pro-bankruptcy-loan-repay-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/queryPortfolioMarginProBankruptcyLoanRepayHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/query_portfolio_margin_pro_bankruptcy_loan_repay_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/query_portfolio_margin_pro_bankruptcy_loan_repay_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/QueryPortfolioMarginProBankruptcyLoanRepayHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/QueryPortfolioMarginProBankruptcyLoanRepayHistory/QueryPortfolioMarginProBankruptcyLoanRepayHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/QueryPortfolioMarginProBankruptcyLoanRepayHistoryExample.php
      x-ip-weight: 500
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
          x-description-cn: 返回的结果集数量 默认值:10 最大值:100
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
            minimum: 1
          description: Currently querying page. Start from 1.
          x-description-cn: 默认值：1
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
        - `startTime` and `endTime` cannot be longer than 360 days
        - If `startTime` and `endTime` not sent, return records of the last 30 days by default.
        - If `startTime`is sent and `endTime` is not sent, return records of [startTime, startTime+30d].
        - If `startTime` is not sent and `endTime` is sent, return records of [endTime-30d, endTime].
      x-parameters-notes-cn: |-
        - `startTime` 和 `endTime` 间隔不能超过 360天
        - 如果 `startTime` 和 `endTime` 没有传, 默认返回最近30天的记录
        - 如果传了 `startTime` 但没有传 `endTime`, 返回记录 [startTime, startTime+30d]
        - 如果没传 `startTime` 但传了 `endTime`, 返回记录 [endTime-30d, endTime]
      responses:
        "200":
          description: Portfolio Margin Pro Bankruptcy Loan Repay History
          x-description-cn: Portfolio 杠杆 Pro Bankruptcy 借贷 还款 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 3
                    format: int64
                    description: total.
                    x-description-cn: 请参见英文说明：total.
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                          description: asset.
                          x-description-cn: 请参见英文说明：asset.
                        amount:
                          type: string
                          example: "404.80294503"
                          description: amount.
                          x-description-cn: 请参见英文说明：amount.
                        repayTime:
                          type: integer
                          example: 1731336427804
                          format: int64
                          description: repay Time.
                          x-description-cn: 请参见英文说明：repay Time.
  /sapi/v1/portfolio/interest-history:
    get:
      summary: Query Portfolio Margin Pro Negative Balance Interest History (USER_DATA)
      x-summary-cn: 查询经典统一账户专业版期货负余额收息历史 (USER_DATA)
      description: Query interest history of negative balance for portfolio margin.
      x-description-cn: 查询统一账户专业版期货负余额收息历史
      tags:
        - account
      operationId: queryPortfolioMarginProNegativeBalanceInterestHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#query-portfolio-margin-pro-negative-balance-interest-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/queryPortfolioMarginProNegativeBalanceInterestHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/query_portfolio_margin_pro_negative_balance_interest_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/query_portfolio_margin_pro_negative_balance_interest_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/QueryPortfolioMarginProNegativeBalanceInterestHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/QueryPortfolioMarginProNegativeBalanceInterestHistory/QueryPortfolioMarginProNegativeBalanceInterestHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/QueryPortfolioMarginProNegativeBalanceInterestHistoryExample.php
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
          x-description-cn: 返回的结果集数量 默认值:10 最大值:100
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
          description: Portfolio Margin Pro Negative Balance Interest History
          x-description-cn: Portfolio 杠杆 Pro Negative Balance 利息 历史
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
                      description: asset.
                      x-description-cn: 请参见英文说明：asset.
                    interest:
                      type: string
                      example: "24.4440"
                      description: interest amount
                      x-description-cn: 利息金额
                    interestAccruedTime:
                      type: integer
                      example: 1670227200000
                      format: int64
                      description: interest Accrued Time.
                      x-description-cn: 请参见英文说明：interest Accrued Time.
                    interestRate:
                      type: string
                      example: "0.0001164"
                      description: daily interest rate
                      x-description-cn: 日利率
                    principal:
                      type: string
                      example: "210000"
                      description: principal.
                      x-description-cn: 请参见英文说明：principal.
  /sapi/v1/portfolio/repay-futures-negative-balance:
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
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#repay-futures-negative-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/repayFuturesNegativeBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/repay_futures_negative_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/repay_futures_negative_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/RepayFuturesNegativeBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/RepayFuturesNegativeBalance/RepayFuturesNegativeBalance.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/RepayFuturesNegativeBalanceExample.php
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
      x-parameters-notes: "- The negative balance is repaid from the Cross Margin account."
      x-parameters-notes-cn: "- 合约负余额将从全仓杠杆账户中偿还。"
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
                    description: msg.
                    x-description-cn: 请参见英文说明：msg.
  /sapi/v1/portfolio/earn-asset-transfer:
    post:
      summary: Transfer LDUSDT/RWUSD for Portfolio Margin (TRADE)
      x-summary-cn: 统一账户转入LDUSDT/RWUSD资产 (TRADE)
      description: Transfer LDUSDT/RWUSD as collateral for all types of Portfolio Margin account
      x-description-cn: LDUSDT/RWUSD转入，支持所有的统一账户类型
      tags:
        - account
      operationId: transferLdusdtRwusdForPortfolioMargin
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#transfer-ldusdt-rwusd-for-portfolio-margin
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/transferLdusdtRwusdForPortfolioMargin.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/transfer_ldusdt_rwusd_for_portfolio_margin.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/transfer_ldusdt_rwusd_for_portfolio_margin.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/TransferLdusdtRwusdForPortfolioMarginExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/TransferLdusdtRwusdForPortfolioMargin/TransferLdusdtRwusdForPortfolioMargin.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/TransferLdusdtRwusdForPortfolioMarginExample.php
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 1500
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
                - transferType
                - amount
                - timestamp
              properties:
                asset:
                  type: string
                  example: LDUSDT
                  enum:
                    - LDUSDT
                    - RWUSD
                transferType:
                  type: string
                  example: EARN_TO_FUTURE
                  enum:
                    - EARN_TO_FUTURE
                    - FUTURE_TO_EARN
                amount:
                  type: number
                  example: 1
                  format: float
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
          description: Transfer LDUSDT/RWUSD for Portfolio Margin
          x-description-cn: 划转 LDUSDT/RWUSD 用于 Portfolio 杠杆
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
                    description: msg.
                    x-description-cn: 请参见英文说明：msg.
  /sapi/v1/portfolio/margin-call-level:
    get:
      summary: Get Margin Call Level (USER_DATA)
      x-summary-cn: 查询强平预警线 (USER_DATA)
      description: Get the margin call level for a Portfolio Margin account.
      x-description-cn: 查询统一保证金账户的强平预警线。
      tags:
        - account
      operationId: getMarginCallLevel
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#get-margin-call-level
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/getMarginCallLevel.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/get_margin_call_level.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/get_margin_call_level.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/GetMarginCallLevelExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/GetMarginCallLevel/GetMarginCallLevel.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/GetMarginCallLevelExample.php
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
          description: Get Margin Call Level
          x-description-cn: 查询强平预警线
          content:
            application/json:
              schema:
                type: object
                properties:
                  marginCallLevel:
                    type: string
                    example: "1.67354637"
                    description: The margin call level value. Empty object returned if not set.
                    x-description-cn: 强平预警线值。未设置时返回空对象。
    post:
      summary: Set Margin Call Level (USER_DATA)
      x-summary-cn: 设置强平预警线 (USER_DATA)
      description: >-
        Set the margin call level for a Portfolio Margin account. When the account's uniMMR drops to the specified
        level, a notification will be sent via email and push/inbox.
      x-description-cn: 设置统一保证金账户的强平预警线。当账户的 uniMMR 降至指定水平时，系统将通过邮件和推送/站内信发送通知。
      tags:
        - account
      operationId: setMarginCallLevel
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#set-margin-call-level
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/setMarginCallLevel.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/set_margin_call_level.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/set_margin_call_level.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/SetMarginCallLevelExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/SetMarginCallLevel/SetMarginCallLevel.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/SetMarginCallLevelExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - marginCallLevel
                - timestamp
              properties:
                marginCallLevel:
                  type: number
                  example: 1.5
                  format: float
                  description: The value must be within the range [1.1, 2.0].
                  x-description-cn: 取值范围必须在 [1.1, 2.0] 之间。
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
                  description: >-
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and

                    is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Set Margin Call Level
          x-description-cn: 设置强平预警线
          content:
            application/json:
              schema:
                type: object
                properties:
                  marginCallLevel:
                    type: string
                    example: "1.67354637"
                    description: The margin call level that was set
                    x-description-cn: 已设置的强平预警线值
    delete:
      summary: Delete Margin Call Level (USER_DATA)
      x-summary-cn: 删除强平预警线 (USER_DATA)
      description: Delete the margin call level for a Portfolio Margin account.
      x-description-cn: 删除统一保证金账户的强平预警线。
      tags:
        - account
      operationId: deleteMarginCallLevel
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/account#delete-margin-call-level
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/AccountApi/deleteMarginCallLevel.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/account_api/delete_margin_call_level.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/Account/delete_margin_call_level.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/account/DeleteMarginCallLevelExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/AccountAPI/DeleteMarginCallLevel/DeleteMarginCallLevel.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/account/DeleteMarginCallLevelExample.php
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
          description: Delete Margin Call Level
          x-description-cn: 删除强平预警线
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
  /sapi/v1/portfolio/margin-asset-leverage:
    get:
      summary: Get Portfolio Margin Asset Leverage (USER_DATA)
      x-summary-cn: 查询统一账户资产支持杠杆倍数 (USER_DATA)
      description: Get Portfolio Margin Asset Leverage
      x-description-cn: 查询统一账户资产支持杠杆倍数
      tags:
        - market-data
      operationId: getPortfolioMarginAssetLeverage
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/market-data#get-portfolio-margin-asset-leverage
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/MarketDataApi/getPortfolioMarginAssetLeverage.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/market_data_api/get_portfolio_margin_asset_leverage.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/MarketData/get_portfolio_margin_asset_leverage.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/marketdata/GetPortfolioMarginAssetLeverageExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/MarketDataAPI/GetPortfolioMarginAssetLeverage/GetPortfolioMarginAssetLeverage.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/marketdata/GetPortfolioMarginAssetLeverageExample.php
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
          description: Get Portfolio Margin Asset Leverage
          x-description-cn: 获取Portfolio 杠杆 资产 Leverage
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    asset:
                      type: string
                      example: USDC
                      description: asset.
                      x-description-cn: 请参见英文说明：asset.
                    leverage:
                      type: integer
                      example: 10
                      format: int64
                      description: leverage.
                      x-description-cn: 请参见英文说明：leverage.
  /sapi/v1/portfolio/collateralRate:
    get:
      summary: Portfolio Margin Collateral Rate (MARKET_DATA)
      x-summary-cn: 统一账户资产质押率 (MARKET_DATA)
      description: Portfolio Margin Collateral Rate
      x-description-cn: 统一账户资产质押率
      tags:
        - market-data
      operationId: portfolioMarginCollateralRate
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/market-data#portfolio-margin-collateral-rate
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/MarketDataApi/portfolioMarginCollateralRate.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/market_data_api/portfolio_margin_collateral_rate.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/MarketData/portfolio_margin_collateral_rate.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/marketdata/PortfolioMarginCollateralRateExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/MarketDataAPI/PortfolioMarginCollateralRate/PortfolioMarginCollateralRate.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/marketdata/PortfolioMarginCollateralRateExample.php
      x-ip-weight: 50
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
      responses:
        "200":
          description: Portfolio Margin Collateral Rate
          x-description-cn: Portfolio 杠杆 抵押 利率
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    asset:
                      type: string
                      example: USDC
                      description: asset.
                      x-description-cn: 请参见英文说明：asset.
                    collateralRate:
                      type: string
                      example: "1.0000"
                      description: collateral Rate.
                      x-description-cn: 质押率
  /sapi/v2/portfolio/collateralRate:
    get:
      summary: Portfolio Margin Pro Tiered Collateral Rate (USER_DATA)
      x-summary-cn: 统一账户专业版资产阶梯质押率 (USER_DATA)
      description: Portfolio Margin PRO Tiered Collateral Rate
      x-description-cn: 统一账户专业版资产阶梯质押率
      tags:
        - market-data
      operationId: portfolioMarginProTieredCollateralRate
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/market-data#portfolio-margin-pro-tiered-collateral-rate
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/MarketDataApi/portfolioMarginProTieredCollateralRate.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/market_data_api/portfolio_margin_pro_tiered_collateral_rate.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/MarketData/portfolio_margin_pro_tiered_collateral_rate.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/marketdata/PortfolioMarginProTieredCollateralRateExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/MarketDataAPI/PortfolioMarginProTieredCollateralRate/PortfolioMarginProTieredCollateralRate.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/marketdata/PortfolioMarginProTieredCollateralRateExample.php
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
          description: Portfolio Margin Pro Tiered Collateral Rate
          x-description-cn: Portfolio 杠杆 Pro Tiered 抵押 利率
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    asset:
                      type: string
                      example: BNB
                      description: asset.
                      x-description-cn: 请参见英文说明：asset.
                    collateralInfo:
                      type: array
                      items:
                        type: object
                        properties:
                          tierFloor:
                            type: string
                            example: "0.0000"
                            description: tier Floor.
                            x-description-cn: 请参见英文说明：tier Floor.
                          tierCap:
                            type: string
                            example: "1000.0000"
                            description: tier Cap.
                            x-description-cn: 请参见英文说明：tier Cap.
                          collateralRate:
                            type: string
                            example: "1.0000"
                            description: collateral Rate.
                            x-description-cn: 请参见英文说明：collateral Rate.
                          cum:
                            type: string
                            example: "0.0000"
                            description: account equity quick addition number
                            x-description-cn: 账户权益计算速算数
  /sapi/v1/portfolio/asset-index-price:
    get:
      summary: Query Portfolio Margin Asset Index Price (MARKET_DATA)
      x-summary-cn: 查询统一账户资产价格指数 (MARKET_DATA)
      description: Query Portfolio Margin Asset Index Price
      x-description-cn: 查询统一账户资产价格指数
      tags:
        - market-data
      operationId: queryPortfolioMarginAssetIndexPrice
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/market-data#query-portfolio-margin-asset-index-price
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/derivatives-trading-portfolio-margin-pro/examples/rest-api/MarketDataApi/queryPortfolioMarginAssetIndexPrice.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/derivatives_trading_portfolio_margin_pro/rest_api/market_data_api/query_portfolio_margin_asset_index_price.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/derivatives_trading_portfolio_margin_pro/examples/rest_api/MarketData/query_portfolio_margin_asset_index_price.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/derivatives-trading-portfolio-margin-pro/src/main/java/com/binance/connector/client/derivatives_trading_portfolio_margin_pro/rest/marketdata/QueryPortfolioMarginAssetIndexPriceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/derivativestradingportfoliomarginpro/examples/restapi/MarketDataAPI/QueryPortfolioMarginAssetIndexPrice/QueryPortfolioMarginAssetIndexPrice.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/derivatives-trading-portfolio-margin-pro/marketdata/QueryPortfolioMarginAssetIndexPriceExample.php
      x-security-type: MARKET_DATA
      x-weight: |-
        - 1 if `asset` is sent
        - 50 if `asset` is not sent
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
            example: BTC
      responses:
        "200":
          description: Portfolio Margin Asset Index Price
          x-description-cn: Portfolio 杠杆 资产 Index 价格
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
                      description: asset.
                      x-description-cn: 请参见英文说明：asset.
                    assetIndexPrice:
                      type: string
                      example: "28251.9136906"
                      description: in USD
                      x-description-cn: USD价格指数
                    time:
                      type: integer
                      example: 1683518338121
                      format: int64
                      description: time.
                      x-description-cn: 请参见英文说明：time.
```