---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:27.671962
---

# vip-and-institutional-sub-account__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Sub Account REST API
  description: Create and manage sub-accounts, control permissions, and transfer assets via the Sub Account API.
  x-description-cn: 通过 Sub Account API 创建和管理子账户、控制权限并划转资产。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/sub-account/general-info#limits
x-rate-limits-guide-cn: products/sub-account/general-info#访问限制
x-security-guide: products/sub-account/general-info#request-security
x-security-guide-cn: products/sub-account/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Sub Account docs
  url: https://developers.binance.com/en/docs/products/sub-account/Introduction
tags:
  - name: account-management
    x-displayName: Account Management
    x-displayName-cn: 帐户管理
  - name: api-management
    x-displayName: API Management
    x-displayName-cn: API管理
  - name: asset-management
    x-displayName: Asset Management
    x-displayName-cn: 资产管理
  - name: managed-sub-account
    x-displayName: Managed Sub Account
    x-displayName-cn: 托管子帳戶
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/sub-account/virtualSubAccount:
    post:
      summary: Create a Virtual Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 创建虚拟子账户 (适用主账户) (USER_DATA)
      description: Create a Virtual Sub-account
      x-description-cn: 创建虚拟子账户
      tags:
        - account-management
      operationId: createAVirtualSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#create-avirtual-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/createAVirtualSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/create_a_virtual_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/create_a_virtual_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/CreateAVirtualSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/CreateAVirtualSubAccount/CreateAVirtualSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/CreateAVirtualSubAccountExample.php
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
      x-parameters-notes: |-
        - This request generates a virtual sub-account under your master account.
        - The API key used to call this endpoint must have the `trade` option enabled.
      x-parameters-notes-cn: |-
        - 该请求会为您的母账户生成一个虚拟子账户
        - 调用此接口的 API Key 需要开通“允许现货及杠杆交易”权限
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - subAccountString
                - timestamp
              properties:
                subAccountString:
                  type: string
                  example: testSubAccount
                  description: Please input a string. We will create a virtual email using that string for you to register
                  x-description-cn: 请输入字符串，我们将为您创建一个虚拟邮箱进行注册
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Create a Virtual Sub-account
          x-description-cn: 创建虚拟子账户
          content:
            application/json:
              schema:
                type: object
                properties:
                  email:
                    type: string
                    example: addsdd_virtual@aasaixwqnoemail.com
  /sapi/v1/sub-account/futures/enable:
    post:
      summary: Enable Futures for Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 为子账户开通合约 (适用主账户) (USER_DATA)
      description: Enable Futures for Sub-account for Master Account
      x-description-cn: 为子账户开通合约 (适用主账户)
      tags:
        - account-management
      operationId: enableFuturesForSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#enable-futures-for-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/enableFuturesForSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/enable_futures_for_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/enable_futures_for_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/EnableFuturesForSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/EnableFuturesForSubAccount/EnableFuturesForSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/EnableFuturesForSubAccountExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Enable Futures for Sub-account
          x-description-cn: 为子账户开通合约
          content:
            application/json:
              schema:
                type: object
                properties:
                  email:
                    type: string
                    example: 123@test.com
                  isFuturesEnabled:
                    type: boolean
                    example: true
                    description: true or false
                    x-description-cn: true or false
  /sapi/v1/sub-account/eoptions/enable:
    post:
      summary: Enable Options for Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 为子账户开通期权 (适用主账户) (USER_DATA)
      description: Enable Options for Sub-account (For Master Account).
      x-description-cn: 为子账户开通期权 (适用主账户)
      tags:
        - account-management
      operationId: enableOptionsForSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#enable-options-for-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/enableOptionsForSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/enable_options_for_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/enable_options_for_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/EnableOptionsForSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/EnableOptionsForSubAccount/EnableOptionsForSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/EnableOptionsForSubAccountExample.php
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Enable Options for Sub-account
          x-description-cn: 为子账户开通期权
          content:
            application/json:
              schema:
                type: object
                properties:
                  email:
                    type: string
                    example: 123@test.com
                  isEOptionsEnabled:
                    type: boolean
                    example: true
                    description: true or false
                    x-description-cn: true or false
  /sapi/v1/sub-account/futures/positionRisk:
    get:
      summary: Get Futures Position-Risk of Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约持仓信息 (仅适用主账户) (USER_DATA)
      description: Get Futures Position-Risk of Sub-account
      x-description-cn: 查询子账户合约持仓信息
      tags:
        - account-management
      operationId: getFuturesPositionRiskOfSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#get-futures-position-risk-of-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/getFuturesPositionRiskOfSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/get_futures_position_risk_of_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/get_futures_position_risk_of_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/GetFuturesPositionRiskOfSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/GetFuturesPositionRiskOfSubAccount/GetFuturesPositionRiskOfSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/GetFuturesPositionRiskOfSubAccountExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Futures Position-Risk of Sub-account
          x-description-cn: 查询子账户合约持仓风险
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    entryPrice:
                      type: string
                      example: "9975.12000"
                    leverage:
                      type: string
                      example: "50"
                      description: current initial leverage
                      x-description-cn: current initial leverage
                    maxNotional:
                      type: string
                      example: "1000000"
                      description: notional value limit of current initial leverage
                      x-description-cn: notional value limit of current initial leverage
                    liquidationPrice:
                      type: string
                      example: "7963.54"
                    markPrice:
                      type: string
                      example: "9973.50770517"
                    positionAmount:
                      type: string
                      example: "0.010"
                    symbol:
                      type: string
                      example: BTCUSDT
                    unrealizedProfit:
                      type: string
                      example: "-0.01612295"
  /sapi/v2/sub-account/futures/positionRisk:
    get:
      summary: Get Futures Position-Risk of Sub-account V2 (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约持仓信息V2 (仅适用主账户) (USER_DATA)
      description: Get Futures Position-Risk of Sub-account V2
      x-description-cn: 查询子账户合约持仓信息
      tags:
        - account-management
      operationId: getFuturesPositionRiskOfSubAccountV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#get-futures-position-risk-of-sub-account-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/getFuturesPositionRiskOfSubAccountV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/get_futures_position_risk_of_sub_account_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/get_futures_position_risk_of_sub_account_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/GetFuturesPositionRiskOfSubAccountV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/GetFuturesPositionRiskOfSubAccountV2/GetFuturesPositionRiskOfSubAccountV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/GetFuturesPositionRiskOfSubAccountV2Example.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: futuresType
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: "1: USDT-margined Futures，2: Coin-margined Futures"
          x-description-cn: "1: USDT合约，2: 币本位合约"
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Futures Position-Risk of Sub-account V2
          x-description-cn: 查询子账户合约持仓风险 V2
          content:
            application/json:
              schema:
                type: object
                properties:
                  futurePositionRiskVos:
                    type: array
                    items:
                      type: object
                      properties:
                        entryPrice:
                          type: string
                          example: "9975.12000"
                        leverage:
                          type: string
                          example: "50"
                          description: current initial leverage
                          x-description-cn: current initial leverage
                        maxNotional:
                          type: string
                          example: "1000000"
                          description: notional value limit of current initial leverage
                          x-description-cn: notional value limit of current initial leverage
                        liquidationPrice:
                          type: string
                          example: "7963.54"
                        markPrice:
                          type: string
                          example: "9973.50770517"
                        positionAmount:
                          type: string
                          example: "0.010"
                        symbol:
                          type: string
                          example: BTCUSDT
                        unrealizedProfit:
                          type: string
                          example: "-0.01612295"
                  deliveryPositionRiskVos:
                    type: array
                    items:
                      type: object
                      properties:
                        entryPrice:
                          type: string
                          example: "9975.12000"
                        markPrice:
                          type: string
                          example: "9973.50770517"
                        leverage:
                          type: string
                          example: "20"
                        isolated:
                          type: string
                          example: "false"
                        isolatedWallet:
                          type: string
                          example: "9973.50770517"
                        isolatedMargin:
                          type: string
                          example: "0.00000000"
                        isAutoAddMargin:
                          type: string
                          example: "false"
                        positionSide:
                          type: string
                          example: BOTH
                        positionAmount:
                          type: string
                          example: "1.230"
                        symbol:
                          type: string
                          example: BTCUSD_201225
                        unrealizedProfit:
                          type: string
                          example: "-0.01612295"
  /sapi/v1/sub-account/status:
    get:
      summary: Get Sub-account's Status on Margin Or Futures (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户杠杆/合约状态 (适用主账户) (USER_DATA)
      description: Get Sub-account's Status on Margin Or Futures
      x-description-cn: 查询子账户杠杆/合约状态
      tags:
        - account-management
      operationId: getSubAccountsStatusOnMarginOrFutures
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#get-sub-accounts-status-on-margin-or-futures
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/getSubAccountsStatusOnMarginOrFutures.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/get_sub_accounts_status_on_margin_or_futures.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/get_sub_accounts_status_on_margin_or_futures.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/GetSubAccountsStatusOnMarginOrFuturesExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/GetSubAccountsStatusOnMarginOrFutures/GetSubAccountsStatusOnMarginOrFutures.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/GetSubAccountsStatusOnMarginOrFuturesExample.php
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
        - name: email
          in: query
          required: false
          schema:
            type: string
            example: 123@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- If no email sent, all sub-accounts' information will be returned."
      x-parameters-notes-cn: "- 如果不提交子账户email，返回所有子账户情况。"
      responses:
        "200":
          description: Get Sub-account's Status on Margin Or Futures
          x-description-cn: 查询子账户杠杆或合约状态
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    email:
                      type: string
                      example: 123@test.com
                      description: user email
                      x-description-cn: user email
                    isSubUserEnabled:
                      type: boolean
                      example: true
                      description: true or false
                      x-description-cn: true or false
                    isUserActive:
                      type: boolean
                      example: true
                      description: true or false
                      x-description-cn: true or false
                    insertTime:
                      type: integer
                      example: 1570791523523
                      format: int64
                      description: sub account create time
                      x-description-cn: sub account create time
                    isMarginEnabled:
                      type: boolean
                      example: true
                      description: true or false for margin
                      x-description-cn: true or false for margin
                    isFutureEnabled:
                      type: boolean
                      example: true
                      description: true or false for futures.
                      x-description-cn: true or false for futures.
                    mobile:
                      type: integer
                      example: 1570791523523
                      format: int64
                      description: user mobile number
                      x-description-cn: user mobile number
  /sapi/v1/sub-account/list:
    get:
      summary: Query Sub-account List (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户列表 (适用主账户) (USER_DATA)
      description: Query Sub-account List
      x-description-cn: 查询子账户列表(适用主账户)
      tags:
        - account-management
      operationId: querySubAccountList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#query-sub-account-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/querySubAccountList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/query_sub_account_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/query_sub_account_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/QuerySubAccountListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/QuerySubAccountList/QuerySubAccountList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/QuerySubAccountListExample.php
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
        - name: email
          in: query
          required: false
          schema:
            type: string
            example: 123@test.com
        - name: isFreeze
          in: query
          required: false
          schema:
            type: string
            example: true
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 1
            maximum: 200
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account List
          x-description-cn: 子账户列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  subAccounts:
                    type: array
                    items:
                      type: object
                      properties:
                        subUserId:
                          type: integer
                          example: 123456
                          format: int64
                        email:
                          type: string
                          example: testsub@gmail.com
                        remark:
                          type: string
                          example: remark
                        isFreeze:
                          type: boolean
                          example: false
                        createTime:
                          type: integer
                          example: 1544433328000
                          format: int64
                        isManagedSubAccount:
                          type: boolean
                          example: false
                        isAssetManagementSubAccount:
                          type: boolean
                          example: false
  /sapi/v1/sub-account/transaction-statistics:
    get:
      summary: Query Sub-account Transaction Statistics (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户交易量统计列表 (适用母账户) (USER_DATA)
      description: Query Sub-account Transaction statistics (For Master Account).
      x-description-cn: 查询子账户交易量统计列表 (适用母账户)
      tags:
        - account-management
      operationId: querySubAccountTransactionStatistics
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/account-management#query-sub-account-transaction-statistics
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AccountManagementApi/querySubAccountTransactionStatistics.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/account_management_api/query_sub_account_transaction_statistics.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AccountManagement/query_sub_account_transaction_statistics.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/accountmanagement/QuerySubAccountTransactionStatisticsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AccountManagementAPI/QuerySubAccountTransactionStatistics/QuerySubAccountTransactionStatistics.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/accountmanagement/QuerySubAccountTransactionStatisticsExample.php
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
        - name: email
          in: query
          required: false
          schema:
            type: string
            example: abc@test.com
          description: Managed sub-account email
          x-description-cn: 托管子账户邮箱
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account Transaction Statistics
          x-description-cn: 子账户交易量统计
          content:
            application/json:
              schema:
                type: object
                properties:
                  recent30BtcTotal:
                    type: string
                    example: "0"
                  recent30BtcFuturesTotal:
                    type: string
                    example: "0"
                  recent30BtcMarginTotal:
                    type: string
                    example: "0"
                  recent30BusdTotal:
                    type: string
                    example: "0"
                  recent30BusdFuturesTotal:
                    type: string
                    example: "0"
                  recent30BusdMarginTotal:
                    type: string
                    example: "0"
                  tradeInfoVos:
                    type: array
                    items:
                      type: object
                      properties:
                        userId:
                          type: integer
                          example: 1000138138384
                          format: int64
                        btc:
                          type: integer
                          example: 0
                          format: int64
                        btcFutures:
                          type: integer
                          example: 0
                          format: int64
                        btcMargin:
                          type: integer
                          example: 0
                          format: int64
                        busd:
                          type: integer
                          example: 0
                          format: int64
                        busdFutures:
                          type: integer
                          example: 0
                          format: int64
                        busdMargin:
                          type: integer
                          example: 0
                          format: int64
                        date:
                          type: integer
                          example: 1676851200000
                          format: int64
  /sapi/v2/sub-account/subAccountApi/ipRestriction:
    post:
      summary: Add IP Restriction for Sub-Account API key (For Master Account) (USER_DATA)
      x-summary-cn: 为子账户API Key增加IP白名单 (适用母账户) (USER_DATA)
      description: Add IP Restriction for Sub-Account API key
      x-description-cn: 为子账户API Key增加IP白名单
      tags:
        - api-management
      operationId: addIpRestrictionForSubAccountApiKey
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#add-ip-restriction-for-sub-account-api-key
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/addIpRestrictionForSubAccountApiKey.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/add_ip_restriction_for_sub_account_api_key.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/add_ip_restriction_for_sub_account_api_key.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/AddIpRestrictionForSubAccountApiKeyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/AddIpRestrictionForSubAccountApiKey/AddIpRestrictionForSubAccountApiKey.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/AddIpRestrictionForSubAccountApiKeyExample.php
      x-security-type: USER_DATA
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
      x-parameters-notes: "- You need to enable Enable Spot & Margin Trading option for the api key which requests this endpoint"
      x-parameters-notes-cn: "- 调用此端口前需要在api管理页开启允许现货及杠杆交易选项"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - subAccountApiKey
                - status
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
                subAccountApiKey:
                  type: string
                  example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
                status:
                  type: integer
                  example: 1
                  format: int64
                  description: IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only.
                  x-description-cn: IP限制状态。1或不填入(null) = IP未受限。2 = 仅限受信任IP访问。
                ipAddress:
                  type: string
                  example: 69.210.67.14
                  description: Insert static IP in batch, separated by commas.
                  x-description-cn: 可批量填入IP，以逗号区隔
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Add IP Restriction for Sub-Account API key
          x-description-cn: 为子账户 API Key 添加 IP 限制
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: "2"
                  ipList:
                    type: array
                    items:
                      type: string
                      example: 69.210.67.14
                  updateTime:
                    type: integer
                    example: 1636371437000
                    format: int64
                  apiKey:
                    type: string
                    example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
  /sapi/v1/sub-account/subAccountApi:
    post:
      summary: Create Sub-account API Key (For Master Account) (USER_DATA)
      x-summary-cn: 创建子账户API Key (适用母账户) (USER_DATA)
      description: Create a new API Key for a sub-account.
      x-description-cn: 为子账户创建新的 API Key。
      tags:
        - api-management
      operationId: createSubAccountApiKey
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#create-sub-account-api-key
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/createSubAccountApiKey.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/create_sub_account_api_key.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/create_sub_account_api_key.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/CreateSubAccountApiKeyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/CreateSubAccountApiKey/CreateSubAccountApiKey.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/CreateSubAccountApiKeyExample.php
      x-security-type: USER_DATA
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
        - `status=2` requires `ipAddress`
        - `status=3` requires `thirdPartyName`
        - Asset Sub Account is not supported
        - The caller must pass the KYC IP restriction check
      x-parameters-notes-cn: |-
        - `status=2` 时 `ipAddress` 为必填
        - `status=3` 时 `thirdPartyName` 为必填
        - 不支持资管子账号（Asset Sub Account）操作
        - 调用者须通过 KYC IP 限制校验
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - apiName
                - status
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
                  description: Sub-account email
                  x-description-cn: 子账户邮箱
                apiName:
                  type: string
                  example: myKey
                  description: API Key name
                  x-description-cn: API Key 名称
                status:
                  type: integer
                  example: 2
                  format: int64
                  description: >-
                    IP restriction status. 1 = unrestricted, 2 = restricted to trusted IPs, 3 = third-party IP
                    restriction
                  x-description-cn: IP 限制状态。1 = 无限制，2 = 限定 IP，3 = 第三方 IP 限制
                canTrade:
                  type: boolean
                  example: true
                  description: Spot & Margin trading permission, default false
                  x-description-cn: 现货/杠杆交易权限，默认 false
                canMarginLoanRepay:
                  type: boolean
                  example: false
                  description: Margin borrow/repay permission, default false
                  x-description-cn: 杠杆借还款权限，默认 false
                canFuturesTrade:
                  type: boolean
                  example: false
                  description: Futures trading permission, default false
                  x-description-cn: 合约交易权限，默认 false
                canUniversalTransfer:
                  type: boolean
                  example: false
                  description: Universal transfer permission, default false
                  x-description-cn: 万能划转权限，默认 false
                canVanillaOptions:
                  type: boolean
                  example: false
                  description: Vanilla options permission, default false
                  x-description-cn: 欧式期权权限，默认 false
                canFixApiTrading:
                  type: boolean
                  example: true
                  description: >-
                    FIX API Trading permission. Only supported for API Keys using an Ed25519 public key. Setting it to
                    `true` for any other key type returns `-9000` `Unsupported operation`
                  x-description-cn: >-
                    FIX API Trading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported
                    operation`
                canFixApiReading:
                  type: boolean
                  example: false
                  description: >-
                    FIX API Reading permission. Only supported for API Keys using an Ed25519 public key. Setting it to
                    `true` for any other key type returns `-9000` `Unsupported operation`
                  x-description-cn: >-
                    FIX API Reading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported
                    operation`
                ipAddress:
                  type: string
                  example: 69.210.67.14
                  description: Required when status=2. IP address list, max 500 chars
                  x-description-cn: status=2 时必填。IP 地址列表，最长 500 个字符
                thirdPartyName:
                  type: string
                  example: thirdParty
                  description: Required when status=3. Third-party name
                  x-description-cn: status=3 时必填。第三方名称
                publicKey:
                  type: string
                  example: ""
                  description: Ed25519 public key (optional, for Ed25519 type API Key)
                  x-description-cn: Ed25519 公钥（可选，用于 Ed25519 类型 API Key）
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Create Sub-account API Key
          x-description-cn: 创建子账户 API Key
          content:
            application/json:
              schema:
                type: object
                properties:
                  apiName:
                    type: string
                    example: myKey
                  apiKey:
                    type: string
                    example: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
                  secretKey:
                    type: string
                    example: NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j
                    description: Secret Key. Returned only once on creation, please keep it safe.
                    x-description-cn: Secret Key，仅创建时返回一次，请妥善保存
                  canTrade:
                    type: boolean
                    example: true
                  canMarginLoanRepay:
                    type: boolean
                    example: false
                  canFuturesTrade:
                    type: boolean
                    example: false
                  canUniversalTransfer:
                    type: boolean
                    example: false
                  canVanillaOptions:
                    type: boolean
                    example: false
                  canFixApiTrading:
                    type: boolean
                    example: true
                  canFixApiReading:
                    type: boolean
                    example: false
                  status:
                    type: integer
                    example: 2
                    format: int64
                  ipList:
                    type: array
                    items:
                      type: string
                      example: 69.210.67.14
    delete:
      summary: Delete Sub-account API Key (For Master Account) (USER_DATA)
      x-summary-cn: 删除子账户API Key (适用母账户) (USER_DATA)
      description: Delete an API Key of a sub-account.
      x-description-cn: 删除子账户的 API Key。
      tags:
        - api-management
      operationId: deleteSubAccountApiKey
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#delete-sub-account-api-key
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/deleteSubAccountApiKey.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/delete_sub_account_api_key.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/delete_sub_account_api_key.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/DeleteSubAccountApiKeyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/DeleteSubAccountApiKey/DeleteSubAccountApiKey.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/DeleteSubAccountApiKeyExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 3000
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to: https://www.binance.com/en/support/faq/detail/360002502072.
          x-description-cn: 访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：https://www.binance.com/cn/support/faq/detail/360002502072。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
          description: Sub-account email
          x-description-cn: 子账户邮箱
        - name: subAccountApiKey
          in: query
          required: true
          schema:
            type: string
            example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
          description: The sub-account API Key to be deleted
          x-description-cn: 要删除的子账户 API Key
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - Asset Sub Account is not supported
        - The caller must pass the KYC IP restriction check
      x-parameters-notes-cn: |-
        - 不支持资管子账号（Asset Sub Account）操作
        - 调用者须通过 KYC IP 限制校验
      responses:
        "200":
          description: Delete Sub-account API Key
          x-description-cn: 删除子账户 API Key
          content:
            application/json:
              schema:
                type: object
                description: Empty object on success
                x-description-cn: 删除成功时返回空对象
                example: {}
    get:
      summary: Query Sub-account API Key (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户API Key (适用母账户) (USER_DATA)
      description: Query the API Key list of a sub-account.
      x-description-cn: 查询子账户的 API Key 列表。
      tags:
        - api-management
      operationId: querySubAccountApiKey
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#query-sub-account-api-key
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/querySubAccountApiKey.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/query_sub_account_api_key.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/query_sub_account_api_key.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/QuerySubAccountApiKeyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/QuerySubAccountApiKey/QuerySubAccountApiKey.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/QuerySubAccountApiKeyExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 3000
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to: https://www.binance.com/en/support/faq/detail/360002502072.
          x-description-cn: 访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：https://www.binance.com/cn/support/faq/detail/360002502072。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
          description: Sub-account email
          x-description-cn: 子账户邮箱
        - name: subAccountApiKey
          in: query
          required: false
          schema:
            type: string
            example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
          description: Specify an API Key for exact match
          x-description-cn: 指定 API Key 进行精确查询
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
            minimum: 1
          description: Page number, default 1, minimum 1
          x-description-cn: 页码，默认 1，最小 1
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 30
            format: int64
            default: 30
            maximum: 100
          description: Page size, default 30, maximum 100
          x-description-cn: 每页数量，默认 30，最大 100
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Query Sub-account API Key
          x-description-cn: 查询子账户 API Key
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 1
                    format: int64
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          example: 123@test.com
                        apiName:
                          type: string
                          example: myKey
                        apikey:
                          type: string
                          example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
                        canTrade:
                          type: boolean
                          example: true
                        canMarginLoanRepay:
                          type: boolean
                          example: false
                        canFuturesTrade:
                          type: boolean
                          example: false
                        canUniversalTransfer:
                          type: boolean
                          example: false
                        canVanillaOptions:
                          type: boolean
                          example: false
                        canFixApiTrading:
                          type: boolean
                          example: true
                        canFixApiReading:
                          type: boolean
                          example: false
                        timestamp:
                          type: integer
                          example: 1640000000000
                          format: int64
  /sapi/v2/sub-account/subAccountApi:
    post:
      summary: Create Sub-account API Key V2 (For Master Account) (USER_DATA)
      x-summary-cn: 创建子账户API Key V2 (适用母账户) (USER_DATA)
      description: Create a new API Key for a sub-account.
      x-description-cn: 为子账户创建新的 API Key。
      tags:
        - api-management
      operationId: createSubAccountApiKeyV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#create-sub-account-api-key-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/createSubAccountApiKeyV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/create_sub_account_api_key_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/create_sub_account_api_key_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/CreateSubAccountApiKeyV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/CreateSubAccountApiKeyV2/CreateSubAccountApiKeyV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/CreateSubAccountApiKeyV2Example.php
      x-security-type: USER_DATA
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
        - `status=2` requires `ipAddress`

        - `status=3` requires `thirdPartyName`

        - Asset Sub Account is not supported

        - The caller must pass the KYC IP restriction check

        - `publicKey` is rejected if passed in the URL query string. The example sends it in the request body with
        `--data-urlencode`
      x-parameters-notes-cn: |-
        - `status=2` 时 `ipAddress` 为必填
        - `status=3` 时 `thirdPartyName` 为必填
        - 不支持资管子账号（Asset Sub Account）操作
        - 调用者须通过 KYC IP 限制校验
        - `publicKey` 放在 URL 查询串中会直接报错，示例中使用 `--data-urlencode` 放在请求体中
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - apiName
                - status
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
                  description: Sub-account email
                  x-description-cn: 子账户邮箱
                apiName:
                  type: string
                  example: my-fix-api
                  description: API Key name
                  x-description-cn: API Key 名称
                status:
                  type: integer
                  example: 2
                  format: int64
                  description: >-
                    IP restriction status. 1 = unrestricted, 2 = restricted to trusted IPs, 3 = third-party IP
                    restriction
                  x-description-cn: IP 限制状态。1 = 无限制，2 = 限定 IP，3 = 第三方 IP 限制
                canTrade:
                  type: boolean
                  example: true
                  description: Spot & Margin trading permission, default false
                  x-description-cn: 现货/杠杆交易权限，默认 false
                canMarginLoanRepay:
                  type: boolean
                  example: false
                  description: Margin borrow/repay permission, default false
                  x-description-cn: 杠杆借还款权限，默认 false
                canFuturesTrade:
                  type: boolean
                  example: false
                  description: Futures trading permission, default false
                  x-description-cn: 合约交易权限，默认 false
                canUniversalTransfer:
                  type: boolean
                  example: false
                  description: Universal transfer permission, default false
                  x-description-cn: 万能划转权限，默认 false
                canVanillaOptions:
                  type: boolean
                  example: false
                  description: Vanilla options permission, default false
                  x-description-cn: 欧式期权权限，默认 false
                canFixApiTrading:
                  type: boolean
                  example: true
                  description: >-
                    FIX API Trading permission. Only supported for API Keys using an Ed25519 public key. Setting it to
                    `true` for any other key type returns `-9000` `Unsupported operation`
                  x-description-cn: >-
                    FIX API Trading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported
                    operation`
                canFixApiReading:
                  type: boolean
                  example: true
                  description: >-
                    FIX API Reading permission. Only supported for API Keys using an Ed25519 public key. Setting it to
                    `true` for any other key type returns `-9000` `Unsupported operation`
                  x-description-cn: >-
                    FIX API Reading 权限。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported
                    operation`
                ipAddress:
                  type: string
                  example: 1.2.3.4
                  description: Required when status=2. IP address list, max 500 chars
                  x-description-cn: status=2 时必填。IP 地址列表，最长 500 个字符
                thirdPartyName:
                  type: string
                  example: thirdParty
                  description: Required when status=3. Third-party name
                  x-description-cn: status=3 时必填。第三方名称
                publicKey:
                  type: string
                  example: |-
                    -----BEGIN PUBLIC KEY-----
                    MCowBQYDK2VwAyEAptEM59ao3nOD2baduIA830qZU4k4mqfvv7PwHVAfZhg=
                    -----END PUBLIC KEY-----
                  description: >-
                    RSA or Ed25519 public key (optional). Must be sent in the request body; it is rejected if passed in
                    the URL query string
                  x-description-cn: RSA 或 Ed25519 公钥（可选）。必须放在请求体中，放在 URL 查询串中会被拒绝
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Create Sub-account API Key V2
          x-description-cn: 创建子账户 API Key V2
          content:
            application/json:
              schema:
                type: object
                properties:
                  apiName:
                    type: string
                    example: myKey
                  apiKey:
                    type: string
                    example: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
                  secretKey:
                    type: string
                    example: NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j
                    description: Secret Key. Returned only once on creation, please keep it safe.
                    x-description-cn: Secret Key，仅创建时返回一次，请妥善保存
                  canTrade:
                    type: boolean
                    example: true
                  canMarginLoanRepay:
                    type: boolean
                    example: false
                  canFuturesTrade:
                    type: boolean
                    example: false
                  canUniversalTransfer:
                    type: boolean
                    example: false
                  canVanillaOptions:
                    type: boolean
                    example: false
                  canFixApiTrading:
                    type: boolean
                    example: true
                  canFixApiReading:
                    type: boolean
                    example: false
                  status:
                    type: integer
                    example: 2
                    format: int64
                  ipList:
                    type: array
                    items:
                      type: string
                      example: 69.210.67.14
  /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList:
    delete:
      summary: Delete IP List For a Sub-account API Key (For Master Account) (USER_DATA)
      x-summary-cn: 删除子账户API Key IP白名单 (适用母账户) (USER_DATA)
      description: Delete IP List For a Sub-account API Key
      x-description-cn: 删除子账户API Key IP白名单
      tags:
        - api-management
      operationId: deleteIpListForASubAccountApiKey
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#delete-ip-list-for-asub-account-api-key
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/deleteIpListForASubAccountApiKey.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/delete_ip_list_for_a_sub_account_api_key.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/delete_ip_list_for_a_sub_account_api_key.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/DeleteIpListForASubAccountApiKeyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/DeleteIpListForASubAccountApiKey/DeleteIpListForASubAccountApiKey.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/DeleteIpListForASubAccountApiKeyExample.php
      x-security-type: USER_DATA
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: subAccountApiKey
          in: query
          required: true
          schema:
            type: string
            example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
        - name: ipAddress
          in: query
          required: true
          schema:
            type: string
            example: 69.210.67.14
          description: IPs to be deleted. Can be added in batches, separated by commas
          x-description-cn: 想删除的 IP。可批量删除，用逗号分隔
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- You need to enable Enable Spot & Margin Trading option for the api key which requests this endpoint"
      x-parameters-notes-cn: "- 调用此端口前需要在api管理页开启允许现货及杠杆交易选项"
      responses:
        "200":
          description: Delete IP List For a Sub-account API Key
          x-description-cn: 删除子账户 API Key 的 IP 白名单
          content:
            application/json:
              schema:
                type: object
                properties:
                  ipRestrict:
                    type: string
                    example: "true"
                  ipList:
                    type: array
                    items:
                      type: string
                      example: 69.210.67.14
                  updateTime:
                    type: integer
                    example: 1636371437000
                    format: int64
                  apiKey:
                    type: string
                    example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
  /sapi/v1/sub-account/subAccountApi/ipRestriction:
    get:
      summary: Get IP Restriction for a Sub-account API Key (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户API Key IP白名单 (适用母账户) (USER_DATA)
      description: Get IP Restriction for a Sub-account API Key
      x-description-cn: 查询子账户API Key IP白名单
      tags:
        - api-management
      operationId: getIpRestrictionForASubAccountApiKey
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#get-ip-restriction-for-asub-account-api-key
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/getIpRestrictionForASubAccountApiKey.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/get_ip_restriction_for_a_sub_account_api_key.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/get_ip_restriction_for_a_sub_account_api_key.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/GetIpRestrictionForASubAccountApiKeyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/GetIpRestrictionForASubAccountApiKey/GetIpRestrictionForASubAccountApiKey.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/GetIpRestrictionForASubAccountApiKeyExample.php
      x-security-type: USER_DATA
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: subAccountApiKey
          in: query
          required: true
          schema:
            type: string
            example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get IP Restriction for a Sub-account API Key
          x-description-cn: 查询子账户 API Key 的 IP 限制
          content:
            application/json:
              schema:
                type: object
                properties:
                  ipRestrict:
                    type: string
                    example: "true"
                  ipList:
                    type: array
                    items:
                      type: string
                      example: 69.210.67.14
                  updateTime:
                    type: integer
                    example: 1636371437000
                    format: int64
                  apiKey:
                    type: string
                    example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
  /sapi/v1/sub-account/subAccountApiPermission:
    post:
      summary: Modify Sub-account API Key Permission (For Master Account) (USER_DATA)
      x-summary-cn: 修改子账户API Key权限 (适用母账户) (USER_DATA)
      description: Modify the trading permissions of a sub-account API Key.
      x-description-cn: 修改子账户 API Key 的交易权限。
      tags:
        - api-management
      operationId: modifySubAccountApiKeyPermission
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/api-management#modify-sub-account-api-key-permission
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ApiManagementApi/modifySubAccountApiKeyPermission.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/api_management_api/modify_sub_account_api_key_permission.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ApiManagement/modify_sub_account_api_key_permission.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/apimanagement/ModifySubAccountApiKeyPermissionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ApiManagementAPI/ModifySubAccountApiKeyPermission/ModifySubAccountApiKeyPermission.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/apimanagement/ModifySubAccountApiKeyPermissionExample.php
      x-security-type: USER_DATA
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
        - Portfolio Margin Retail User is not supported
        - Asset Sub Account is not supported
        - The caller must pass the KYC IP restriction check
      x-parameters-notes-cn: |-
        - 不支持 Portfolio Margin 零售账号（Portfolio Margin Retail User）操作
        - 不支持资管子账号（Asset Sub Account）操作
        - 调用者须通过 KYC IP 限制校验
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - subAccountApiKey
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
                  description: Sub-account email
                  x-description-cn: 子账户邮箱
                subAccountApiKey:
                  type: string
                  example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
                  description: Sub-account API Key
                  x-description-cn: 子账户 API Key
                canTrade:
                  type: boolean
                  example: true
                  description: Spot & Margin trading permission
                  x-description-cn: 现货/杠杆交易权限
                canMarginLoanRepay:
                  type: boolean
                  example: false
                  description: Margin borrow/repay permission
                  x-description-cn: 杠杆借还款权限
                canFuturesTrade:
                  type: boolean
                  example: true
                  description: Futures trading permission
                  x-description-cn: 合约交易权限
                canUniversalTransfer:
                  type: boolean
                  example: false
                  description: Universal transfer permission
                  x-description-cn: 万能划转权限
                canVanillaOptions:
                  type: boolean
                  example: false
                  description: Vanilla options permission
                  x-description-cn: 欧式期权权限
                canFixApiTrading:
                  type: boolean
                  example: true
                  description: >-
                    FIX API Trading permission. If omitted, the existing value is unchanged. Only supported for API Keys
                    using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000`
                    `Unsupported operation`
                  x-description-cn: >-
                    FIX API Trading 权限。不传则不修改。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported
                    operation`
                canFixApiReading:
                  type: boolean
                  example: false
                  description: >-
                    FIX API Reading permission. If omitted, the existing value is unchanged. Only supported for API Keys
                    using an Ed25519 public key. Setting it to `true` for any other key type returns `-9000`
                    `Unsupported operation`
                  x-description-cn: >-
                    FIX API Reading 权限。不传则不修改。仅支持使用 Ed25519 公钥的 API Key。其他类型的 key 设置为 `true` 时返回 `-9000` `Unsupported
                    operation`
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Modify Sub-account API Key Permission
          x-description-cn: 修改子账户 API Key 权限
          content:
            application/json:
              schema:
                type: object
                properties:
                  apiName:
                    type: string
                    example: myKey
                  apikey:
                    type: string
                    example: k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf
                  canTrade:
                    type: boolean
                    example: true
                  canMarginLoanRepay:
                    type: boolean
                    example: false
                  canFuturesTrade:
                    type: boolean
                    example: true
                  canUniversalTransfer:
                    type: boolean
                    example: false
                  canVanillaOptions:
                    type: boolean
                    example: false
                  canFixApiTrading:
                    type: boolean
                    example: true
                  canFixApiReading:
                    type: boolean
                    example: false
                  timestamp:
                    type: integer
                    example: 1640000000000
                    format: int64
  /sapi/v1/sub-account/futures/transfer:
    post:
      summary: Futures Transfer for Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 子账户合约划转 (仅适用主账户) (USER_DATA)
      description: Futures Transfer for Sub-account
      x-description-cn: 子账户合约划转
      tags:
        - asset-management
      operationId: futuresTransferForSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#futures-transfer-for-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/futuresTransferForSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/futures_transfer_for_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/futures_transfer_for_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/FuturesTransferForSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/FuturesTransferForSubAccount/FuturesTransferForSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/FuturesTransferForSubAccountExample.php
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
      x-parameters-notes: "- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint."
      x-parameters-notes-cn: "- 您需要为调用此接口的 API Key 开通“允许现货及杠杆交易”权限。"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - asset
                - amount
                - type
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
                asset:
                  type: string
                  example: USDT
                  description: The asset being transferred
                  x-description-cn: 划转的资产
                amount:
                  type: number
                  example: "1.0"
                  format: float
                  description: The amount to be transferred
                  x-description-cn: 划转数量
                type:
                  type: integer
                  example: 1
                  format: int64
                  description: |-
                    1: transfer from subaccount's spot account to its USDT-margined futures account 2: transfer from
                    subaccount's USDT-margined futures account to its spot account 3: transfer from subaccount's spot
                    account to its COIN-margined futures account 4: transfer from subaccount's COIN-margined futures
                    account to its spot account
                  x-description-cn: "1: 子账户现货账户划转到其 U 本位合约账户 2: 子账户 U 本位合约账户划转到其现货账户 3: 子账户现货账户划转到其币本位合约账户 4: 子账户币本位合约账户划转到其现货账户"
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Futures Transfer for Sub-account
          x-description-cn: 子账户合约划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  txnId:
                    type: string
                    example: "2966662589"
  /sapi/v1/sub-account/futures/account:
    get:
      summary: Get Detail on Sub-account's Futures Account (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约账户详情 (适用主账户) (USER_DATA)
      description: Get Detail on Sub-account's Futures Account
      x-description-cn: 查询子账户合约账户详情
      tags:
        - asset-management
      operationId: getDetailOnSubAccountsFuturesAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-detail-on-sub-accounts-futures-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getDetailOnSubAccountsFuturesAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_detail_on_sub_accounts_futures_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_detail_on_sub_accounts_futures_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetDetailOnSubAccountsFuturesAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetDetailOnSubAccountsFuturesAccount/GetDetailOnSubAccountsFuturesAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetDetailOnSubAccountsFuturesAccountExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Detail on Sub-account's Futures Account
          x-description-cn: 查询子账户合约账户详情
          content:
            application/json:
              schema:
                type: object
                properties:
                  email:
                    type: string
                    example: abc@test.com
                  asset:
                    type: string
                    example: USDT
                  assets:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                        initialMargin:
                          type: string
                          example: "0.00000000"
                        maintenanceMargin:
                          type: string
                          example: "0.00000000"
                        marginBalance:
                          type: string
                          example: "0.88308000"
                        maxWithdrawAmount:
                          type: string
                          example: "0.88308000"
                        openOrderInitialMargin:
                          type: string
                          example: "0.00000000"
                        positionInitialMargin:
                          type: string
                          example: "0.00000000"
                        unrealizedProfit:
                          type: string
                          example: "0.00000000"
                        walletBalance:
                          type: string
                          example: "0.88308000"
                  canDeposit:
                    type: boolean
                    example: true
                  canTrade:
                    type: boolean
                    example: true
                  canWithdraw:
                    type: boolean
                    example: true
                  feeTier:
                    type: integer
                    example: 2
                    format: int64
                  maxWithdrawAmount:
                    type: string
                    example: "0.88308000"
                  totalInitialMargin:
                    type: string
                    example: "0.00000000"
                  totalMaintenanceMargin:
                    type: string
                    example: "0.00000000"
                  totalMarginBalance:
                    type: string
                    example: "0.88308000"
                  totalOpenOrderInitialMargin:
                    type: string
                    example: "0.00000000"
                  totalPositionInitialMargin:
                    type: string
                    example: "0.00000000"
                  totalUnrealizedProfit:
                    type: string
                    example: "0.00000000"
                  totalWalletBalance:
                    type: string
                    example: "0.88308000"
                  updateTime:
                    type: integer
                    example: 1576756674610
                    format: int64
  /sapi/v2/sub-account/futures/account:
    get:
      summary: Get Detail on Sub-account's Futures Account V2 (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约账户详情 V2 (适用主账户) (USER_DATA)
      description: Get Detail on Sub-account's Futures Account
      x-description-cn: 查询子账户合约账户详情
      tags:
        - asset-management
      operationId: getDetailOnSubAccountsFuturesAccountV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-detail-on-sub-accounts-futures-account-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getDetailOnSubAccountsFuturesAccountV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_detail_on_sub_accounts_futures_account_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_detail_on_sub_accounts_futures_account_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetDetailOnSubAccountsFuturesAccountV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetDetailOnSubAccountsFuturesAccountV2/GetDetailOnSubAccountsFuturesAccountV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetDetailOnSubAccountsFuturesAccountV2Example.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: futuresType
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: "1: USDT-margined Futures，2: Coin-margined Futures"
          x-description-cn: "1: USDT合约，2: 币本位合约"
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Detail on Sub-account's Futures Account V2
          x-description-cn: 查询子账户合约账户详情 V2
          content:
            application/json:
              schema:
                type: object
                properties:
                  futureAccountResp:
                    type: object
                    properties:
                      email:
                        type: string
                        example: abc@test.com
                      assets:
                        type: array
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: USDT
                            initialMargin:
                              type: string
                              example: "0.00000000"
                            maintenanceMargin:
                              type: string
                              example: "0.00000000"
                            marginBalance:
                              type: string
                              example: "0.88308000"
                            maxWithdrawAmount:
                              type: string
                              example: "0.88308000"
                            openOrderInitialMargin:
                              type: string
                              example: "0.00000000"
                            positionInitialMargin:
                              type: string
                              example: "0.00000000"
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                            walletBalance:
                              type: string
                              example: "0.88308000"
                      canDeposit:
                        type: boolean
                        example: true
                      canTrade:
                        type: boolean
                        example: true
                      canWithdraw:
                        type: boolean
                        example: true
                      feeTier:
                        type: integer
                        example: 2
                        format: int64
                      maxWithdrawAmount:
                        type: string
                        example: "0.88308000"
                      totalInitialMargin:
                        type: string
                        example: "0.00000000"
                      totalMaintenanceMargin:
                        type: string
                        example: "0.00000000"
                      totalMarginBalance:
                        type: string
                        example: "0.88308000"
                      totalOpenOrderInitialMargin:
                        type: string
                        example: "0.00000000"
                      totalPositionInitialMargin:
                        type: string
                        example: "0.00000000"
                      totalUnrealizedProfit:
                        type: string
                        example: "0.00000000"
                      totalWalletBalance:
                        type: string
                        example: "0.88308000"
                      updateTime:
                        type: integer
                        example: 1576756674610
                        format: int64
                  deliveryAccountResp:
                    type: object
                    properties:
                      email:
                        type: string
                        example: abc@test.com
                      assets:
                        type: array
                        items:
                          type: object
                          properties:
                            asset:
                              type: string
                              example: BTC
                            initialMargin:
                              type: string
                              example: "0.00000000"
                            maintenanceMargin:
                              type: string
                              example: "0.00000000"
                            marginBalance:
                              type: string
                              example: "0.88308000"
                            maxWithdrawAmount:
                              type: string
                              example: "0.88308000"
                            openOrderInitialMargin:
                              type: string
                              example: "0.00000000"
                            positionInitialMargin:
                              type: string
                              example: "0.00000000"
                            unrealizedProfit:
                              type: string
                              example: "0.00000000"
                            walletBalance:
                              type: string
                              example: "0.88308000"
                      canDeposit:
                        type: boolean
                        example: true
                      canTrade:
                        type: boolean
                        example: true
                      canWithdraw:
                        type: boolean
                        example: true
                      feeTier:
                        type: integer
                        example: 2
                        format: int64
                      updateTime:
                        type: integer
                        example: 1598959682001
                        format: int64
  /sapi/v1/sub-account/margin/account:
    get:
      summary: Get Detail on Sub-account's Margin Account (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户杠杆账户详情 (适用主账户) (USER_DATA)
      description: Get Detail on Sub-account's Margin Account
      x-description-cn: 查询子账户杠杆账户详情
      tags:
        - asset-management
      operationId: getDetailOnSubAccountsMarginAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-detail-on-sub-accounts-margin-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getDetailOnSubAccountsMarginAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_detail_on_sub_accounts_margin_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_detail_on_sub_accounts_margin_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetDetailOnSubAccountsMarginAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetDetailOnSubAccountsMarginAccount/GetDetailOnSubAccountsMarginAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetDetailOnSubAccountsMarginAccountExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Detail on Sub-account's Margin Account
          x-description-cn: 查询子账户杠杆账户详情
          content:
            application/json:
              schema:
                type: object
                properties:
                  email:
                    type: string
                    example: 123@test.com
                  marginLevel:
                    type: string
                    example: "11.64405625"
                  totalAssetOfBtc:
                    type: string
                    example: "6.82728457"
                  totalLiabilityOfBtc:
                    type: string
                    example: "0.58633215"
                  totalNetAssetOfBtc:
                    type: string
                    example: "6.24095242"
                  marginTradeCoeffVo:
                    type: object
                    properties:
                      forceLiquidationBar:
                        type: string
                        example: "1.10000000"
                        description: Liquidation margin ratio
                        x-description-cn: 强平风险率
                      marginCallBar:
                        type: string
                        example: "1.50000000"
                        description: Margin call margin ratio
                        x-description-cn: 补仓风险率
                      normalBar:
                        type: string
                        example: "2.00000000"
                        description: Initial margin ratio
                        x-description-cn: 初始风险率
                  marginUserAssetVoList:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: BTC
                        borrowed:
                          type: string
                          example: "0.00000000"
                        free:
                          type: string
                          example: "0.00499500"
                        interest:
                          type: string
                          example: "0.00000000"
                        locked:
                          type: string
                          example: "0.00000000"
                        netAsset:
                          type: string
                          example: "0.00499500"
  /sapi/v1/sub-account/futures/move-position:
    get:
      summary: Get Move Position History for Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 查询账户移仓历史 (适用主账户) (USER_DATA)
      description: Query move position history
      x-description-cn: 查询账户移仓历史
      tags:
        - asset-management
      operationId: getMovePositionHistoryForSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-move-position-history-for-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getMovePositionHistoryForSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_move_position_history_for_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_move_position_history_for_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetMovePositionHistoryForSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetMovePositionHistoryForSubAccount/GetMovePositionHistoryForSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetMovePositionHistoryForSubAccountExample.php
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
        - name: productType
          in: query
          required: false
          schema:
            type: string
            example: UM
            enum:
              - UM
              - OPTION
          description: Default UM.
          x-description-cn: 默认 UM。
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
        - name: page
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
        - name: rows
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
            maximum: 100
          description: Max 100.
          x-description-cn: 最大 100。
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - If `startTime` and `endTime` are both omitted, records from the last 90 days are returned by default (up to
        100 records).

        - If `startTime` is sent and `endTime` is omitted, records in `[max(startTime, now-90d), now]` are returned.

        - If `startTime` is omitted and `endTime` is sent, records in `[max(now, endTime-90d), endTime]` are returned.
      x-parameters-notes-cn: |-
        - 如果 `startTime` 和 `endTime` 都未传，默认返回最近 90 天内最多 100 条记录。
        - 如果传了 `startTime` 但未传 `endTime`，返回 `[max(startTime, now-90d), now]` 范围内的记录。
        - 如果未传 `startTime` 但传了 `endTime`，返回 `[max(now, endTime-90d), endTime]` 范围内的记录。
      responses:
        "200":
          description: Get Move Position History for Sub-account
          x-description-cn: 查询子账户移仓历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 3
                    format: int64
                  futureMovePositionOrderVoList:
                    type: array
                    items:
                      type: object
                      properties:
                        fromUserEmail:
                          type: string
                          example: testFrom@google.com
                        toUserEmail:
                          type: string
                          example: testTo@google.com
                        productType:
                          type: string
                          example: UM
                        symbol:
                          type: string
                          example: BTCUSDT
                        price:
                          type: string
                          example: "105025.50981609"
                        quantity:
                          type: string
                          example: "0.00100000"
                        positionSide:
                          type: string
                          example: BOTH
                        side:
                          type: string
                          example: SELL
                        timeStamp:
                          type: integer
                          example: 1737544712000
                          format: int64
    post:
      summary: Move Position for Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 移仓功能 (适用主账户) (USER_DATA)
      description: Move position between sub-master, master-sub, or sub-sub accounts when necessary
      x-description-cn: 支持主账户和母账户，子账户和子账户之间的移仓
      tags:
        - asset-management
      operationId: movePositionForSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#move-position-for-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/movePositionForSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/move_position_for_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/move_position_for_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/MovePositionForSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/MovePositionForSubAccount/MovePositionForSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/MovePositionForSubAccountExample.php
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
      x-parameters-notes: >-
        - You need to enable the `Trading` permission for the API key used to call this endpoint.

        - This function is only available for VIP levels 7-9.

        - Only master accounts can call this endpoint.

        - `quantity` must be a positive number.

        - Supported account types: normal account, PM PRO, PM PRO SPAN, and PM Retail.

        - The source account must have positions.

        - For orders in the same `orderArgs` request, if any symbol's total close position quantity exceeds current
        position quantity, all orders in that batch fail.

        - Only cross margin mode is supported.

        - The move position price supports `MARK_PRICE` only.

        - MSA is not supported.

        - Symbols configured with `Reduce-Only` are not supported.
      x-parameters-notes-cn: |-
        - 您需要为调用此接口的 API Key 开通 `Trading` 权限。
        - 该功能仅支持 VIP 7-9。
        - 仅母账户可调用此接口。
        - `quantity` 必须为正数。
        - 支持普通账户、PM PRO、PM PRO SPAN 和 PM Retail 的仓位转移。
        - 仅当源账户存在仓位时可调用此接口。
        - 对同一个 `orderArgs` 请求，若任一 `symbol` 的平仓总量大于该 `symbol` 当前持仓量，则该批次全部订单失败。
        - 仅支持全仓模式。
        - 移仓价格仅支持 `MARK_PRICE`。
        - 不支持 MSA。
        - 设置了 `Reduce-Only` 的 `symbol` 不支持该功能。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - fromUserEmail
                - toUserEmail
                - productType
                - orderArgs
                - timestamp
              properties:
                fromUserEmail:
                  type: string
                  example: testFrom@google.com
                toUserEmail:
                  type: string
                  example: testTo@google.com
                productType:
                  type: string
                  example: UM
                  enum:
                    - UM
                    - OPTION
                  description: A single request cannot mix UM and OPTION positions.
                  x-description-cn: 单次请求不支持 UM 和 OPTION 混合提交。
                orderArgs:
                  type: array
                  items:
                    type: object
                    properties:
                      symbol:
                        type: string
                        example: BTCUSDT
                      quantity:
                        type: number
                        example: "0.001"
                        format: float
                      positionSide:
                        type: string
                        example: BOTH
                        description: >-
                          Required when productType=UM. Optional and ignored when productType=OPTION (the response
                          returns positionSide as null).
                        x-description-cn: productType=UM 时必填；productType=OPTION 时可选且会被忽略（响应中 positionSide 返回 null）。
                  description: |-
                    Max 10 positions supported. When input request parameter,orderArgs.symbol should be STRING,
                    orderArgs.quantity should be BIGDECIMAL, and orderArgs.positionSide should be STRING, positionSide
                    support BOTH,LONG and SHORT. Each entry should be like
                    orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. Example of
                    the request parameter array: orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001
                    orderArgs[0].positionSide=BOTH orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01
                    orderArgs[1].positionSide=BOTH
                  x-description-cn: |-
                    一次最多支持 10 个仓位转移. orderArgs.symbol的参数类型为STRING, orderArgs.quantity的参数类型为BIGDECIMAL,
                    orderArgs.positionSide的参数类型为STRING, positionSide 支持 BOTH,LONG and SHORT. 请求参数格式如下
                    orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. 举例:
                    orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001 orderArgs[0].positionSide=BOTH
                    orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01 orderArgs[1].positionSide=BOTH
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Move Position for Sub-account
          x-description-cn: 子账户移仓
          content:
            application/json:
              schema:
                type: object
                properties:
                  movePositionOrders:
                    type: array
                    items:
                      type: object
                      properties:
                        fromUserEmail:
                          type: string
                          example: testFrom@google.com
                        toUserEmail:
                          type: string
                          example: testTo@google.com
                        productType:
                          type: string
                          example: UM
                        symbol:
                          type: string
                          example: BTCUSDT
                        priceType:
                          type: string
                          example: MARK_PRICE
                        price:
                          type: string
                          example: "97139.00000000"
                        quantity:
                          type: string
                          example: "0.001"
                        positionSide:
                          type: string
                          example: BOTH
                          nullable: true
                          description: null when productType=OPTION.
                          x-description-cn: productType=OPTION 时返回 null。
                        side:
                          type: string
                          example: BUY
                        success:
                          type: boolean
                          example: true
  /sapi/v1/capital/deposit/subAddress:
    get:
      summary: Get Sub-account Deposit Address (For Master Account) (USER_DATA)
      x-summary-cn: 获取子账户充值地址 (适用主账户) (USER_DATA)
      description: Fetch sub-account deposit address
      x-description-cn: 获取子账户充值地址
      tags:
        - asset-management
      operationId: getSubAccountDepositAddress
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-sub-account-deposit-address
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getSubAccountDepositAddress.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_sub_account_deposit_address.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_sub_account_deposit_address.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetSubAccountDepositAddressExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetSubAccountDepositAddress/GetSubAccountDepositAddress.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetSubAccountDepositAddressExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: coin
          in: query
          required: true
          schema:
            type: string
            example: BTC
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
          description: networks can be found in `GET /sapi/v1/capital/deposit/address`
          x-description-cn: 网络可以在`GET /sapi/v1/capital/deposit/address`获取
        - name: amount
          in: query
          required: false
          schema:
            type: number
            example: "1.0"
            format: float
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: "- `amount` needs to be sent if using LIGHTNING network"
      x-parameters-notes-cn: "- 使用LIGHTNING网络时，`amount`必须传"
      responses:
        "200":
          description: Get Sub-account Deposit Address
          x-description-cn: 获取子账户充值地址
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: string
                    example: TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV
                  coin:
                    type: string
                    example: USDT
                  tag:
                    type: string
                    example: ""
                  url:
                    type: string
                    example: https://tronscan.org/#/address/TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV
  /sapi/v1/capital/deposit/subHisrec:
    get:
      summary: Get Sub-account Deposit History (For Master Account) (USER_DATA)
      x-summary-cn: 获取子账户充值记录 (适用主账户) (USER_DATA)
      description: Fetch sub-account deposit history
      x-description-cn: 获取子账户充值记录
      tags:
        - asset-management
      operationId: getSubAccountDepositHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-sub-account-deposit-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getSubAccountDepositHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_sub_account_deposit_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_sub_account_deposit_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetSubAccountDepositHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetSubAccountDepositHistory/GetSubAccountDepositHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetSubAccountDepositHistoryExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: includeSource
          in: query
          required: false
          schema:
            type: boolean
            example: false
            default: false
          description: Default `false`, return `sourceAddress` field when set to `true`
          x-description-cn: 默认 `false`，如果为`true`时会返回`sourceAddress`字段
        - name: coin
          in: query
          required: false
          schema:
            type: string
            example: BTC
        - name: status
          in: query
          required: false
          schema:
            type: integer
            example: 0
            format: int64
          description: >-
            Deposit status: 0=pending, 6=credited but cannot withdraw, 7=wrong deposit, 8=waiting user confirmation,
            1=success.
          x-description-cn: 充值状态：0=待处理，6=已入账但不可提币，7=错误充值，8=等待用户确认，1=成功。
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
            example: 1
            default: 1
            maximum: 200
            format: int64
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: 0
            default: 0
            format: int64
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
        - name: txId
          in: query
          required: false
          schema:
            type: string
            example: "1"
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
          description: Get Sub-account Deposit History
          x-description-cn: 获取子账户充值历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      example: "769800519366885376"
                    amount:
                      type: string
                      example: "0.001"
                    coin:
                      type: string
                      example: BNB
                    network:
                      type: string
                      example: BNB
                    status:
                      type: integer
                      example: 0
                      format: int64
                      description: >-
                        Deposit status: 0=pending, 6=credited but cannot withdraw, 7=wrong deposit, 8=waiting user
                        confirmation, 1=success.
                      x-description-cn: 充值状态：0=待处理，6=已入账但不可提币，7=错误充值，8=等待用户确认，1=成功。
                    address:
                      type: string
                      example: bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23
                    addressTag:
                      type: string
                      example: "101764890"
                    txId:
                      type: string
                      example: 98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC
                    insertTime:
                      type: integer
                      example: 1661493146000
                      format: int64
                    transferType:
                      type: integer
                      example: 0
                      format: int64
                    confirmTimes:
                      type: string
                      example: 1/1
                    unlockConfirm:
                      type: integer
                      example: 0
                      format: int64
                    walletType:
                      type: integer
                      example: 0
                      format: int64
  /sapi/v1/sub-account/futures/accountSummary:
    get:
      summary: Get Summary of Sub-account's Futures Account (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约账户汇总 (适用主账户) (USER_DATA)
      description: Get Summary of Sub-account's Futures Account
      x-description-cn: 查询子账户合约账户汇总
      tags:
        - asset-management
      operationId: getSummaryOfSubAccountsFuturesAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-summary-of-sub-accounts-futures-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getSummaryOfSubAccountsFuturesAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_summary_of_sub_accounts_futures_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_summary_of_sub_accounts_futures_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetSummaryOfSubAccountsFuturesAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetSummaryOfSubAccountsFuturesAccount/GetSummaryOfSubAccountsFuturesAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetSummaryOfSubAccountsFuturesAccountExample.php
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
        - name: page
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
        - name: limit
          in: query
          required: true
          schema:
            type: integer
            example: 1
            maximum: 500
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Summary of Sub-account's Futures Account
          x-description-cn: 查询子账户合约账户汇总
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalInitialMargin:
                    type: string
                    example: "9.83137400"
                  totalMaintenanceMargin:
                    type: string
                    example: "0.41568700"
                  totalMarginBalance:
                    type: string
                    example: "23.03235621"
                  totalOpenOrderInitialMargin:
                    type: string
                    example: "9.00000000"
                  totalPositionInitialMargin:
                    type: string
                    example: "0.83137400"
                  totalUnrealizedProfit:
                    type: string
                    example: "0.03219710"
                  totalWalletBalance:
                    type: string
                    example: "22.15879444"
                  asset:
                    type: string
                    example: USD
                    description: The sum of BUSD and USDT
                    x-description-cn: USDT和BUSD资产汇总
                  subAccountList:
                    type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          example: 123@test.com
                        totalInitialMargin:
                          type: string
                          example: "9.00000000"
                        totalMaintenanceMargin:
                          type: string
                          example: "0.00000000"
                        totalMarginBalance:
                          type: string
                          example: "22.12659734"
                        totalOpenOrderInitialMargin:
                          type: string
                          example: "9.00000000"
                        totalPositionInitialMargin:
                          type: string
                          example: "0.00000000"
                        totalUnrealizedProfit:
                          type: string
                          example: "0.00000000"
                        totalWalletBalance:
                          type: string
                          example: "22.12659734"
                        asset:
                          type: string
                          example: USD
                          description: The sum of BUSD and USDT
                          x-description-cn: USDT和BUSD资产汇总
  /sapi/v2/sub-account/futures/accountSummary:
    get:
      summary: Get Summary of Sub-account's Futures Account V2 (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约账户汇总 V2 (适用主账户) (USER_DATA)
      description: Get Summary of Sub-account's Futures Account
      x-description-cn: 查询子账户合约账户汇总
      tags:
        - asset-management
      operationId: getSummaryOfSubAccountsFuturesAccountV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-summary-of-sub-accounts-futures-account-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getSummaryOfSubAccountsFuturesAccountV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_summary_of_sub_accounts_futures_account_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_summary_of_sub_accounts_futures_account_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetSummaryOfSubAccountsFuturesAccountV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetSummaryOfSubAccountsFuturesAccountV2/GetSummaryOfSubAccountsFuturesAccountV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetSummaryOfSubAccountsFuturesAccountV2Example.php
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
        - name: futuresType
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: "1: USDT-margined Futures，2: Coin-margined Futures"
          x-description-cn: "1: USDT合约，2: 币本位合约"
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 10
            maximum: 20
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Summary of Sub-account's Futures Account V2
          x-description-cn: 查询子账户合约账户汇总 V2
          content:
            application/json:
              schema:
                type: object
                properties:
                  futureAccountSummaryResp:
                    type: object
                    properties:
                      totalInitialMargin:
                        type: string
                        example: "9.83137400"
                      totalMaintenanceMargin:
                        type: string
                        example: "0.41568700"
                      totalMarginBalance:
                        type: string
                        example: "23.03235621"
                      totalOpenOrderInitialMargin:
                        type: string
                        example: "9.00000000"
                      totalPositionInitialMargin:
                        type: string
                        example: "0.83137400"
                      totalUnrealizedProfit:
                        type: string
                        example: "0.03219710"
                      totalWalletBalance:
                        type: string
                        example: "22.15879444"
                      asset:
                        type: string
                        example: USD
                        description: The sum of BUSD and USDT
                        x-description-cn: USDT和BUSD资产汇总
                      subAccountList:
                        type: array
                        items:
                          type: object
                          properties:
                            email:
                              type: string
                              example: 123@test.com
                            totalInitialMargin:
                              type: string
                              example: "9.00000000"
                            totalMaintenanceMargin:
                              type: string
                              example: "0.00000000"
                            totalMarginBalance:
                              type: string
                              example: "22.12659734"
                            totalOpenOrderInitialMargin:
                              type: string
                              example: "9.00000000"
                            totalPositionInitialMargin:
                              type: string
                              example: "0.00000000"
                            totalUnrealizedProfit:
                              type: string
                              example: "0.00000000"
                            totalWalletBalance:
                              type: string
                              example: "22.12659734"
                            asset:
                              type: string
                              example: USD
                              description: The sum of BUSD and USDT
                              x-description-cn: USDT和BUSD资产汇总
                  deliveryAccountSummaryResp:
                    type: object
                    properties:
                      totalMarginBalanceOfBTC:
                        type: string
                        example: "25.03221121"
                      totalUnrealizedProfitOfBTC:
                        type: string
                        example: "0.12233410"
                      totalWalletBalanceOfBTC:
                        type: string
                        example: "22.15879444"
                      asset:
                        type: string
                        example: BTC
                      subAccountList:
                        type: array
                        items:
                          type: object
                          properties:
                            email:
                              type: string
                              example: 123@test.com
                            totalMarginBalance:
                              type: string
                              example: "22.12659734"
                            totalUnrealizedProfit:
                              type: string
                              example: "0.00000000"
                            totalWalletBalance:
                              type: string
                              example: "22.12659734"
                            asset:
                              type: string
                              example: BTC
  /sapi/v1/sub-account/margin/accountSummary:
    get:
      summary: Get Summary of Sub-account's Margin Account (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户杠杆账户汇总 (适用主账户) (USER_DATA)
      description: Get Summary of Sub-account's Margin Account
      x-description-cn: 查询子账户杠杆账户汇总
      tags:
        - asset-management
      operationId: getSummaryOfSubAccountsMarginAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#get-summary-of-sub-accounts-margin-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/getSummaryOfSubAccountsMarginAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/get_summary_of_sub_accounts_margin_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/get_summary_of_sub_accounts_margin_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/GetSummaryOfSubAccountsMarginAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/GetSummaryOfSubAccountsMarginAccount/GetSummaryOfSubAccountsMarginAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/GetSummaryOfSubAccountsMarginAccountExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Summary of Sub-account's Margin Account
          x-description-cn: 查询子账户杠杆账户汇总
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalAssetOfBtc:
                    type: string
                    example: "4.33333333"
                  totalLiabilityOfBtc:
                    type: string
                    example: "2.11111112"
                  totalNetAssetOfBtc:
                    type: string
                    example: "2.22222221"
                  subAccountList:
                    type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          example: 123@test.com
                        totalAssetOfBtc:
                          type: string
                          example: "2.11111111"
                        totalLiabilityOfBtc:
                          type: string
                          example: "1.11111111"
                        totalNetAssetOfBtc:
                          type: string
                          example: "1.00000000"
  /sapi/v1/sub-account/margin/transfer:
    post:
      summary: Margin Transfer for Sub-account (For Master Account) (USER_DATA)
      x-summary-cn: 子账户杠杆划转 (仅适用主账户) (USER_DATA)
      description: Margin Transfer for Sub-account
      x-description-cn: 子账户杠杆划转
      tags:
        - asset-management
      operationId: marginTransferForSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#margin-transfer-for-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/marginTransferForSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/margin_transfer_for_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/margin_transfer_for_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/MarginTransferForSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/MarginTransferForSubAccount/MarginTransferForSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/MarginTransferForSubAccountExample.php
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
      x-parameters-notes: "- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint."
      x-parameters-notes-cn: "- 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - email
                - asset
                - amount
                - type
                - timestamp
              properties:
                email:
                  type: string
                  example: 123@test.com
                asset:
                  type: string
                  example: BTC
                  description: The asset being transferred
                  x-description-cn: 划转资产
                amount:
                  type: number
                  example: "1.0"
                  format: float
                  description: The amount to be transferred
                  x-description-cn: 划转数量
                type:
                  type: integer
                  example: 1
                  format: int64
                  description: |-
                    1: transfer from subaccount's spot account to margin account 2: transfer from subaccount's margin
                    account to its spot account
                  x-description-cn: "1: 由子账户的现货账户划转至其杠杆账户; 2: 由子账户的杠杆账户划转至其现货账户"
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Margin Transfer for Sub-account
          x-description-cn: 子账户杠杆划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  txnId:
                    type: string
                    example: "2966662589"
  /sapi/v3/sub-account/assets:
    get:
      summary: Query Sub-account Assets (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户资产 (适用主账户) (USER_DATA)
      description: Fetch sub-account assets
      x-description-cn: 查询子账户资产
      tags:
        - asset-management
      operationId: querySubAccountAssets
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#query-sub-account-assets
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/querySubAccountAssets.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/query_sub_account_assets.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/query_sub_account_assets.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/QuerySubAccountAssetsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/QuerySubAccountAssets/QuerySubAccountAssets.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/QuerySubAccountAssetsExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 60
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account Assets
          x-description-cn: 子账户资产
          content:
            application/json:
              schema:
                type: object
                properties:
                  balances:
                    type: array
                    items:
                      type: object
                      properties:
                        freeze:
                          type: integer
                          example: 0
                          format: int64
                        withdrawing:
                          type: integer
                          example: 0
                          format: int64
                        asset:
                          type: string
                          example: ADA
                        free:
                          type: number
                          example: 11467.6399
                          format: float
                        locked:
                          type: integer
                          example: 0
                          format: int64
  /sapi/v4/sub-account/assets:
    get:
      summary: Query Sub-account Assets V4 (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户资产 (适用主账户) (USER_DATA)
      description: Fetch sub-account assets
      x-description-cn: 获取子账户资产
      tags:
        - asset-management
      operationId: querySubAccountAssetsAssetManagement
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#query-sub-account-assets-asset-management
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/querySubAccountAssetsAssetManagement.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/query_sub_account_assets_asset_management.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/query_sub_account_assets_asset_management.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/QuerySubAccountAssetsAssetManagementExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/QuerySubAccountAssetsAssetManagement/QuerySubAccountAssetsAssetManagement.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/QuerySubAccountAssetsAssetManagementExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 60
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account Assets
          x-description-cn: 子账户资产
          content:
            application/json:
              schema:
                type: object
                properties:
                  balances:
                    type: array
                    items:
                      type: object
                      properties:
                        freeze:
                          type: string
                          example: "0"
                        withdrawing:
                          type: string
                          example: "0"
                        asset:
                          type: string
                          example: ADA
                        free:
                          type: string
                          example: "10000"
                        locked:
                          type: string
                          example: "0"
  /sapi/v1/sub-account/futures/internalTransfer:
    get:
      summary: Query Sub-account Futures Asset Transfer History (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户合约资金划转历史 (适用主账户) (USER_DATA)
      description: Query Sub-account Futures Asset Transfer History
      x-description-cn: 查询子账户合约资金划转历史
      tags:
        - asset-management
      operationId: querySubAccountFuturesAssetTransferHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#query-sub-account-futures-asset-transfer-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/querySubAccountFuturesAssetTransferHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/query_sub_account_futures_asset_transfer_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/query_sub_account_futures_asset_transfer_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/QuerySubAccountFuturesAssetTransferHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/QuerySubAccountFuturesAssetTransferHistory/QuerySubAccountFuturesAssetTransferHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/QuerySubAccountFuturesAssetTransferHistoryExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: 123@test.com
        - name: futuresType
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: "1: USDT-margined Futures，2: Coin-margined Futures"
          x-description-cn: "1: USDT合约，2: 币本位合约"
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Cannot be earlier than 1 month ago
          x-description-cn: 只能查询近一个月内历史纪录
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 50
            maximum: 500
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account Futures Asset Transfer History
          x-description-cn: 查询子账户合约资产划转历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  futuresType:
                    type: integer
                    example: 2
                    format: int64
                  transfers:
                    type: array
                    items:
                      type: object
                      properties:
                        from:
                          type: string
                          example: aaa@test.com
                        to:
                          type: string
                          example: bbb@test.com
                        asset:
                          type: string
                          example: BTC
                        qty:
                          type: string
                          example: "1"
                        tranId:
                          type: integer
                          example: 11897001102
                          format: int64
                        time:
                          type: integer
                          example: 1544433328000
                          format: int64
    post:
      summary: Sub-account Futures Asset Transfer (For Master Account) (USER_DATA)
      x-summary-cn: 执行子账户合约资金划转 (适用主账户) (USER_DATA)
      description: Sub-account Futures Asset Transfer
      x-description-cn: 执行子账户合约资金划转
      tags:
        - asset-management
      operationId: subAccountFuturesAssetTransfer
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#sub-account-futures-asset-transfer
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/subAccountFuturesAssetTransfer.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/sub_account_futures_asset_transfer.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/sub_account_futures_asset_transfer.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/SubAccountFuturesAssetTransferExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/SubAccountFuturesAssetTransfer/SubAccountFuturesAssetTransfer.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/SubAccountFuturesAssetTransferExample.php
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
      x-parameters-notes: |-
        - A master account can transfer at most 2000 times per minute.
        - The futures wallet must have sufficient margin balance to execute the transfer.
      x-parameters-notes-cn: |-
        - 每个母账户每分钟上限2000次
        - 您期货钱包中须有足够保证金余额才能执行转账
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - fromEmail
                - toEmail
                - futuresType
                - asset
                - amount
                - timestamp
              properties:
                fromEmail:
                  type: string
                  example: abc@test.com
                  description: Sender email
                  x-description-cn: 发送者邮箱
                toEmail:
                  type: string
                  example: def@test.com
                  description: Recipient email
                  x-description-cn: 接收者邮箱
                futuresType:
                  type: integer
                  example: 1
                  format: int64
                  description: "1: USDT-margined Futures，2: Coin-margined Futures"
                  x-description-cn: "1: USDT合约， 2: 币本位合约"
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account Futures Asset Transfer
          x-description-cn: 执行子账户合约资产划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  txnId:
                    type: string
                    example: "2934662589"
  /sapi/v1/sub-account/spotSummary:
    get:
      summary: Query Sub-account Spot Assets Summary (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户现货资产汇总 (适用主账户) (USER_DATA)
      description: Get BTC valued asset summary of subaccounts.
      x-description-cn: 获取BTC计价的子账户现货资产汇总。
      tags:
        - asset-management
      operationId: querySubAccountSpotAssetsSummary
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#query-sub-account-spot-assets-summary
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/querySubAccountSpotAssetsSummary.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/query_sub_account_spot_assets_summary.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/query_sub_account_spot_assets_summary.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/QuerySubAccountSpotAssetsSummaryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/QuerySubAccountSpotAssetsSummary/QuerySubAccountSpotAssetsSummary.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/QuerySubAccountSpotAssetsSummaryExample.php
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
        - name: email
          in: query
          required: false
          schema:
            type: string
            example: 123@test.com
          description: Managed sub-account email
          x-description-cn: 托管子账户邮箱
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 10
            maximum: 20
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Sub-account Spot Assets Summary
          x-description-cn: 查询子账户现货资产汇总
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalCount:
                    type: integer
                    example: 2
                    format: int64
                  masterAccountTotalAsset:
                    type: string
                    example: "0.23231201"
                  spotSubUserAssetBtcVoList:
                    type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          example: sub123@test.com
                        totalAsset:
                          type: string
                          example: "9999.00000000"
  /sapi/v1/sub-account/sub/transfer/history:
    get:
      summary: Query Sub-account Spot Asset Transfer History (For Master Account) (USER_DATA)
      x-summary-cn: 查询子账户现货资金划转历史 (适用主账户) (USER_DATA)
      description: Query Sub-account Spot Asset Transfer History
      x-description-cn: 查询子账户现货资金划转历史
      tags:
        - asset-management
      operationId: querySubAccountSpotAssetTransferHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#query-sub-account-spot-asset-transfer-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/querySubAccountSpotAssetTransferHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/query_sub_account_spot_asset_transfer_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/query_sub_account_spot_asset_transfer_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/QuerySubAccountSpotAssetTransferHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/QuerySubAccountSpotAssetTransferHistory/QuerySubAccountSpotAssetTransferHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/QuerySubAccountSpotAssetTransferHistoryExample.php
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
        - name: fromEmail
          in: query
          required: false
          schema:
            type: string
            example: aaa@test.com
        - name: toEmail
          in: query
          required: false
          schema:
            type: string
            example: bbb@test.com
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
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 500
            maximum: 200
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - `fromEmail` and `toEmail` cannot be sent at the same time.

        - If both `fromEmail` and `toEmail` are omitted, records with `fromEmail` equal to the master account are
        returned by default.
      x-parameters-notes-cn: |-
        - `fromEmail` 和 `toEmail` 不能同时传入。
        - 若 `fromEmail` 和 `toEmail` 都未传，默认返回 `fromEmail` 为母账户的记录。
      responses:
        "200":
          description: Sub-account Spot Asset Transfer History
          x-description-cn: 查询子账户现货资产划转历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    from:
                      type: string
                      example: aaa@test.com
                    to:
                      type: string
                      example: bbb@test.com
                    asset:
                      type: string
                      example: BTC
                    qty:
                      type: string
                      example: "10"
                    status:
                      type: string
                      example: SUCCESS
                    tranId:
                      type: integer
                      example: 6489943656
                      format: int64
                    time:
                      type: integer
                      example: 1544433328000
                      format: int64
  /sapi/v1/sub-account/universalTransfer:
    get:
      summary: Query Universal Transfer History (For Master Account) (USER_DATA)
      x-summary-cn: 查询子母账户万能划转历史 (适用主账户) (USER_DATA)
      description: Query Universal Transfer History
      x-description-cn: 查询子母账户万能划转历史
      tags:
        - asset-management
      operationId: queryUniversalTransferHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#query-universal-transfer-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/queryUniversalTransferHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/query_universal_transfer_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/query_universal_transfer_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/QueryUniversalTransferHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/QueryUniversalTransferHistory/QueryUniversalTransferHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/QueryUniversalTransferHistoryExample.php
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
        - name: fromEmail
          in: query
          required: false
          schema:
            type: string
            example: abctest@gmail.com
        - name: toEmail
          in: query
          required: false
          schema:
            type: string
            example: deftest@gmail.com
        - name: clientTranId
          in: query
          required: false
          schema:
            type: string
            example: "1"
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
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 500
            maximum: 500
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - `fromEmail` and `toEmail` cannot be sent at the same time.

        - If both `fromEmail` and `toEmail` are omitted, records with `fromEmail` equal to the master account are
        returned by default.

        - The query time range must be less than 7 days.

        - If `startTime` and `endTime` are omitted, records from the last 7 days are returned by default.
      x-parameters-notes-cn: |-
        - 本查询接口仅支持单边查询，`fromEmail` 和 `toEmail` 不能同时传入。
        - 若 `fromEmail` 和 `toEmail` 都未传，默认返回 `fromEmail` 为母账户的划转记录。
        - 查询时间范围最大不得超过 7 天。
        - 若 `startTime` 和 `endTime` 都未传，则默认返回最近 7 天的记录。
      responses:
        "200":
          description: Universal Transfer History
          x-description-cn: 万能划转 历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        tranId:
                          type: integer
                          example: 92275823339
                          format: int64
                        fromEmail:
                          type: string
                          example: abctest@gmail.com
                        toEmail:
                          type: string
                          example: deftest@gmail.com
                        asset:
                          type: string
                          example: BNB
                        amount:
                          type: string
                          example: "0.01"
                        createTimeStamp:
                          type: integer
                          example: 1640317374000
                          format: int64
                        fromAccountType:
                          type: string
                          example: USDT_FUTURE
                        toAccountType:
                          type: string
                          example: SPOT
                        status:
                          type: string
                          example: SUCCESS
                        clientTranId:
                          type: string
                          example: test
                  totalCount:
                    type: integer
                    example: 1
                    format: int64
    post:
      summary: Universal Transfer (For Master Account) (USER_DATA)
      x-summary-cn: 子母账户万能划转 (适用主账户) (USER_DATA)
      description: Universal Transfer
      x-description-cn: 子母账户万能划转
      tags:
        - asset-management
      operationId: universalTransfer
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#universal-transfer
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/universalTransfer.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/universal_transfer.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/universal_transfer.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/UniversalTransferExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/UniversalTransfer/UniversalTransfer.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/UniversalTransferExample.php
      x-ip-weight: 1
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 360
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - You need to enable the `internal transfer` option for the API key used to call this endpoint.

        - If `fromEmail` is not sent, transfer out from the master account by default.

        - If `toEmail` is not sent, transfer into the master account by default.

        - When `fromAccountType` and `toAccountType` are the same, at least one of `fromEmail` or `toEmail` must be
        sent.

        - Supported transfer scenarios:
          - `SPOT` -> `SPOT` / `USDT_FUTURE` / `COIN_FUTURE` (master or sub-account).
          - `SPOT` / `USDT_FUTURE` / `COIN_FUTURE` -> `SPOT` (master or sub-account).
          - Master account `SPOT` -> sub-account `MARGIN(Cross)` / `ISOLATED_MARGIN`.
          - Sub-account `MARGIN(Cross)` / `ISOLATED_MARGIN` -> master account `SPOT`.
          - Sub-account `MARGIN(Cross)` -> sub-account `MARGIN(Cross)`.
          - `ALPHA` -> `ALPHA` (master or sub-account).
      x-parameters-notes-cn: |-
        - 需要开启母账户 API Key 的“允许子母账户划转”权限。
        - 若 `fromEmail` 未传，默认从母账户转出。
        - 若 `toEmail` 未传，默认转入母账户。
        - 当 `fromAccountType` 与 `toAccountType` 相同时，`fromEmail` 和 `toEmail` 至少传一个。
        - 该接口支持的划转场景：
        - `SPOT` 划转到 `SPOT`、`USDT_FUTURE`、`COIN_FUTURE`（母账户或子账户）。
        - `SPOT`、`USDT_FUTURE`、`COIN_FUTURE` 划转到 `SPOT`（母账户或子账户）。
        - 母账户 `SPOT` 划转到子账户 `MARGIN(Cross)`、`ISOLATED_MARGIN`。
        - 子账户 `MARGIN(Cross)`、`ISOLATED_MARGIN` 划转到母账户 `SPOT`。
        - 子账户 `MARGIN(Cross)` 划转到子账户 `MARGIN(Cross)`。
        - `ALPHA` 划转到 `ALPHA`（母账户或子账户）。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - fromAccountType
                - toAccountType
                - asset
                - amount
                - timestamp
              properties:
                fromEmail:
                  type: string
                  example: abc@test.com
                toEmail:
                  type: string
                  example: def@test.com
                fromAccountType:
                  type: string
                  example: SPOT
                  enum:
                    - SPOT
                    - USDT_FUTURE
                    - COIN_FUTURE
                    - MARGIN
                    - ISOLATED_MARGIN
                toAccountType:
                  type: string
                  example: SPOT
                  enum:
                    - SPOT
                    - USDT_FUTURE
                    - COIN_FUTURE
                    - MARGIN
                    - ISOLATED_MARGIN
                clientTranId:
                  type: string
                  example: "1"
                  description: Must be unique
                  x-description-cn: 不可重复
                symbol:
                  type: string
                  example: BTCUSDT
                  description: Only supported under ISOLATED_MARGIN type
                  x-description-cn: 仅在ISOLATED_MARGIN类型下使用
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Universal Transfer
          x-description-cn: 万能划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 11945860693
                    format: int64
                  clientTranId:
                    type: string
                    example: test
  /sapi/v1/sub-account/transfer/subUserHistory:
    get:
      summary: Sub-account Transfer History (For Sub-account) (USER_DATA)
      x-summary-cn: 查询子账户划转历史 (仅适用子账户) (USER_DATA)
      description: Sub-account Transfer History
      x-description-cn: 查询子账户划转历史
      tags:
        - asset-management
      operationId: subAccountTransferHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#sub-account-transfer-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/subAccountTransferHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/sub_account_transfer_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/sub_account_transfer_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/SubAccountTransferHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/SubAccountTransferHistory/SubAccountTransferHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/SubAccountTransferHistoryExample.php
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
            example: BTC
          description: If not sent, result of all assets will be returned
          x-description-cn: 如不提供，返回所有asset 划转记录
        - name: type
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: "1: transfer in, 2: transfer out"
          x-description-cn: "1: 转入，2: 转出；如不提供，返回转出方向划转记录"
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
            example: 10
            default: 500
            maximum: 200
            format: int64
        - name: returnFailHistory
          in: query
          required: false
          schema:
            type: boolean
            example: false
            default: false
          description: |-
            Default `False`, return PROCESS and SUCCESS status history; If `True`,return PROCESS and SUCCESS and FAILURE
            status history
          x-description-cn: 默认 `false`，返回 PROCESS 和 SUCCESS 状态的数据；若传 `true`，返回 PROCESS、SUCCESS、FAILURE 状态的数据。
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `type` is not sent, records of type `2` (transfer out) are returned by default.
        - If `startTime` and `endTime` are not sent, data from the most recent 30 days is returned.
      x-parameters-notes-cn: |-
        - 如果未传 `type`，默认只返回 `type=2`（转出）数据。
        - 如果 `startTime` 和 `endTime` 均未传，默认只返回最近 30 天数据。
      responses:
        "200":
          description: Sub-account Transfer History
          x-description-cn: 查询子账户划转历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    counterParty:
                      type: string
                      example: master
                    email:
                      type: string
                      example: master@test.com
                    type:
                      type: integer
                      example: 1
                      format: int64
                      description: 1 for transfer in, 2 for transfer out
                      x-description-cn: 1 for transfer in , 2 for transfer out
                    asset:
                      type: string
                      example: BTC
                    qty:
                      type: string
                      example: "1"
                    fromAccountType:
                      type: string
                      example: SPOT
                    toAccountType:
                      type: string
                      example: SPOT
                    status:
                      type: string
                      example: SUCCESS
                      description: "status: PROCESS / SUCCESS / FAILURE"
                      x-description-cn: "status: PROCESS / SUCCESS / FAILURE"
                    tranId:
                      type: integer
                      example: 11798835829
                      format: int64
                    time:
                      type: integer
                      example: 1544433325000
                      format: int64
  /sapi/v1/sub-account/transfer/subToMaster:
    post:
      summary: Transfer to Master (For Sub-account) (USER_DATA)
      x-summary-cn: 向主账户主动划转 (仅适用子账户) (USER_DATA)
      description: Transfer to Master
      x-description-cn: 向主账户主动划转
      tags:
        - asset-management
      operationId: transferToMaster
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#transfer-to-master
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/transferToMaster.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/transfer_to_master.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/transfer_to_master.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/TransferToMasterExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/TransferToMaster/TransferToMaster.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/TransferToMasterExample.php
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
      x-parameters-notes: "- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint."
      x-parameters-notes-cn: "- 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。"
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
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Transfer to Master
          x-description-cn: 划转至主账户
          content:
            application/json:
              schema:
                type: object
                properties:
                  txnId:
                    type: string
                    example: "2966662589"
  /sapi/v1/sub-account/transfer/subToSub:
    post:
      summary: Transfer to Sub-account of Same Master (For Sub-account) (USER_DATA)
      x-summary-cn: 向共同主账户下的子账户主动划转 (仅适用子账户) (USER_DATA)
      description: Transfer to Sub-account of Same Master
      x-description-cn: 向共同主账户下的子账户主动划转
      tags:
        - asset-management
      operationId: transferToSubAccountOfSameMaster
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/asset-management#transfer-to-sub-account-of-same-master
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/AssetManagementApi/transferToSubAccountOfSameMaster.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/asset_management_api/transfer_to_sub_account_of_same_master.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/AssetManagement/transfer_to_sub_account_of_same_master.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/assetmanagement/TransferToSubAccountOfSameMasterExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/AssetManagementAPI/TransferToSubAccountOfSameMaster/TransferToSubAccountOfSameMaster.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/assetmanagement/TransferToSubAccountOfSameMasterExample.php
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
      x-parameters-notes: "- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint."
      x-parameters-notes-cn: "- 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - toEmail
                - asset
                - amount
                - timestamp
              properties:
                toEmail:
                  type: string
                  example: abc@test.com
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Transfer to Sub-account of Same Master
          x-description-cn: 划转至同一主账户下的子账户
          content:
            application/json:
              schema:
                type: object
                properties:
                  txnId:
                    type: string
                    example: "2966662589"
  /sapi/v1/managed-subaccount/deposit:
    post:
      summary: Deposit Assets Into The Managed Sub-account (For Investor Master Account) (USER_DATA)
      x-summary-cn: 投资人账户为托管子账户充值资产 (适用投资人母账户) (USER_DATA)
      description: Deposit Assets Into The Managed Sub-account
      x-description-cn: 投资人账户为托管子账户充值资产(适用投资人母账户)
      tags:
        - managed-sub-account
      operationId: depositAssetsIntoTheManagedSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#deposit-assets-into-the-managed-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/depositAssetsIntoTheManagedSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/deposit_assets_into_the_managed_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/deposit_assets_into_the_managed_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/DepositAssetsIntoTheManagedSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/DepositAssetsIntoTheManagedSubAccount/DepositAssetsIntoTheManagedSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/DepositAssetsIntoTheManagedSubAccountExample.php
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
      x-parameters-notes: "- You need to enable `Enable Spot & Margin Trading` option for the api key which requests this endpoint"
      x-parameters-notes-cn: "- 您需要开通API Key`允许现货和杠杆交易`权限"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - toEmail
                - asset
                - amount
                - timestamp
              properties:
                toEmail:
                  type: string
                  example: abc@test.com
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Deposit Assets Into The Managed Sub-account
          x-description-cn: 投资人账户为托管子账户充值资产
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 66157362489
                    format: int64
  /sapi/v1/managed-subaccount/deposit/address:
    get:
      summary: Get Managed Sub-account Deposit Address (For Investor Master Account) (USER_DATA)
      x-summary-cn: 获取托管子账户充值地址 (适用投资人母账户) (USER_DATA)
      description: Get investor's managed sub-account deposit address.
      x-description-cn: 获取投资人之托管子账户充值地址
      tags:
        - managed-sub-account
      operationId: getManagedSubAccountDepositAddress
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#get-managed-sub-account-deposit-address
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/getManagedSubAccountDepositAddress.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/get_managed_sub_account_deposit_address.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/get_managed_sub_account_deposit_address.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/GetManagedSubAccountDepositAddressExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/GetManagedSubAccountDepositAddress/GetManagedSubAccountDepositAddress.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/GetManagedSubAccountDepositAddressExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 1
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
        - name: coin
          in: query
          required: true
          schema:
            type: string
            example: USDT
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: LIGHTNING
          description: networks can be found in `GET /sapi/v1/capital/deposit/address`
          x-description-cn: 网络可以在`GET /sapi/v1/capital/deposit/address`获取
        - name: amount
          in: query
          required: false
          schema:
            type: number
            example: "1.0"
            format: float
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - If `network` is not sent, the default `network` for the `coin` is returned.
        - When using `LIGHTNING`, `amount` must be provided.
      x-parameters-notes-cn: |-
        - `network` 不传时，返回该 `coin` 的默认 `network`。
        - 使用 `LIGHTNING` 网络时，`amount` 必传。
      responses:
        "200":
          description: Get Managed Sub-account Deposit Address
          x-description-cn: 获取托管子账户充值地址
          content:
            application/json:
              schema:
                type: object
                properties:
                  coin:
                    type: string
                    example: USDT
                  address:
                    type: string
                    example: "0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d"
                  tag:
                    type: string
                    example: ""
                  url:
                    type: string
                    example: https://etherscan.io/address/0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d
  /sapi/v1/managed-subaccount/asset:
    get:
      summary: Query Managed Sub-account Asset Details (For Investor Master Account) (USER_DATA)
      x-summary-cn: 投资人账户查询托管子账户资产 (适用投资人母账户) (USER_DATA)
      description: Query Managed Sub-account Asset Details
      x-description-cn: 投资人账户查询托管子账户资产
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountAssetDetails
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-asset-details
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountAssetDetails.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_asset_details.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_asset_details.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountAssetDetailsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountAssetDetails/QueryManagedSubAccountAssetDetails.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountAssetDetailsExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Managed Sub-account Asset Details
          x-description-cn: 查询托管子账户资产详情
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    coin:
                      type: string
                      example: INJ
                    name:
                      type: string
                      example: Injective Protocol
                    totalBalance:
                      type: string
                      example: "0"
                    availableBalance:
                      type: string
                      example: "0"
                    inOrder:
                      type: string
                      example: "0"
                    btcValue:
                      type: string
                      example: "0"
  /sapi/v1/managed-subaccount/fetch-future-asset:
    get:
      summary: Query Managed Sub-account Futures Asset Details (For Investor Master Account) (USER_DATA)
      x-summary-cn: 投资人账户查询托管子账户期货资产 (适用投资人母账户) (USER_DATA)
      description: Investor can use this api to query managed sub account futures asset details
      x-description-cn: 投资人可以根据此接口查询其托管子账户期货资产
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountFuturesAssetDetails
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-futures-asset-details
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountFuturesAssetDetails.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_futures_asset_details.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_futures_asset_details.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountFuturesAssetDetailsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountFuturesAssetDetails/QueryManagedSubAccountFuturesAssetDetails.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountFuturesAssetDetailsExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 60
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
        - name: accountType
          in: query
          required: false
          schema:
            type: string
            example: MARGIN
          description: >-
            No input or input "USDT_FUTURE" to get UM Futures account details. Input "COIN_FUTURE" to get CM Futures
            account details.
          x-description-cn: 不传或传入 "USDT_FUTURE" 获取 U 本位合约账户详情。传入 "COIN_FUTURE" 获取币本位合约账户详情。
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
          description: Managed Sub-account Futures Asset Details
          x-description-cn: 查询托管子账户合约资产详情
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "200"
                  message:
                    type: string
                    example: OK
                  snapshotVos:
                    type: array
                    items:
                      type: object
                      properties:
                        type:
                          type: string
                          example: FUTURES
                        updateTime:
                          type: integer
                          example: 1672893855394
                          format: int64
                        data:
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
                                  marginBalance:
                                    type: integer
                                    example: 100
                                    format: int64
                                  walletBalance:
                                    type: integer
                                    example: 120
                                    format: int64
                            position:
                              type: array
                              items:
                                type: object
                                properties:
                                  symbol:
                                    type: string
                                    example: BTCUSDT
                                  entryPrice:
                                    type: integer
                                    example: 17000
                                    format: int64
                                  markPrice:
                                    type: integer
                                    example: 17000
                                    format: int64
                                  positionAmt:
                                    type: number
                                    example: 0.0001
                                    format: float
  /sapi/v1/managed-subaccount/info:
    get:
      summary: Query Managed Sub-account List (For Investor) (USER_DATA)
      x-summary-cn: 查询托管子账户列表 (适用投资人母账户) (USER_DATA)
      description: Get investor's managed sub-account list.
      x-description-cn: 获取投资人之托管子账户列表
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountList/QueryManagedSubAccountList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountListExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 60
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: false
          schema:
            type: string
            example: abc@test.com
        - name: page
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 20
            maximum: 20
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Managed Sub-account List
          x-description-cn: 查询托管子账户列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 3
                    format: int64
                  managerSubUserInfoVoList:
                    type: array
                    items:
                      type: object
                      properties:
                        rootUserId:
                          type: integer
                          example: 1000138475670
                          format: int64
                        managersubUserId:
                          type: integer
                          example: 1000137842513
                          format: int64
                        bindParentUserId:
                          type: integer
                          example: 1000138475669
                          format: int64
                        email:
                          type: string
                          example: test_0_virtual@kq3kno9imanagedsub.com
                        insertTimeStamp:
                          type: integer
                          example: 1678435149000
                          format: int64
                        bindParentEmail:
                          type: string
                          example: wdyw8xsh8pey@test.com
                        isSubUserEnabled:
                          type: boolean
                          example: true
                        isUserActive:
                          type: boolean
                          example: true
                        isMarginEnabled:
                          type: boolean
                          example: false
                        isFutureEnabled:
                          type: boolean
                          example: false
                        isSignedLVTRiskAgreement:
                          type: boolean
                          example: false
  /sapi/v1/managed-subaccount/marginAsset:
    get:
      summary: Query Managed Sub-account Margin Asset Details (For Investor Master Account) (USER_DATA)
      x-summary-cn: 投资人账户查询托管子账户杠杆资产 (适用投资人母账户) (USER_DATA)
      description: Investor can use this api to query managed sub account margin asset details
      x-description-cn: 投资人可以根据此接口查询其托管子账户杠杆资产
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountMarginAssetDetails
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-margin-asset-details
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountMarginAssetDetails.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_margin_asset_details.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_margin_asset_details.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountMarginAssetDetailsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountMarginAssetDetails/QueryManagedSubAccountMarginAssetDetails.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountMarginAssetDetailsExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
        - name: accountType
          in: query
          required: false
          schema:
            type: string
            example: MARGIN
          description: |-
            No input or input "MARGIN" to get Cross Margin account details. Input "ISOLATED_MARGIN" to get Isolated
            Margin account details.
          x-description-cn: 不输入或输入MARGIN，取得全仓帐户资产。 输入ISOLATED_MARGIN，取得逐仓帐户资产。
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
          description: Managed Sub-account Margin Asset Details
          x-description-cn: 查询托管子账户杠杆资产详情
          content:
            application/json:
              schema:
                type: object
                properties:
                  marginLevel:
                    type: string
                    example: "999"
                  totalAssetOfBtc:
                    type: string
                    example: "0"
                  totalLiabilityOfBtc:
                    type: string
                    example: "0"
                  totalNetAssetOfBtc:
                    type: string
                    example: "0"
                  userAssets:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: MATIC
                        borrowed:
                          type: string
                          example: "0"
                        free:
                          type: string
                          example: "0"
                        interest:
                          type: string
                          example: "0"
                        locked:
                          type: string
                          example: "0"
                        netAsset:
                          type: string
                          example: "0"
  /sapi/v1/managed-subaccount/accountSnapshot:
    get:
      summary: Query Managed Sub-account Snapshot (For Investor Master Account) (USER_DATA)
      x-summary-cn: 查询托管子账户资产快照 (适用投资人母账户) (USER_DATA)
      description: Query Managed Sub-account Snapshot
      x-description-cn: 查询托管子账户资产快照
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountSnapshot
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-snapshot
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountSnapshot.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_snapshot.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_snapshot.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountSnapshotExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountSnapshot/QueryManagedSubAccountSnapshot.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountSnapshotExample.php
      x-ip-weight: 2400
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
        - name: type
          in: query
          required: true
          schema:
            type: string
            example: SPOT
            enum:
              - SPOT
              - MARGIN
              - FUTURES
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Query time range must be within 30 days and only supports data within the last month.
          x-description-cn: 查询时间范围不得超过 30 天，且仅支持最近 1 个月内的数据。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: If both startTime and endTime are omitted, records from the last 7 days are returned by default.
          x-description-cn: 如果未同时传入 startTime 和 endTime，默认返回最近 7 天记录。
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 7
            minimum: 7
            maximum: 30
            format: int64
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: |-
        - The query time range must be less than 30 days.
        - Only data from the most recent month is supported.
        - If `startTime` and `endTime` are omitted, records from the last 7 days are returned by default.
      x-parameters-notes-cn: |-
        - 查询时间范围最大不得超过30天
        - 仅支持查询最近 1 个月数据
        - 若 `startTime` 和 `endTime` 未传，则默认返回最近 7 天数据。
      responses:
        "200":
          description: Managed Sub-account Snapshot
          x-description-cn: 托管子账户资产快照
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                    example: 200
                    format: int64
                    description: 200 for success; others are error codes
                    x-description-cn: 200表示返回正确，否则即为错误码
                  msg:
                    type: string
                    example: ""
                    description: error message
                    x-description-cn: 与错误码对应的报错信息
                  snapshotVos:
                    type: array
                    items:
                      type: object
                      properties:
                        data:
                          type: object
                          properties:
                            balances:
                              type: array
                              items:
                                type: object
                                properties:
                                  asset:
                                    type: string
                                    example: BTC
                                  free:
                                    type: string
                                    example: "0.09905021"
                                  locked:
                                    type: string
                                    example: "0.00000000"
                            totalAssetOfBtc:
                              type: string
                              example: "0.09942700"
                            marginLevel:
                              type: string
                              example: "2748.02909813"
                            totalLiabilityOfBtc:
                              type: string
                              example: "0.00000100"
                            totalNetAssetOfBtc:
                              type: string
                              example: "0.00274750"
                            userAssets:
                              type: array
                              items:
                                type: object
                                properties:
                                  asset:
                                    type: string
                                    example: XRP
                                  borrowed:
                                    type: string
                                    example: "0.00000000"
                                  free:
                                    type: string
                                    example: "1.00000000"
                                  interest:
                                    type: string
                                    example: "0.00000000"
                                  locked:
                                    type: string
                                    example: "0.00000000"
                                  netAsset:
                                    type: string
                                    example: "1.00000000"
                            assets:
                              type: array
                              items:
                                type: object
                                properties:
                                  asset:
                                    type: string
                                    example: USDT
                                  marginBalance:
                                    type: string
                                    example: "118.99782335"
                                  walletBalance:
                                    type: string
                                    example: "120.23811389"
                            position:
                              type: array
                              items:
                                type: object
                                properties:
                                  entryPrice:
                                    type: string
                                    example: "7130.41000000"
                                  markPrice:
                                    type: string
                                    example: "7257.66239673"
                                  positionAmt:
                                    type: string
                                    example: "0.01000000"
                                  symbol:
                                    type: string
                                    example: BTCUSDT
                                  unRealizedProfit:
                                    type: string
                                    example: "1.24029054"
                                    description: Only show the value at the time of opening the position
                                    x-description-cn: 只显示开仓当时的未实现盈亏，不会实时更新，可以忽略
                        type:
                          type: string
                          example: spot
                        updateTime:
                          type: integer
                          example: 1576281599000
                          format: int64
  /sapi/v1/managed-subaccount/queryTransLogForInvestor:
    get:
      summary: Query Managed Sub Account Transfer Log For Investor Master Account (USER_DATA)
      x-summary-cn: 查询托管子账户的划转记录 (适用投资人母账户) (USER_DATA)
      description: >-
        Query Managed Sub Account Transfer Log For Investor Master Account


        Investor can use this api to query managed sub account transfer log. This endpoint is available for investor of

        Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset

        allocation and account application, while delegating trades to a professional trading team.


        Please refer to

        [link](https://www.binance.com/en/support/faq/how-to-get-started-with-managed-sub-account-functions-and-frequently-asked-questions-0594748722704383a7c369046e489459)
      x-description-cn: >-
        查询托管子账户的划转记录 (适用投资人母账户)


        投资人可以根据此接口查询其托管子账户划转记录。此接口可供托管子账户的投资者使用。托管子账户是为重视资产配置与账户应用灵活性，并同时将交易委托专业交易团队的投资者的子账户类型。


        请参阅[链接](https://www.binance.com/zh-CN/support/faq/%E6%89%98%E7%AE%A1%E5%AD%90%E8%B4%A6%E6%88%B7%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D-0594748722704383a7c369046e489459)
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountTransferLogMasterAccountInvestor
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-transfer-log-master-account-investor
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountTransferLogMasterAccountInvestor.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_transfer_log_master_account_investor.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_transfer_log_master_account_investor.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountTransferLogMasterAccountInvestorExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountTransferLogMasterAccountInvestor/QueryManagedSubAccountTransferLogMasterAccountInvestor.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountTransferLogMasterAccountInvestorExample.php
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
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time
          x-description-cn: 开始时间
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time (The start time and end time interval cannot exceed half a year)
          x-description-cn: 结束时间(开始时间结束时间间隔不能超过半年)
        - name: page
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: Page
          x-description-cn: 页数
        - name: limit
          in: query
          required: true
          schema:
            type: integer
            example: 1
            maximum: 500
            format: int64
        - name: transfers
          in: query
          required: false
          schema:
            type: string
            example: null
          description: Transfer Direction (FROM/TO)
          x-description-cn: 划转方向 (FROM/TO)
        - name: transferFunctionAccountType
          in: query
          required: false
          schema:
            type: string
            example: SPOT
            enum:
              - SPOT
              - MARGIN
              - ISOLATED_MARGIN
              - USDT_FUTURE
              - COIN_FUTURE
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
          description: Managed Sub Account Transfer Log
          x-description-cn: 查询托管子账户划转记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  managerSubTransferHistoryVos:
                    type: array
                    items:
                      type: object
                      properties:
                        fromEmail:
                          type: string
                          example: test_0_virtual@kq3kno9imanagedsub.com
                        fromAccountType:
                          type: string
                          example: SPOT
                        toEmail:
                          type: string
                          example: wdywl0lddakh@test.com
                        toAccountType:
                          type: string
                          example: SPOT
                        asset:
                          type: string
                          example: BNB
                        amount:
                          type: string
                          example: "0.01"
                        scheduledData:
                          type: integer
                          example: 1679416673000
                          format: int64
                        createTime:
                          type: integer
                          example: 1679416673000
                          format: int64
                        status:
                          type: string
                          example: SUCCESS
                        tranId:
                          type: integer
                          example: 91077779
                          format: int64
                  count:
                    type: integer
                    example: 2
                    format: int64
  /sapi/v1/managed-subaccount/queryTransLogForTradeParent:
    get:
      summary: Query Managed Sub Account Transfer Log For Trading Team Master Account (USER_DATA)
      x-summary-cn: 查询托管子账户的划转记录 (适用交易团队母账户) (USER_DATA)
      description: >-
        Query Managed Sub Account Transfer Log For Trading Team Master Account


        Trading team can use this api to query managed sub account transfer log. This endpoint is available for trading

        team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in

        asset allocation and account application, while delegating trades to a professional trading team.


        Please refer to

        [link](https://www.binance.com/en/support/faq/how-to-get-started-with-managed-sub-account-functions-and-frequently-asked-questions-0594748722704383a7c369046e489459)
      x-description-cn: >-
        查询托管子账户的划转记录 (适用交易团队母账户)


        交易团队可以根据此接口查询其托管子账户划转记录。此接口可供托管子账户的交易团队使用。托管子账户是为重视资产配置与账户应用灵活性，并同时将交易委托专业交易团队的投资者的子账户类型。


        请参阅[链接](https://www.binance.com/zh-CN/support/faq/%E6%89%98%E7%AE%A1%E5%AD%90%E8%B4%A6%E6%88%B7%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D-0594748722704383a7c369046e489459)
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountTransferLogMasterAccountTrading
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-transfer-log-master-account-trading
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountTransferLogMasterAccountTrading.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_transfer_log_master_account_trading.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_transfer_log_master_account_trading.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountTransferLogMasterAccountTradingExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountTransferLogMasterAccountTrading/QueryManagedSubAccountTransferLogMasterAccountTrading.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountTransferLogMasterAccountTradingExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 60
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: email
          in: query
          required: true
          schema:
            type: string
            example: abc@test.com
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start Time
          x-description-cn: 开始时间
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time (The start time and end time interval cannot exceed half a year)
          x-description-cn: 结束时间(开始时间结束时间间隔不能超过半年)
        - name: page
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
        - name: limit
          in: query
          required: true
          schema:
            type: integer
            example: 10
            maximum: 500
            format: int64
        - name: transfers
          in: query
          required: false
          schema:
            type: string
            example: null
          description: Transfer Direction (FROM/TO)
          x-description-cn: 划转方向 (FROM/TO)
        - name: transferFunctionAccountType
          in: query
          required: false
          schema:
            type: string
            example: SPOT
            enum:
              - SPOT
              - MARGIN
              - ISOLATED_MARGIN
              - USDT_FUTURE
              - COIN_FUTURE
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
          description: Managed Sub Account Transfer Log
          x-description-cn: 查询托管子账户划转记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  managerSubTransferHistoryVos:
                    type: array
                    items:
                      type: object
                      properties:
                        fromEmail:
                          type: string
                          example: test_0_virtual@kq3kno9imanagedsub.com
                        fromAccountType:
                          type: string
                          example: SPOT
                        toEmail:
                          type: string
                          example: wdywl0lddakh@test.com
                        toAccountType:
                          type: string
                          example: SPOT
                        asset:
                          type: string
                          example: BNB
                        amount:
                          type: string
                          example: "0.01"
                        scheduledData:
                          type: integer
                          example: 1679416673000
                          format: int64
                        createTime:
                          type: integer
                          example: 1679416673000
                          format: int64
                        status:
                          type: string
                          example: SUCCESS
                        tranId:
                          type: integer
                          example: 91077779
                          format: int64
                  count:
                    type: integer
                    example: 2
                    format: int64
  /sapi/v1/managed-subaccount/query-trans-log:
    get:
      summary: Query Managed Sub Account Transfer Log (For Trading Team Sub Account) (USER_DATA)
      x-summary-cn: 查询托管子账户的划转记录 (适用交易团队子账户) (USER_DATA)
      description: Query Managed Sub Account Transfer Log (For Trading Team Sub Account)
      x-description-cn: 查询托管子账户的划转记录(适用交易团队子账户)
      tags:
        - managed-sub-account
      operationId: queryManagedSubAccountTransferLogSubAccountTrading
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#query-managed-sub-account-transfer-log-sub-account-trading
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/queryManagedSubAccountTransferLogSubAccountTrading.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/query_managed_sub_account_transfer_log_sub_account_trading.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/query_managed_sub_account_transfer_log_sub_account_trading.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/QueryManagedSubAccountTransferLogSubAccountTradingExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/QueryManagedSubAccountTransferLogSubAccountTrading/QueryManagedSubAccountTransferLogSubAccountTrading.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/QueryManagedSubAccountTransferLogSubAccountTradingExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 60
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
          description: Start Time
          x-description-cn: 开始时间
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End Time (The start time and end time interval cannot exceed half a year)
          x-description-cn: 结束时间(开始时间结束时间间隔不能超过半年)
        - name: page
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
        - name: limit
          in: query
          required: true
          schema:
            type: integer
            example: 10
            maximum: 500
            format: int64
        - name: transfers
          in: query
          required: false
          schema:
            type: string
            example: null
          description: Transfer Direction (from/to)
          x-description-cn: 划转方向 (from/to)
        - name: transferFunctionAccountType
          in: query
          required: false
          schema:
            type: string
            example: SPOT
            enum:
              - SPOT
              - MARGIN
              - ISOLATED_MARGIN
              - USDT_FUTURE
              - COIN_FUTURE
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Managed Sub Account Transfer Log
          x-description-cn: 查询托管子账户划转记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  managerSubTransferHistoryVos:
                    type: array
                    items:
                      type: object
                      properties:
                        fromEmail:
                          type: string
                          example: test_0_virtual@kq3kno9imanagedsub.com
                        fromAccountType:
                          type: string
                          example: SPOT
                        toEmail:
                          type: string
                          example: wdywl0lddakh@test.com
                        toAccountType:
                          type: string
                          example: SPOT
                        asset:
                          type: string
                          example: BNB
                        amount:
                          type: string
                          example: "0.01"
                        scheduledData:
                          type: integer
                          example: 1679416673000
                          format: int64
                        createTime:
                          type: integer
                          example: 1679416673000
                          format: int64
                        status:
                          type: string
                          example: SUCCESS
                        tranId:
                          type: integer
                          example: 91077779
                          format: int64
                  count:
                    type: integer
                    example: 2
                    format: int64
  /sapi/v1/managed-subaccount/withdraw:
    post:
      summary: Withdrawl Assets From The Managed Sub-account (For Investor Master Account) (USER_DATA)
      x-summary-cn: 投资人账户为托管子账户提币资产 (适用投资人母账户) (USER_DATA)
      description: Withdrawl Assets From The Managed Sub-account
      x-description-cn: 投资人账户为托管子账户提币资产
      tags:
        - managed-sub-account
      operationId: withdrawlAssetsFromTheManagedSubAccount
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/vip-and-institutional-sub-account/api/rest-api/managed-sub-account#withdrawl-assets-from-the-managed-sub-account
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/sub-account/examples/rest-api/ManagedSubAccountApi/withdrawlAssetsFromTheManagedSubAccount.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/sub_account/rest_api/managed_sub_account_api/withdrawl_assets_from_the_managed_sub_account.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/sub_account/examples/rest_api/ManagedSubAccount/withdrawl_assets_from_the_managed_sub_account.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/sub-account/src/main/java/com/binance/connector/client/sub_account/rest/managedsubaccount/WithdrawlAssetsFromTheManagedSubAccountExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/subaccount/examples/restapi/ManagedSubAccountAPI/WithdrawlAssetsFromTheManagedSubAccount/WithdrawlAssetsFromTheManagedSubAccount.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/sub-account/managedsubaccount/WithdrawlAssetsFromTheManagedSubAccountExample.php
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
      x-parameters-notes: "- Your API key must have the permission `Enable Spot & Margin Trading`."
      x-parameters-notes-cn: "- 您需要开通API Key`允许现货和杠杆交易`权限"
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - fromEmail
                - asset
                - amount
                - timestamp
              properties:
                fromEmail:
                  type: string
                  example: from@test.com
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
                transferDate:
                  type: integer
                  example: null
                  format: int64
                  description: |-
                    Withdrawal will happen automatically on the selected date (UTC 0). If no date is selected,
                    withdrawal takes effect immediately.
                  x-description-cn: 提币会自动发生在选择的日期(UTC0)，如果没有选择日期，提币会立即生效
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
                    Unix timestamp in milliseconds used to sign the request. The value must reflect the current client
                    time and is validated by the server for signed endpoints.
                  x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Withdrawl Assets From The Managed Sub-account
          x-description-cn: 从托管子账户提币资产
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 66157362489
                    format: int64
```