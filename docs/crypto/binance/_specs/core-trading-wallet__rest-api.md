---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:39:53.164101
---

# core-trading-wallet__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Wallet REST API
  description: Query balances, manage assets, and perform wallet operations via the Binance Wallet API.
  x-description-cn: 通过 Binance Wallet API 查询余额、管理资产并执行钱包操作。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/wallet/general-info#limits
x-rate-limits-guide-cn: products/wallet/general-info#访问限制
x-security-guide: products/wallet/general-info#request-security
x-security-guide-cn: products/wallet/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Wallet docs
  url: https://developers.binance.com/en/docs/products/wallet/Introduction
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户
  - name: asset
    x-displayName: Asset
    x-displayName-cn: 资产
  - name: capital
    x-displayName: Capital
    x-displayName-cn: 钱包
  - name: others
    x-displayName: Others
    x-displayName-cn: 其他
  - name: travel-rule
    x-displayName: Travel Rule
    x-displayName-cn: 旅行规则
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/account/apiTradingStatus:
    get:
      summary: Account API Trading Status (USER_DATA)
      x-summary-cn: 账户API交易状态 (USER_DATA)
      description: Fetch account api trading status detail.
      x-description-cn: 获取 api 账户交易状态详情。
      tags:
        - account
      operationId: accountApiTradingStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#account-api-trading-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/accountApiTradingStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/account_api_trading_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/account_api_trading_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/AccountApiTradingStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/AccountApiTradingStatus/AccountApiTradingStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/AccountApiTradingStatusExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Account API Trading Status
          x-description-cn: 账户 API 交易状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      isLocked:
                        type: boolean
                        example: false
                        description: API trading function is locked or not
                        x-description-cn: API交易功能是否被锁
                      plannedRecoverTime:
                        type: integer
                        example: 0
                        format: int64
                        description: If API trading function is locked, this is the planned recover time
                        x-description-cn: API交易功能被锁情况下的预计恢复时间
                      triggerCondition:
                        type: object
                        properties:
                          GCR:
                            type: integer
                            example: 150
                            format: int64
                            description: Number of GTC orders
                            x-description-cn: Number of GTC orders
                          IFER:
                            type: integer
                            example: 150
                            format: int64
                            description: Number of FOK/IOC orders
                            x-description-cn: Number of FOK/IOC orders
                          UFR:
                            type: integer
                            example: 300
                            format: int64
                            description: Number of orders
                            x-description-cn: Number of orders
                      updateTime:
                        type: integer
                        example: 1547630471725
                        format: int64
  /sapi/v1/account/info:
    get:
      summary: Account info (USER_DATA)
      x-summary-cn: 帐户信息 (USER_DATA)
      description: Fetch account info detail.
      x-description-cn: 获取帐户信息详情。
      tags:
        - account
      operationId: accountInfo
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#account-info
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/accountInfo.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/account_info.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/account_info.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/AccountInfoExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/AccountInfo/AccountInfo.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/AccountInfoExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Account info
          x-description-cn: 账户信息
          content:
            application/json:
              schema:
                type: object
                properties:
                  vipLevel:
                    type: integer
                    example: 0
                    format: int64
                  isMarginEnabled:
                    type: boolean
                    example: true
                    description: true or false for margin.
                    x-description-cn: 是否开通杠杆账户，true 或 false。
                  isFutureEnabled:
                    type: boolean
                    example: true
                    description: true or false for futures.
                    x-description-cn: 是否开通合约账户，true 或 false。
                  isOptionsEnabled:
                    type: boolean
                    example: true
                    description: true or false for options.
                    x-description-cn: 是否开通期权账户，true 或 false。
                  isPortfolioMarginRetailEnabled:
                    type: boolean
                    example: true
                    description: true or false for portfolio margin retail.
                    x-description-cn: 是否开通统一账户（零售版），true 或 false。
  /sapi/v1/account/status:
    get:
      summary: Account Status (USER_DATA)
      x-summary-cn: 账户状态 (USER_DATA)
      description: Fetch account status detail.
      x-description-cn: 账户状态(USER_DATA)
      tags:
        - account
      operationId: accountStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#account-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/accountStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/account_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/account_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/AccountStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/AccountStatus/AccountStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/AccountStatusExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Account Status
          x-description-cn: 账户 状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: string
                    example: Normal
  /sapi/v1/accountSnapshot:
    get:
      summary: Daily Account Snapshot (USER_DATA)
      x-summary-cn: 查询每日资产快照 (USER_DATA)
      description: Daily account snapshot
      x-description-cn: 查询每日资产快照
      tags:
        - account
      operationId: dailyAccountSnapshot
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#daily-account-snapshot
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/dailyAccountSnapshot.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/daily_account_snapshot.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/daily_account_snapshot.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/DailyAccountSnapshotExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/DailyAccountSnapshot/DailyAccountSnapshot.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/DailyAccountSnapshotExample.php
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
            example: 7
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
        - The query time period must be less then 30 days
        - Support query within the last one month only
        - If startTimeand endTime not sent, return records of the last 7 days by default
      x-parameters-notes-cn: |-
        - The 查询 时间 period must be less then 30 days
        - Support 查询 within the last one month 仅
        - If 开始 Timeand 结束 时间 not sent, return records of the last 7 days by 默认
      responses:
        "200":
          description: Daily Account Snapshot
          x-description-cn: 每日账户快照
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
                                    description: Not real-time data, can ignore
                                    x-description-cn: 不会实时更新，可以忽略
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
  /sapi/v1/account/disableFastWithdrawSwitch:
    post:
      summary: Disable Fast Withdraw Switch (USER_DATA)
      x-summary-cn: 关闭站内划转 (USER_DATA)
      description: Disable Fast Withdraw Switch
      x-description-cn: 关闭站内划转
      tags:
        - account
      operationId: disableFastWithdrawSwitch
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#disable-fast-withdraw-switch
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/disableFastWithdrawSwitch.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/disable_fast_withdraw_switch.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/disable_fast_withdraw_switch.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/DisableFastWithdrawSwitchExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/DisableFastWithdrawSwitch/DisableFastWithdrawSwitch.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/DisableFastWithdrawSwitchExample.php
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
        - This request will disable fastwithdraw switch under your account. You need to enable "trade" option for the
        api key which requests this endpoint.
      x-parameters-notes-cn: '- 此请求会关闭您账户的站内快速划转。您需要为api-key开通"trade"权限才能发送此请求。'
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
          description: OK
          x-description-cn: 成功
  /sapi/v1/account/enableFastWithdrawSwitch:
    post:
      summary: Enable Fast Withdraw Switch (USER_DATA)
      x-summary-cn: 开启站内划转 (USER_DATA)
      description: Enable Fast Withdraw Switch (USER_DATA)
      x-description-cn: 开启站内划转(USER_DATA)
      tags:
        - account
      operationId: enableFastWithdrawSwitch
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#enable-fast-withdraw-switch
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/enableFastWithdrawSwitch.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/enable_fast_withdraw_switch.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/enable_fast_withdraw_switch.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/EnableFastWithdrawSwitchExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/EnableFastWithdrawSwitch/EnableFastWithdrawSwitch.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/EnableFastWithdrawSwitchExample.php
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
        - This request will enable fastwithdraw switch under your account. You need to enable "trade" option for the api
        key which requests this endpoint.

        - When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no
        on-chain transaction, no transaction ID and no withdrawal fee.
      x-parameters-notes-cn: |-
        - 此请求会开启您账户的站内快速划转。您需要为api-key开通"trade"权限才能发送此请求。
        - 开启以后, 如果收款方为币安账户地址，转账费用为0, 速度快, 不需要提交上链请求。
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
          description: OK
          x-description-cn: 成功
  /sapi/v1/account/apiRestrictions:
    get:
      summary: Get API Key Permission (USER_DATA)
      x-summary-cn: 查询用户API Key权限 (USER_DATA)
      description: Get API Key Permission
      x-description-cn: 查询用户 API Key 权限
      tags:
        - account
      operationId: getApiKeyPermission
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/account#get-api-key-permission
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AccountApi/getApiKeyPermission.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/account_api/get_api_key_permission.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Account/get_api_key_permission.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/account/GetApiKeyPermissionExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AccountAPI/GetApiKeyPermission/GetApiKeyPermission.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/account/GetApiKeyPermissionExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get API Key Permission
          x-description-cn: 查询 API Key 权限
          content:
            application/json:
              schema:
                type: object
                properties:
                  ipRestrict:
                    type: boolean
                    example: false
                  createTime:
                    type: integer
                    example: 1623840271000
                    format: int64
                  enableReading:
                    type: boolean
                    example: true
                  enableWithdrawals:
                    type: boolean
                    example: false
                    description: >-
                      This option allows you to withdraw via API. You must apply the IP Access Restriction filter in
                      order to enable withdrawals
                    x-description-cn: 此选项允许通过此api提现。开启提现选项必须添加IP访问限制过滤器
                  enableInternalTransfer:
                    type: boolean
                    example: true
                    description: >-
                      This option authorizes this key to transfer funds between your master account and your sub account
                      instantly
                    x-description-cn: 此选项授权此密钥在您的母账户和子账户之间划转资金
                  enableMargin:
                    type: boolean
                    example: false
                    description: This option can be adjusted after the Cross Margin account transfer is completed
                    x-description-cn: 此选项在全仓账户完成划转后可编辑
                  enableFutures:
                    type: boolean
                    example: false
                    description: >-
                      The Futures API cannot be used if the API key was created before the Futures account was opened,
                      or if you have enabled portfolio margin.
                    x-description-cn: 合约交易权限，需注意开通合约账户之前创建的API Key，或已开通统一账户的API Key，不支持合约API功能
                  permitsUniversalTransfer:
                    type: boolean
                    example: true
                    description: >-
                      Authorizes this key to be used for a dedicated universal transfer API to transfer multiple
                      supported currencies. Each business's own transfer API rights are not affected by this
                      authorization
                    x-description-cn: 授权该密钥可用于专用的万向划转接口，用以操作其支持的多种类型资金划转。各业务自身的划转接口使用权限，不受本授权影响
                  enableVanillaOptions:
                    type: boolean
                    example: false
                    description: Authorizes this key to Vanilla options trading
                    x-description-cn: 欧式期权交易权限
                  enableFixApiTrade:
                    type: boolean
                    example: false
                  enableFixReadOnly:
                    type: boolean
                    example: true
                  enableSpotAndMarginTrading:
                    type: boolean
                    example: false
                    description: Spot and margin trading
                    x-description-cn: 现货和杠杆交易权限
                  enablePortfolioMarginTrading:
                    type: boolean
                    example: true
                    description: >-
                      API Key created before your activate portfolio margin does not support portfolio margin API
                      service
                    x-description-cn: 统一账户交易权限，需注意开通统一账户之前创建的API Key不支持统一账户API功能
  /sapi/v1/asset/assetDetail:
    get:
      summary: Asset Detail (USER_DATA)
      x-summary-cn: 上架资产详情 (USER_DATA)
      description: Fetch details of assets supported on Binance.
      x-description-cn: 获取上架资产详情
      tags:
        - asset
      operationId: assetDetail
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#asset-detail
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/assetDetail.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/asset_detail.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/asset_detail.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/AssetDetailExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/AssetDetail/AssetDetail.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/AssetDetailExample.php
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
      x-parameters-notes: "- Please get network and other deposit or withdraw details from `GET /sapi/v1/capital/config/getall`."
      x-parameters-notes-cn: "- 充提币信息，建议查询 `GET /sapi/v1/capital/config/getall` 获取详情。"
      responses:
        "200":
          description: Asset Detail
          x-description-cn: 资产 Detail
          content:
            application/json:
              schema:
                type: object
                properties:
                  CTR:
                    type: object
                    properties:
                      minWithdrawAmount:
                        type: string
                        example: "70.00000000"
                        description: min withdraw amount
                        x-description-cn: 最小提现数量
                      depositStatus:
                        type: boolean
                        example: false
                        description: deposit status (false if ALL of networks' are false)
                        x-description-cn: 是否可以充值(只有所有网络都关闭充值才为false)
                      withdrawFee:
                        type: integer
                        example: 35
                        format: int64
                        description: withdraw fee
                        x-description-cn: 提现手续费
                      withdrawStatus:
                        type: boolean
                        example: true
                        description: withdraw status (false if ALL of networks' are false)
                        x-description-cn: 是否开放提现(只有所有网络都关闭提币才为false)
                      depositTip:
                        type: string
                        example: Delisted, Deposit Suspended
                        description: reason
                        x-description-cn: 暂停充值的原因(如果暂停才有这一项)
                  SKY:
                    type: object
                    properties:
                      minWithdrawAmount:
                        type: string
                        example: "0.02000000"
                        description: min withdraw amount
                        x-description-cn: 最小提现数量
                      depositStatus:
                        type: boolean
                        example: true
                        description: deposit status (false if ALL of networks' are false)
                        x-description-cn: 是否可以充值(只有所有网络都关闭充值才为false)
                      withdrawFee:
                        type: number
                        example: 0.01
                        format: float
                        description: withdraw fee
                        x-description-cn: 提现手续费
                      withdrawStatus:
                        type: boolean
                        example: true
                        description: withdraw status (false if ALL of networks' are false)
                        x-description-cn: 是否开放提现(只有所有网络都关闭提币才为false)
  /sapi/v1/asset/assetDividend:
    get:
      summary: Asset Dividend Record (USER_DATA)
      x-summary-cn: 资产利息记录 (USER_DATA)
      description: Query asset dividend record.
      x-description-cn: 获取资产利息记录。
      tags:
        - asset
      operationId: assetDividendRecord
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#asset-dividend-record
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/assetDividendRecord.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/asset_dividend_record.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/asset_dividend_record.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/AssetDividendRecordExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/AssetDividendRecord/AssetDividendRecord.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/AssetDividendRecordExample.php
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
          required: false
          schema:
            type: string
            example: BTC
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
            example: 20
            default: 20
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
      x-parameters-notes: "- There cannot be more than 180 days between parameter `startTime` and `endTime`."
      x-parameters-notes-cn: "- `startTime` 与 `endTime`之间最多只可以相差180天。"
      responses:
        "200":
          description: Asset Dividend Record
          x-description-cn: 资产分红记录
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
                        id:
                          type: integer
                          example: 1637366104
                          format: int64
                        amount:
                          type: string
                          example: "10.00000000"
                        asset:
                          type: string
                          example: BHFT
                        divTime:
                          type: integer
                          example: 1563189166000
                          format: int64
                        enInfo:
                          type: string
                          example: BHFT distribution
                        tranId:
                          type: integer
                          example: 2968885920
                          format: int64
                        direction:
                          type: integer
                          example: 1
                          format: int64
                          description: "direction: 1 for Asset credited (inflow), -1 for Asset debited (outflow)"
                          x-description-cn: direction：1 表示资产记账入账（资产流入），-1 表示资产记账出账（资产流出）
                  total:
                    type: integer
                    example: 2
                    format: int64
  /sapi/v1/asset/dust-convert/convert:
    post:
      summary: Dust Convert (USER_DATA)
      x-summary-cn: 小额资产兑换 (USER_DATA)
      description: Convert dust assets
      x-description-cn: 小额兑换
      tags:
        - asset
      operationId: dustConvert
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#dust-convert
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/dustConvert.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/dust_convert.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/dust_convert.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/DustConvertExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/DustConvert/DustConvert.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/DustConvertExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 10
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
                - timestamp
              properties:
                asset:
                  type: string
                  example: USDT
                accountType:
                  type: string
                  example: SPOT
                  description: "`SPOT` or `MARGIN`, default `SPOT`"
                  x-description-cn: "`SPOT` 或 `MARGIN`，默认 `SPOT`"
                clientId:
                  type: string
                  example: "1"
                  description: A unique id for the request
                  x-description-cn: 用户自定义的请求号 ｜
                targetAsset:
                  type: string
                  example: BTC
                thirdPartyClientId:
                  type: string
                  example: "1"
                dustQuotaAssetToTargetAssetPrice:
                  type: number
                  example: "1.0"
                  format: float
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
          description: Dust Convert
          x-description-cn: 小额资产兑换
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalTransfered:
                    type: string
                    example: "3.5971223"
                  totalServiceCharge:
                    type: string
                    example: "0.0794964"
                  transferResult:
                    type: array
                    items:
                      type: object
                      properties:
                        tranId:
                          type: integer
                          example: 2987331510
                          format: int64
                        fromAsset:
                          type: string
                          example: USDT
                        amount:
                          type: string
                          example: "1"
                        transferedAmount:
                          type: string
                          example: "3.5971223"
                        serviceChargeAmount:
                          type: string
                          example: "0.0794964"
                        operateTime:
                          type: integer
                          example: 1765212029749
                          format: int64
  /sapi/v1/asset/dust-convert/query-convertible-assets:
    post:
      summary: Dust Convertible Assets (USER_DATA)
      x-summary-cn: 小额可以兑换的资产 (USER_DATA)
      description: Query dust convertible assets
      x-description-cn: 获取小额可以兑换的资产
      tags:
        - asset
      operationId: dustConvertibleAssets
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#dust-convertible-assets
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/dustConvertibleAssets.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/dust_convertible_assets.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/dust_convertible_assets.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/DustConvertibleAssetsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/DustConvertibleAssets/DustConvertibleAssets.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/DustConvertibleAssetsExample.php
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
                - targetAsset
                - timestamp
              properties:
                accountType:
                  type: string
                  example: SPOT
                  description: "`SPOT` or `MARGIN`, default `SPOT`"
                  x-description-cn: "`SPOT` 或 `MARGIN`，默认 `SPOT`"
                targetAsset:
                  type: string
                  example: BTC
                dustQuotaAssetToTargetAssetPrice:
                  type: number
                  example: "1.0"
                  format: float
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
          description: Dust Convertible Assets
          x-description-cn: 可兑换小额资产
          content:
            application/json:
              schema:
                type: object
                properties:
                  dribbletPercentage:
                    type: string
                    example: "0.02"
                  totalTransferQuotaAssetAmount:
                    type: string
                    example: "0.7899968"
                  totalTransferTargetAssetAmount:
                    type: string
                    example: "0.7899968"
                  dribbletBase:
                    type: string
                    example: "10"
                  details:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: AR
                        assetFullName:
                          type: string
                          example: AR
                        amountFree:
                          type: string
                          example: "0.00856"
                        exchange:
                          type: string
                          example: "0.00073616"
                        toQuotaAssetAmount:
                          type: string
                          example: "0.036808"
                        toTargetAssetAmount:
                          type: string
                          example: "0.036808"
                        toTargetAssetOffExchange:
                          type: string
                          example: "0.03607184"
  /sapi/v1/asset/dribblet:
    get:
      summary: DustLog (USER_DATA)
      x-summary-cn: 小额资产转换BNB历史 (USER_DATA)
      description: Dustlog
      x-description-cn: 小额资产转换BNB历史(USER_DATA)
      tags:
        - asset
      operationId: dustlog
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#dustlog
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/dustlog.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/dustlog.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/dustlog.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/DustlogExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/Dustlog/Dustlog.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/DustlogExample.php
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
        - name: accountType
          in: query
          required: false
          schema:
            type: string
            example: SPOT
            enum:
              - SPOT
              - MARGIN
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
        - Only return last 100 records
        - Only return records after 2020/12/01
      x-parameters-notes-cn: |-
        - 只返回最近100条记录
        - 只返回 2020/12/01 之后记录
      responses:
        "200":
          description: DustLog
          x-description-cn: 小额资产兑换记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 8
                    format: int64
                    description: Total counts of exchange
                    x-description-cn: 共计发生过的转换笔数
                  userAssetDribblets:
                    type: array
                    items:
                      type: object
                      properties:
                        operateTime:
                          type: integer
                          example: 1615985535000
                          format: int64
                        totalTransferedAmount:
                          type: string
                          example: "0.00132256"
                          description: Total transfered BNB amount for this exchange.
                          x-description-cn: 本次转换所得BNB
                        totalServiceChargeAmount:
                          type: string
                          example: "0.00002699"
                          description: Total service charge amount for this exchange.
                          x-description-cn: 本次转换手续费(BNB)
                        transId:
                          type: integer
                          example: 45178372831
                          format: int64
                        userAssetDribbletDetails:
                          type: array
                          items:
                            type: object
                            properties:
                              transId:
                                type: integer
                                example: 4359321
                                format: int64
                              serviceChargeAmount:
                                type: string
                                example: "0.000009"
                              amount:
                                type: string
                                example: "0.0009"
                              operateTime:
                                type: integer
                                example: 1615985535000
                                format: int64
                              transferedAmount:
                                type: string
                                example: "0.000441"
                              fromAsset:
                                type: string
                                example: USDT
                              targetAsset:
                                type: string
                                example: BNB
  /sapi/v1/asset/dust:
    post:
      summary: Dust Transfer (USER_DATA)
      x-summary-cn: 小额资产转换 (USER_DATA)
      description: Convert dust assets to BNB.
      x-description-cn: 小额资产转换
      tags:
        - asset
      operationId: dustTransfer
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#dust-transfer
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/dustTransfer.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/dust_transfer.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/dust_transfer.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/DustTransferExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/DustTransfer/DustTransfer.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/DustTransferExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 10
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
      x-parameters-notes: "- You need to open`Enable Spot & Margin Trading` permission for the API Key which requests this endpoint."
      x-parameters-notes-cn: "- 您需要为API Key开通`允许现货和杠杆交易`权限才能发送此请求"
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
                  description: "The asset being converted. For example: asset=BTC,USDT"
                  x-description-cn: 正在转换的资产。 例如：asset=BTC,USDT
                accountType:
                  type: string
                  example: SPOT
                  default: SPOT
                  enum:
                    - SPOT
                    - MARGIN
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
          description: Dust Transfer
          x-description-cn: Dust 划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalServiceCharge:
                    type: string
                    example: "0.02102542"
                  totalTransfered:
                    type: string
                    example: "1.05127099"
                  transferResult:
                    type: array
                    items:
                      type: object
                      properties:
                        amount:
                          type: string
                          example: "0.03000000"
                        fromAsset:
                          type: string
                          example: ETH
                        operateTime:
                          type: integer
                          example: 1563368549307
                          format: int64
                        serviceChargeAmount:
                          type: string
                          example: "0.00500000"
                        tranId:
                          type: integer
                          example: 2970932918
                          format: int64
                        transferedAmount:
                          type: string
                          example: "0.25000000"
  /sapi/v1/asset/get-funding-asset:
    post:
      summary: Funding Wallet (USER_DATA)
      x-summary-cn: 查询资金账户 (USER_DATA)
      description: Query Funding Wallet
      x-description-cn: 查询资金账户(USER_DATA)
      tags:
        - asset
      operationId: fundingWallet
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#funding-wallet
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/fundingWallet.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/funding_wallet.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/funding_wallet.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/FundingWalletExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/FundingWallet/FundingWallet.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/FundingWalletExample.php
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
        - Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card, Stock
        Token
      x-parameters-notes-cn: '- 目前仅支持查询以下业务资产：Binance Pay, Binance Card, Binance Gift Card, Stock Token"'
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - timestamp
              properties:
                asset:
                  type: string
                  example: BTC
                needBtcValuation:
                  type: boolean
                  example: true
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
          description: Funding Wallet
          x-description-cn: 资金钱包
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
                    free:
                      type: string
                      example: "1"
                      description: avalible balance
                      x-description-cn: 可用余额
                    locked:
                      type: string
                      example: "0"
                      description: locked asset
                      x-description-cn: 锁定资金
                    freeze:
                      type: string
                      example: "0"
                      description: freeze asset
                      x-description-cn: 冻结资金
                    withdrawing:
                      type: string
                      example: "0"
                    btcValuation:
                      type: string
                      example: "0.00000091"
  /sapi/v1/spot/asset/tags:
    get:
      summary: Get Spot Asset Tags (MARKET_DATA)
      x-summary-cn: 查询现货资产标签 (MARKET_DATA)
      description: Get the tags configured for spot-tradable assets.
      x-description-cn: 查询现货可交易资产配置的标签。
      tags:
        - asset
      operationId: getSpotAssetTags
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#get-spot-asset-tags
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/getSpotAssetTags.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/get_spot_asset_tags.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/get_spot_asset_tags.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/GetSpotAssetTagsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/GetSpotAssetTags/GetSpotAssetTags.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/GetSpotAssetTagsExample.php
      x-ip-weight: 100
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
        - name: tag
          in: query
          required: false
          schema:
            type: string
            example: Layer1_Layer2,BSC
          description: >-
            Tag filter. Supports multiple comma-separated tags with OR semantics (an asset is returned if it matches any
            one tag); leading/trailing whitespace around each tag is ignored. Returns all eligible assets when omitted.
          x-description-cn: 标签过滤条件。支持逗号分隔多个标签，任一标签命中即返回；会忽略标签前后空白。未传时返回全部符合条件的资产。
      responses:
        "200":
          description: Get Spot Asset Tags
          x-description-cn: 查询现货资产标签
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    assetCode:
                      type: string
                      example: BNB
                      description: Asset code.
                      x-description-cn: 资产代码。
                    assetName:
                      type: string
                      example: BNB
                      description: Asset name.
                      x-description-cn: 资产名称。
                    trading:
                      type: boolean
                      example: true
                      description: Asset trading status. This endpoint only returns `true`.
                      x-description-cn: 资产交易状态；此接口只会返回 `true`。
                    tags:
                      type: array
                      example:
                        - Layer1_Layer2
                        - BSC
                      items:
                        type: string
                      description: Tags configured for the asset. Returns an empty array when the asset has no tags.
                      x-description-cn: 该资产配置的标签；没有标签时返回空数组。
  /sapi/v1/asset/dust-btc:
    post:
      summary: Get Assets That Can Be Converted Into BNB (USER_DATA)
      x-summary-cn: 获取可以转换成BNB的小额资产 (USER_DATA)
      description: Get Assets That Can Be Converted Into BNB
      x-description-cn: 获取可以转换成BNB的小额资产
      tags:
        - asset
      operationId: getAssetsThatCanBeConvertedIntoBnb
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#get-assets-that-can-be-converted-into-bnb
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/getAssetsThatCanBeConvertedIntoBnb.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/get_assets_that_can_be_converted_into_bnb.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/get_assets_that_can_be_converted_into_bnb.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/GetAssetsThatCanBeConvertedIntoBnbExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/GetAssetsThatCanBeConvertedIntoBnb/GetAssetsThatCanBeConvertedIntoBnb.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/GetAssetsThatCanBeConvertedIntoBnbExample.php
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
                - timestamp
              properties:
                accountType:
                  type: string
                  example: SPOT
                  default: SPOT
                  enum:
                    - SPOT
                    - MARGIN
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
          description: Get Assets That Can Be Converted Into BNB
          x-description-cn: 获取Assets That Can Be Converted Into BNB
          content:
            application/json:
              schema:
                type: object
                properties:
                  details:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: ADA
                        assetFullName:
                          type: string
                          example: ADA
                        amountFree:
                          type: string
                          example: "6.21"
                          description: Convertible amount
                          x-description-cn: 可转换数量
                        toBTC:
                          type: string
                          example: "0.00016848"
                          description: BTC amount
                          x-description-cn: 等值BTC
                        toBNB:
                          type: string
                          example: "0.01777302"
                          description: BNB amount（Not deducted commission fee）
                          x-description-cn: 可转换BNB（未扣除手续费）
                        toBNBOffExchange:
                          type: string
                          example: "0.01741756"
                          description: BNB amount（Deducted commission fee）
                          x-description-cn: 可转换BNB（已扣除手续费）
                        exchange:
                          type: string
                          example: "0.00035546"
                          description: Commission fee
                          x-description-cn: 手续费
                  totalTransferBtc:
                    type: string
                    example: "0.00016848"
                  totalTransferBNB:
                    type: string
                    example: "0.01777302"
                  dribbletPercentage:
                    type: string
                    example: "0.02"
                    description: Commission fee
                    x-description-cn: 转换手续费
  /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage:
    get:
      summary: Get Cloud-Mining payment and refund history (USER_DATA)
      x-summary-cn: 云算力历史记录分页查询 (USER_DATA)
      description: The query of Cloud-Mining payment and refund history
      x-description-cn: 云算力支付和退款历史分页查询
      tags:
        - asset
      operationId: getCloudMiningPaymentAndRefundHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#get-cloud-mining-payment-and-refund-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/getCloudMiningPaymentAndRefundHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/get_cloud_mining_payment_and_refund_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/get_cloud_mining_payment_and_refund_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/GetCloudMiningPaymentAndRefundHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/GetCloudMiningPaymentAndRefundHistory/GetCloudMiningPaymentAndRefundHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/GetCloudMiningPaymentAndRefundHistoryExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 600
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: tranId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: The transaction id
          x-description-cn: 流水号
        - name: clientTranId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: The unique flag
          x-description-cn: 外部唯一流水号
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: BTC
          description: If it is blank, we will query all assets
          x-description-cn: 不传或者空字符串查全部
        - name: startTime
          in: query
          required: true
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "inclusive, unit: ms"
          x-description-cn: 开始时间（包含），单位：毫秒
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "exclusive, unit: ms"
          x-description-cn: 结束时间（不包含），单位：毫秒
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            minimum: 1
            format: int64
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 10
            maximum: 100
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
        - Just return the SUCCESS records of payment and refund.
        - For response, type = 248 means payment, type = 249 means refund, status =S means SUCCESS.
      x-parameters-notes-cn: |-
        - Just return the SUCCESS records of payment 和 refund.
        - 用于 响应, 类型 = 248 means payment, 类型 = 249 means refund, 状态 =S means SUCCESS.
      responses:
        "200":
          description: Get Cloud-Mining payment and refund history
          x-description-cn: 获取云算力支付和退款历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 5
                    format: int64
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        createTime:
                          type: integer
                          example: 1667880112000
                          format: int64
                        tranId:
                          type: integer
                          example: 121230610120
                          format: int64
                        type:
                          type: integer
                          example: 248
                          format: int64
                        asset:
                          type: string
                          example: USDT
                        amount:
                          type: string
                          example: "25.0068"
                        status:
                          type: string
                          example: S
  /sapi/v1/spot/open-symbol-list:
    get:
      summary: Get Open Symbol List (MARKET_DATA)
      x-summary-cn: 查询开放币对列表 (MARKET_DATA)
      description: |-
        Get the list of symbols that are scheduled to be opened for trading in
        the market.
      x-description-cn: 查询即将开放交易的币对列表。
      tags:
        - asset
      operationId: getOpenSymbolList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#get-open-symbol-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/getOpenSymbolList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/get_open_symbol_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/get_open_symbol_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/GetOpenSymbolListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/GetOpenSymbolList/GetOpenSymbolList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/GetOpenSymbolListExample.php
      x-ip-weight: 100
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
          description: Get Open Symbol List
          x-description-cn: 获取未完成交易对 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    openTime:
                      type: integer
                      example: 1686161202000
                      format: int64
                    symbols:
                      type: array
                      items:
                        type: string
                        example: BNBBTC
  /sapi/v1/asset/custody/transfer-history:
    get:
      summary: Query User Delegation History(For Master Account) (USER_DATA)
      x-summary-cn: 查询用户委托资金历史(适用主账户) (USER_DATA)
      description: Query User Delegation History
      x-description-cn: 查询用户委托资金历史
      tags:
        - asset
      operationId: queryUserDelegationHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#query-user-delegation-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/queryUserDelegationHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/query_user_delegation_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/query_user_delegation_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/QueryUserDelegationHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/QueryUserDelegationHistory/QueryUserDelegationHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/QueryUserDelegationHistoryExample.php
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
        - name: endTime
          in: query
          required: true
          schema:
            type: integer
            example: 1641782889000
            format: int64
        - name: type
          in: query
          required: false
          schema:
            type: string
            example: Delegate
            enum:
              - DELEGATE
              - UNDELEGATE
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: BTC
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            minimum: 1
            format: int64
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 10
            maximum: 100
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
          description: User Delegation History
          x-description-cn: 用户委托历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 3316
                    format: int64
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        clientTranId:
                          type: string
                          example: "293915932290879488"
                        transferType:
                          type: string
                          example: Undelegate
                        asset:
                          type: string
                          example: ETH
                        amount:
                          type: string
                          example: "1"
                        time:
                          type: integer
                          example: 1695205406000
                          format: int64
  /sapi/v1/asset/transfer:
    get:
      summary: Query User Universal Transfer History (USER_DATA)
      x-summary-cn: 查询用户万向划转历史 (USER_DATA)
      description: Query User Universal Transfer History
      x-description-cn: 查询用户万向划转历史
      tags:
        - asset
      operationId: queryUserUniversalTransferHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#query-user-universal-transfer-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/queryUserUniversalTransferHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/query_user_universal_transfer_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/query_user_universal_transfer_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/QueryUserUniversalTransferHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/QueryUserUniversalTransferHistory/QueryUserUniversalTransferHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/QueryUserUniversalTransferHistoryExample.php
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
        - name: type
          in: query
          required: true
          schema:
            type: string
            example: null
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
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            default: 1
            minimum: 1
            format: int64
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            default: 10
            maximum: 100
            format: int64
        - name: fromSymbol
          in: query
          required: false
          schema:
            type: string
            example: ISOLATEDMARGIN_MARGIN
            enum:
              - ISOLATEDMARGIN_MARGIN
              - ISOLATEDMARGIN_ISOLATEDMARGIN
        - name: toSymbol
          in: query
          required: false
          schema:
            type: string
            example: MARGIN_ISOLATEDMARGIN
            enum:
              - MARGIN_ISOLATEDMARGIN
              - ISOLATEDMARGIN_ISOLATEDMARGIN
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
        - `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - Support query within the last 6 months only
        - If `startTime`and `endTime` not sent, return records of the last 7 days by default
      x-parameters-notes-cn: |-
        - `fromSymbol` 必须要发送，当类型为 ISOLATEDMARGIN_MARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN
        - `toSymbol` 必须要发送，当类型为 MARGIN_ISOLATEDMARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN
        - 仅支持查询最近半年（6个月）数据
        - 若`startTime`和`endTime`没传，则默认返回最近7天数据
      responses:
        "200":
          description: User Universal Transfer History
          x-description-cn: 用户万向划转历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 2
                    format: int64
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          type: string
                          example: USDT
                        amount:
                          type: string
                          example: "1"
                        type:
                          type: string
                          example: MAIN_UMFUTURE
                        status:
                          type: string
                          example: CONFIRMED
                          description: "status: CONFIRMED / FAILED / PENDING"
                          x-description-cn: "status: CONFIRMED / FAILED / PENDING"
                        tranId:
                          type: integer
                          example: 11415955596
                          format: int64
                        timestamp:
                          type: integer
                          example: 1544433328000
                          format: int64
    post:
      summary: User Universal Transfer (USER_DATA)
      x-summary-cn: 用户万向划转 (USER_DATA)
      description: User universal transfer
      x-description-cn: 用户万向划转
      tags:
        - asset
      operationId: userUniversalTransfer
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#user-universal-transfer
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/userUniversalTransfer.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/user_universal_transfer.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/user_universal_transfer.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/UserUniversalTransferExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/UserUniversalTransfer/UserUniversalTransfer.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/UserUniversalTransferExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 300
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - You need to enable Permits Universal Transfer option for the API Key that requests this endpoint.
        - `fromSymbol` must be sent when type is `ISOLATEDMARGIN_MARGIN` or `ISOLATEDMARGIN_ISOLATEDMARGIN`.
        - `toSymbol` must be sent when type is `MARGIN_ISOLATEDMARGIN` or `ISOLATEDMARGIN_ISOLATEDMARGIN`.
        - ENUM of transfer types:
        - `MAIN_UMFUTURE`: Spot → USDⓈ-M Futures
        - `MAIN_CMFUTURE`: Spot → COIN-M Futures
        - `MAIN_MARGIN`: Spot → Margin (cross)
        - `UMFUTURE_MAIN`: USDⓈ-M Futures → Spot
        - `UMFUTURE_MARGIN`: USDⓈ-M Futures → Margin (cross)
        - `CMFUTURE_MAIN`: COIN-M Futures → Spot
        - `CMFUTURE_MARGIN`: COIN-M Futures → Margin (cross)
        - `MARGIN_MAIN`: Margin (cross) → Spot
        - `MARGIN_UMFUTURE`: Margin (cross) → USDⓈ-M Futures
        - `MARGIN_CMFUTURE`: Margin (cross) → COIN-M Futures
        - `ISOLATEDMARGIN_MARGIN`: Isolated margin → Margin (cross)
        - `MARGIN_ISOLATEDMARGIN`: Margin (cross) → Isolated margin
        - `ISOLATEDMARGIN_ISOLATEDMARGIN`: Isolated margin → Isolated margin
        - `MAIN_FUNDING`: Spot → Funding
        - `FUNDING_MAIN`: Funding → Spot
        - `FUNDING_UMFUTURE`: Funding → USDⓈ-M Futures
        - `UMFUTURE_FUNDING`: USDⓈ-M Futures → Funding
        - `MARGIN_FUNDING`: Margin (cross) → Funding
        - `FUNDING_MARGIN`: Funding → Margin (cross)
        - `FUNDING_CMFUTURE`: Funding → COIN-M Futures
        - `CMFUTURE_FUNDING`: COIN-M Futures → Funding
        - `MAIN_OPTION`: Spot → Options
        - `OPTION_MAIN`: Options → Spot
        - `UMFUTURE_OPTION`: USDⓈ-M Futures → Options
        - `OPTION_UMFUTURE`: Options → USDⓈ-M Futures
        - `MARGIN_OPTION`: Margin (cross) → Options
        - `OPTION_MARGIN`: Options → Margin (cross)
        - `FUNDING_OPTION`: Funding → Options
        - `OPTION_FUNDING`: Options → Funding
        - `MAIN_PORTFOLIO_MARGIN`: Spot → Portfolio Margin
        - `PORTFOLIO_MARGIN_MAIN`: Portfolio Margin → Spot
      x-parameters-notes-cn: |-
        - 请求此接口的 API Key 需要开启允许万向划转权限。
        - 当 type 为 `ISOLATEDMARGIN_MARGIN` 或 `ISOLATEDMARGIN_ISOLATEDMARGIN` 时，`fromSymbol` 为必填项。
        - 当 type 为 `MARGIN_ISOLATEDMARGIN` 或 `ISOLATEDMARGIN_ISOLATEDMARGIN` 时，`toSymbol` 为必填项。
        - 划转类型枚举值：
        - `MAIN_UMFUTURE`：现货 → USDⓈ-M 合约
        - `MAIN_CMFUTURE`：现货 → COIN-M 合约
        - `MAIN_MARGIN`：现货 → 全仓杠杆
        - `UMFUTURE_MAIN`：USDⓈ-M 合约 → 现货
        - `UMFUTURE_MARGIN`：USDⓈ-M 合约 → 全仓杠杆
        - `CMFUTURE_MAIN`：COIN-M 合约 → 现货
        - `CMFUTURE_MARGIN`：COIN-M 合约 → 全仓杠杆
        - `MARGIN_MAIN`：全仓杠杆 → 现货
        - `MARGIN_UMFUTURE`：全仓杠杆 → USDⓈ-M 合约
        - `MARGIN_CMFUTURE`：全仓杠杆 → COIN-M 合约
        - `ISOLATEDMARGIN_MARGIN`：逐仓杠杆 → 全仓杠杆
        - `MARGIN_ISOLATEDMARGIN`：全仓杠杆 → 逐仓杠杆
        - `ISOLATEDMARGIN_ISOLATEDMARGIN`：逐仓杠杆 → 逐仓杠杆
        - `MAIN_FUNDING`：现货 → 资金账户
        - `FUNDING_MAIN`：资金账户 → 现货
        - `FUNDING_UMFUTURE`：资金账户 → USDⓈ-M 合约
        - `UMFUTURE_FUNDING`：USDⓈ-M 合约 → 资金账户
        - `MARGIN_FUNDING`：全仓杠杆 → 资金账户
        - `FUNDING_MARGIN`：资金账户 → 全仓杠杆
        - `FUNDING_CMFUTURE`：资金账户 → COIN-M 合约
        - `CMFUTURE_FUNDING`：COIN-M 合约 → 资金账户
        - `MAIN_OPTION`：现货 → 期权
        - `OPTION_MAIN`：期权 → 现货
        - `UMFUTURE_OPTION`：USDⓈ-M 合约 → 期权
        - `OPTION_UMFUTURE`：期权 → USDⓈ-M 合约
        - `MARGIN_OPTION`：全仓杠杆 → 期权
        - `OPTION_MARGIN`：期权 → 全仓杠杆
        - `FUNDING_OPTION`：资金账户 → 期权
        - `OPTION_FUNDING`：期权 → 资金账户
        - `MAIN_PORTFOLIO_MARGIN`：现货 → 统一账户
        - `PORTFOLIO_MARGIN_MAIN`：统一账户 → 现货
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - type
                - asset
                - amount
                - timestamp
              properties:
                type:
                  type: string
                  example: MAIN_UMFUTURE
                  enum:
                    - MAIN_UMFUTURE
                    - MAIN_CMFUTURE
                    - MAIN_MARGIN
                    - UMFUTURE_MAIN
                    - UMFUTURE_MARGIN
                    - CMFUTURE_MAIN
                    - CMFUTURE_MARGIN
                    - MARGIN_MAIN
                    - MARGIN_UMFUTURE
                    - MARGIN_CMFUTURE
                    - ISOLATEDMARGIN_MARGIN
                    - MARGIN_ISOLATEDMARGIN
                    - ISOLATEDMARGIN_ISOLATEDMARGIN
                    - MAIN_FUNDING
                    - FUNDING_MAIN
                    - FUNDING_UMFUTURE
                    - UMFUTURE_FUNDING
                    - MARGIN_FUNDING
                    - FUNDING_MARGIN
                    - FUNDING_CMFUTURE
                    - CMFUTURE_FUNDING
                    - MAIN_OPTION
                    - OPTION_MAIN
                    - UMFUTURE_OPTION
                    - OPTION_UMFUTURE
                    - MARGIN_OPTION
                    - OPTION_MARGIN
                    - FUNDING_OPTION
                    - OPTION_FUNDING
                    - MAIN_PORTFOLIO_MARGIN
                    - PORTFOLIO_MARGIN_MAIN
                asset:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
                fromSymbol:
                  type: string
                  example: ISOLATEDMARGIN_MARGIN
                  enum:
                    - ISOLATEDMARGIN_MARGIN
                    - ISOLATEDMARGIN_ISOLATEDMARGIN
                toSymbol:
                  type: string
                  example: MARGIN_ISOLATEDMARGIN
                  enum:
                    - MARGIN_ISOLATEDMARGIN
                    - ISOLATEDMARGIN_ISOLATEDMARGIN
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
          description: User Universal Transfer
          x-description-cn: 用户万向划转
          content:
            application/json:
              schema:
                type: object
                properties:
                  tranId:
                    type: integer
                    example: 13526853623
                    format: int64
  /sapi/v1/asset/wallet/balance:
    get:
      summary: Query User Wallet Balance (USER_DATA)
      x-summary-cn: 查询用户钱包余额 (USER_DATA)
      description: Query User Wallet Balance
      x-description-cn: 查询用户钱包余额
      tags:
        - asset
      operationId: queryUserWalletBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#query-user-wallet-balance
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/queryUserWalletBalance.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/query_user_wallet_balance.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/query_user_wallet_balance.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/QueryUserWalletBalanceExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/QueryUserWalletBalance/QueryUserWalletBalance.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/QueryUserWalletBalanceExample.php
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
        - name: quoteAsset
          in: query
          required: false
          schema:
            type: string
            example: BTC
            default: BTC
        - name: needBalanceDetail
          in: query
          required: false
          schema:
            type: boolean
            example: false
            default: false
          description: |-
            Whether to return the per-asset balance detail for each wallet. When `false` or omitted, the response is
            unchanged from current behavior.
          x-description-cn: 是否返回每个钱包下各币种的持仓明细。为 `false` 或不传时，响应与现有行为完全一致。
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
          description: User Wallet Balance
          x-description-cn: 用户 Wallet Balance
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    activate:
                      type: boolean
                      example: true
                    balance:
                      type: string
                      example: "0"
                    walletName:
                      type: string
                      example: Spot
                    assetBalances:
                      type: array
                      description: |-
                        Per-asset balance detail for this wallet. Only present when `needBalanceDetail=true` is passed;
                        omitted entirely otherwise.
                      x-description-cn: 该钱包下各币种的持仓明细。仅当传入 `needBalanceDetail=true` 时才会返回，否则该字段完全不出现。
                      items:
                        type: object
                        properties:
                          asset:
                            type: string
                            example: USDT
                          assetName:
                            type: string
                            example: TetherUS
                          free:
                            type: string
                            example: "6.238383"
                          locked:
                            type: string
                            example: "0"
                          freeze:
                            type: string
                            example: "0"
                          withdrawing:
                            type: string
                            example: "0"
                          btcValuation:
                            type: string
                            example: "6.238383"
  /sapi/v1/bnbBurn:
    post:
      summary: Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
      x-summary-cn: 现货交易和杠杆利息BNB抵扣开关 (USER_DATA)
      description: Toggle BNB Burn On Spot Trade And Margin Interest
      x-description-cn: 现货交易和杠杆利息BNB抵扣开关
      tags:
        - asset
      operationId: toggleBnbBurnOnSpotTradeAndMarginInterest
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#toggle-bnb-burn-on-spot-trade-and-margin-interest
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/toggleBnbBurnOnSpotTradeAndMarginInterest.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/toggle_bnb_burn_on_spot_trade_and_margin_interest.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/toggle_bnb_burn_on_spot_trade_and_margin_interest.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/ToggleBnbBurnOnSpotTradeAndMarginInterestExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/ToggleBnbBurnOnSpotTradeAndMarginInterest/ToggleBnbBurnOnSpotTradeAndMarginInterest.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/ToggleBnbBurnOnSpotTradeAndMarginInterestExample.php
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
      x-parameters-notes: '- "spotBNBBurn" and "interestBNBBurn" should be sent at least one.'
      x-parameters-notes-cn: '- "spotBNBBurn" 和 "interestBNBBurn" 二者必须传至少一个'
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - timestamp
              properties:
                spotBNBBurn:
                  type: string
                  example: true
                  description: Determines whether to use BNB to pay for trading fees on SPOT
                  x-description-cn: 是否使用BNB支付现货交易的手续费
                interestBNBBurn:
                  type: string
                  example: true
                  description: Determines whether to use BNB to pay for margin loan's interest
                  x-description-cn: 是否使用BNB支付杠杆贷款的利息
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
          description: Toggle BNB Burn On Spot Trade And Margin Interest
          x-description-cn: 切换现货交易和杠杆利息 BNB 抵扣
          content:
            application/json:
              schema:
                type: object
                properties:
                  spotBNBBurn:
                    type: boolean
                    example: true
                  interestBNBBurn:
                    type: boolean
                    example: false
  /sapi/v1/asset/tradeFee:
    get:
      summary: Trade Fee (USER_DATA)
      x-summary-cn: 交易手续费率查询 (USER_DATA)
      description: Fetch trade fee
      x-description-cn: 交易手续费率查询
      tags:
        - asset
      operationId: tradeFee
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#trade-fee
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/tradeFee.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/trade_fee.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/trade_fee.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/TradeFeeExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/TradeFee/TradeFee.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/TradeFeeExample.php
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
            example: ADABNB
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
          description: Trade Fee
          x-description-cn: 交易手续费率
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      example: ADABNB
                    makerCommission:
                      type: string
                      example: "0.001"
                    takerCommission:
                      type: string
                      example: "0.001"
  /sapi/v3/asset/getUserAsset:
    post:
      summary: User Asset (USER_DATA)
      x-summary-cn: 用户持仓 (USER_DATA)
      description: Get user assets, just for positive data.
      x-description-cn: 获取用户持仓，仅返回>0的数据。
      tags:
        - asset
      operationId: userAsset
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/asset#user-asset
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/AssetApi/userAsset.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/asset_api/user_asset.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Asset/user_asset.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/asset/UserAssetExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/AssetAPI/UserAsset/UserAsset.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/asset/UserAssetExample.php
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
      x-parameters-notes: |-
        - If asset is set, then return this asset, otherwise return all assets positive.
        - If needBtcValuation is set, then return btcValudation.
      x-parameters-notes-cn: |-
        - If 资产 is set, then return this 资产, otherwise return all assets positive.
        - If need Btc Valuation is set, then return btc Valudation.
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - timestamp
              properties:
                asset:
                  type: string
                  example: BTC
                  description: If asset is blank, then query all positive assets user have.
                  x-description-cn: 如果资产为空，则查询用户所有的正资产。
                needBtcValuation:
                  type: boolean
                  example: true
                  description: Whether need btc valuation or not.
                  x-description-cn: 是否需要返回兑换成BTC的估值
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
          description: User Asset
          x-description-cn: 用户资产
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    asset:
                      type: string
                      example: AVAX
                    free:
                      type: string
                      example: "1"
                    locked:
                      type: string
                      example: "0"
                    freeze:
                      type: string
                      example: "0"
                    withdrawing:
                      type: string
                      example: "0"
                    ipoable:
                      type: string
                      example: "0"
                    btcValuation:
                      type: string
                      example: "0"
  /sapi/v1/capital/config/getall:
    get:
      summary: All Coins' Information (USER_DATA)
      x-summary-cn: 获取所有币信息 (USER_DATA)
      description: Get information of coins (available for deposit and withdraw) for user.
      x-description-cn: 获取针对用户的所有(Binance支持充提操作的)币种信息。
      tags:
        - capital
      operationId: allCoinsInformation
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#all-coins-information
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/allCoinsInformation.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/all_coins_information.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/all_coins_information.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/AllCoinsInformationExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/AllCoinsInformation/AllCoinsInformation.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/AllCoinsInformationExample.php
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
          description: All Coins' Information
          x-description-cn: 全部币种信息
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    coin:
                      type: string
                      example: 1MBABYDOGE
                    depositAllEnable:
                      type: boolean
                      example: true
                    withdrawAllEnable:
                      type: boolean
                      example: true
                    name:
                      type: string
                      example: 1M x BABYDOGE
                    free:
                      type: string
                      example: "34941.1"
                    locked:
                      type: string
                      example: "0"
                    freeze:
                      type: string
                      example: "0"
                    withdrawing:
                      type: string
                      example: "0"
                    ipoing:
                      type: string
                      example: "0"
                    ipoable:
                      type: string
                      example: "0"
                    storage:
                      type: string
                      example: "0"
                    isLegalMoney:
                      type: boolean
                      example: false
                    trading:
                      type: boolean
                      example: true
                    networkList:
                      type: array
                      items:
                        type: object
                        properties:
                          network:
                            type: string
                            example: BSC
                          coin:
                            type: string
                            example: 1MBABYDOGE
                          withdrawIntegerMultiple:
                            type: string
                            example: "0.01"
                          isDefault:
                            type: boolean
                            example: false
                          depositEnable:
                            type: boolean
                            example: true
                          withdrawEnable:
                            type: boolean
                            example: true
                          depositDesc:
                            type: string
                            example: ""
                            description: shown only when "depositEnable" is false.
                            x-description-cn: 仅在充值关闭时返回
                          withdrawDesc:
                            type: string
                            example: ""
                            description: shown only when "withdrawEnable" is false.
                            x-description-cn: 仅在提现关闭时返回
                          specialTips:
                            type: string
                            example: ""
                          specialWithdrawTips:
                            type: string
                            example: ""
                          name:
                            type: string
                            example: BNB Smart Chain (BEP20)
                          resetAddressStatus:
                            type: boolean
                            example: false
                          addressRegex:
                            type: string
                            example: ^(0x)[0-9A-Fa-f]{40}$
                          memoRegex:
                            type: string
                            example: ""
                          withdrawFee:
                            type: string
                            example: "10"
                          withdrawMin:
                            type: string
                            example: "20"
                          withdrawMax:
                            type: string
                            example: "9999999999"
                          withdrawInternalMin:
                            type: string
                            example: "0.01"
                            description: Minimum internal transfer amount
                            x-description-cn: 内部转账最小提现数
                          depositDust:
                            type: string
                            example: "0.01"
                          minConfirm:
                            type: integer
                            example: 5
                            format: int64
                            description: min number for balance confirmation
                            x-description-cn: 上账所需的最小确认数
                          unLockConfirm:
                            type: integer
                            example: 0
                            format: int64
                            description: confirmation number for balance unlock
                            x-description-cn: 解锁需要的确认数
                          sameAddress:
                            type: boolean
                            example: false
                            description: Obsoleted, recomment to use withdrawTag
                            x-description-cn: 过时字段，建议使用withdrawTag
                          withdrawTag:
                            type: boolean
                            example: false
                            description: If the coin needs to provide memo to withdraw
                            x-description-cn: 提现时是否需要memo
                          estimatedArrivalTime:
                            type: integer
                            example: 1
                            format: int64
                          busy:
                            type: boolean
                            example: false
                          contractAddressUrl:
                            type: string
                            example: https://bscscan.com/token/
                          contractAddress:
                            type: string
                            example: "0xc748673057861a797275cd8a068abb95a902e8de"
                          denomination:
                            type: integer
                            example: 1000000
                            format: int64
                            description: 1 1MBABYDOGE = 1000000 BABYDOGE
                            x-description-cn: 1 1MBABYDOGE = 1000000 BABYDOGE
  /sapi/v1/capital/deposit/address:
    get:
      summary: Deposit Address(supporting network) (USER_DATA)
      x-summary-cn: 获取充值地址(支持多网络) (USER_DATA)
      description: Fetch deposit address with network.
      x-description-cn: 获取充值地址
      tags:
        - capital
      operationId: depositAddress
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#deposit-address
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/depositAddress.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/deposit_address.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/deposit_address.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/DepositAddressExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/DepositAddress/DepositAddress.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/DepositAddressExample.php
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
        - name: coin
          in: query
          required: true
          schema:
            type: string
            example: BTC
          description: "`coin` refers to the parent network address format that the address is using"
          x-description-cn: 币种，指该地址所使用的主网络地址格式
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
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
      x-parameters-notes: >-
        - If `network` is not send, return with default network of the coin.

        - You can get `network` and `isDefault` in `networkList` in the response of `Get /sapi/v1/capital/config/getall
        (HMAC SHA256)`.

        - `amount` needs to be sent if using LIGHTNING network
      x-parameters-notes-cn: |-
        - If `network` is not send, return 带 默认network of the coin.
        - You can 获取 `network` 和 `is默认` in `network 列表` in the 响应 of `获取/sapi/v1/capital/config/getall (HMAC SHA256)`.
        - `数量` needs 到 be sent if using LIGHTNING network
      responses:
        "200":
          description: Deposit Address
          x-description-cn: 充值地址
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: string
                    example: 1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv
                  coin:
                    type: string
                    example: BTC
                  tag:
                    type: string
                    example: ""
                  url:
                    type: string
                    example: https://btc.com/1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv
  /sapi/v1/capital/deposit/hisrec:
    get:
      summary: Deposit History (supporting network) (USER_DATA)
      x-summary-cn: 获取充值历史 (USER_DATA)
      description: Fetch deposit history.
      x-description-cn: 获取充值历史(支持多网络)
      tags:
        - capital
      operationId: depositHistory
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#deposit-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/depositHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/deposit_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/deposit_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/DepositHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/DepositHistory/DepositHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/DepositHistoryExample.php
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
        - name: includeSource
          in: query
          required: false
          schema:
            type: boolean
            example: false
            default: false
          description: return `sourceAddress` field when set to `true`
          x-description-cn: 如果为`true`时会返回`sourceAddress`字段
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
            enum:
              - 0
              - 1
              - 2
              - 6
              - 7
              - 8
            format: int64
          description: >-
            0: pending, 1: success, 2: rejected, 6: credited but cannot withdraw, 7: Wrong Deposit, 8: Waiting User
            confirm
          x-description-cn: "0: 待确认, 1: 成功, 2: 已拒绝, 6: 已到账但不可提现, 7: 充值异常, 8: 等待用户确认"
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "Default: 90 days from current timestamp"
          x-description-cn: 默认当前时间90天前的时间戳
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "Default: present timestamp"
          x-description-cn: 默认当前时间戳
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: 0
            default: 0
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            default: 1000
            maximum: 1000
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
      x-parameters-notes: |-
        - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
        - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.
      x-parameters-notes-cn: |-
        - 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不超过90天.
        - 同时提交`startTime` 与 `endTime`间隔不得超过90天.
        - 请注意，由于网络特定的特性，返回的源地址可能不准确。 如果找到多个源地址，则仅返回第一个地址
      responses:
        "200":
          description: Deposit History
          x-description-cn: 充值历史
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
                      example: 1
                      format: int64
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
                    completeTime:
                      type: integer
                      example: 1661493146000
                      format: int64
                      description: represents deposit completion datetime, available for deposits after 6-Mar-2025.
                      x-description-cn: 代表充值完成时间，仅适用于2025年03月06日之后的充值。
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
                    travelRuleStatus:
                      type: integer
                      example: 0
                      format: int64
                      description: >-
                        0: travel rule not required OR info already provided and funds ready to use, 1: travel rule
                        required to provide deposit info
                      x-description-cn: >-
                        0: travel rule not required OR info already provided and funds ready to use, 1: travel rule
                        required to provide deposit info
  /sapi/v1/capital/deposit/address/list:
    get:
      summary: Fetch deposit address list with network (USER_DATA)
      x-summary-cn: 查询充值地址列表 (USER_DATA)
      description: Fetch deposit address list with network.
      x-description-cn: 根据网络币种或币种获取充值地址列表
      tags:
        - capital
      operationId: fetchDepositAddressListWithNetwork
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#fetch-deposit-address-list-with-network
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/fetchDepositAddressListWithNetwork.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/fetch_deposit_address_list_with_network.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/fetch_deposit_address_list_with_network.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/FetchDepositAddressListWithNetworkExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/FetchDepositAddressListWithNetwork/FetchDepositAddressListWithNetwork.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/FetchDepositAddressListWithNetworkExample.php
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
        - name: coin
          in: query
          required: true
          schema:
            type: string
            example: BTC
          description: Coin name
          x-description-cn: 币种名称
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
          description: >-
            If network is not send, return with default network of the coin. You can get network and isDefault in
            networkList in the response of `Get /sapi/v1/capital/config/getall`
          x-description-cn: 如果没传网络，会返回网络对应的默认网络。可以通过后面的接口，来获取网络和 isDefault 字段，在返回的响应里`Get /sapi/v1/capital/config/getall`
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
          description: Fetch deposit address list with network
          x-description-cn: 查询充值地址列表（按网络）
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    coin:
                      type: string
                      example: ETH
                      description: coin here means network address space, ETH for all EVM-like network
                      x-description-cn: 这里 coin 实际上指 network 的地址空间, 类 ETH 网络都使用 ETH 的地址
                    address:
                      type: string
                      example: "0xD316E95Fd9E8E237Cb11f8200Babbc5D8D177BA4"
                    tag:
                      type: string
                      example: ""
                    isDefault:
                      type: integer
                      example: 0
                      format: int64
                      description: "'isDefault' is 1 means the address is default, same as shown in the app."
                      x-description-cn: isDefault 为 1 表示该地址为默认地址，与 App 中显示的一致。
  /sapi/v1/capital/withdraw/address/list:
    get:
      summary: Fetch withdraw address list (USER_DATA)
      x-summary-cn: 查询提现地址簿 (USER_DATA)
      description: Fetch withdraw address list
      x-description-cn: 查询提现地址簿
      tags:
        - capital
      operationId: fetchWithdrawAddressList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#fetch-withdraw-address-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/fetchWithdrawAddressList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/fetch_withdraw_address_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/fetch_withdraw_address_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/FetchWithdrawAddressListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/FetchWithdrawAddressList/FetchWithdrawAddressList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/FetchWithdrawAddressListExample.php
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
          description: Fetch withdraw address list
          x-description-cn: 查询提现地址簿
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    address:
                      type: string
                      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
                    addressTag:
                      type: string
                      example: ""
                    coin:
                      type: string
                      example: BTC
                    name:
                      type: string
                      example: Satoshi
                      description: is a user-defined name
                      x-description-cn: 用户自定义
                    network:
                      type: string
                      example: BTC
                    origin:
                      type: string
                      example: bla
                      description: >-
                        if originType != 'others', this value is blank, otherwise the origin is manually filled in by
                        the user
                      x-description-cn: 如果 originType != 'others'，则该值为空，否则 origin 由用户手动填写
                    originType:
                      type: string
                      example: others
                      description: >-
                        Address source type, including but not limited to: type Exchange Address: Binance, CoinBase,
                        HTX, Bitfinex, OKX, Bithumb, Kraken, Kucoin, Gemini, Bitget, Bybit, Upbit, Gate.io;  type Wallet
                        Address: Binance Web3 Wallet, Trust Wallet, MetaMask, Rabby Wallet, Phantom, OKX Web 3 Wallet,
                        Coinbase Wallet, Bitget Wallet; type Others: others(multilanguage support)
                      x-description-cn: >-
                        地址来源类型，包括但不限于: 交易所地址类型: Binance, CoinBase, HTX, Bitfinex, OKX, Bithumb, Kraken, Kucoin, Gemini,
                        Bitget, Bybit, Upbit, Gate.io; 个人钱包类型: Binance Web3 Wallet, Trust Wallet, MetaMask, Rabby
                        Wallet, Phantom, OKX Web 3 Wallet, Coinbase Wallet, Bitget Wallet; 其他 Others 类型: others(支持多语言)
                    whiteStatus:
                      type: boolean
                      example: true
                      description: Is it whitelisted
                      x-description-cn: 是否是白名单
  /sapi/v1/capital/withdraw/quota:
    get:
      summary: Fetch withdraw quota (USER_DATA)
      x-summary-cn: 获取用户提现额度 (USER_DATA)
      description: Fetch withdraw quota
      x-description-cn: 获取用户提现额度
      tags:
        - capital
      operationId: fetchWithdrawQuota
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#fetch-withdraw-quota
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/fetchWithdrawQuota.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/fetch_withdraw_quota.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/fetch_withdraw_quota.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/FetchWithdrawQuotaExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/FetchWithdrawQuota/FetchWithdrawQuota.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/FetchWithdrawQuotaExample.php
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
          description: Fetch withdraw quota
          x-description-cn: 获取提现额度
          content:
            application/json:
              schema:
                type: object
                properties:
                  wdQuota:
                    type: string
                    example: "10000"
                    description: >-
                      User's total withdrawal quota in the past 24 hours (including on-chain withdrawal and internal
                      transfer), unit in USD
                    x-description-cn: 用户过去24小时的提币额度（包含链上提币和内部转账），单位为 USD
                  usedWdQuota:
                    type: string
                    example: "1000"
                    description: User withdrawal quota usage in the past 24 hours, unit in USD
                    x-description-cn: 用户过去24小时内已用提币额度，单位为 USD
  /sapi/v1/capital/deposit/credit-apply:
    post:
      summary: One click arrival deposit apply (for expired address deposit) (USER_DATA)
      x-summary-cn: 一键上账(充值到过期地址) (USER_DATA)
      description: Apply deposit credit for expired address (One click arrival)
      x-description-cn: 申请充值到过期地址的一键上账.
      tags:
        - capital
      operationId: oneClickArrivalDepositApply
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#one-click-arrival-deposit-apply
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/oneClickArrivalDepositApply.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/one_click_arrival_deposit_apply.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/one_click_arrival_deposit_apply.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/OneClickArrivalDepositApplyExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/OneClickArrivalDepositApply/OneClickArrivalDepositApply.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/OneClickArrivalDepositApplyExample.php
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
                - timestamp
              properties:
                depositId:
                  type: integer
                  example: 1
                  format: int64
                  description: Deposit record Id, priority use
                  x-description-cn: 充值记录Id，优先使用
                txId:
                  type: string
                  example: "1"
                  description: Deposit txId, used when depositId is not specified
                  x-description-cn: 充值txId，当depositId没指定时使用
                subAccountId:
                  type: string
                  example: "1"
                  description: Sub-accountId of Cloud user
                  x-description-cn: Cloud的子账户ID
                subUserId:
                  type: integer
                  example: 1
                  format: int64
                  description: Sub-userId of parent user
                  x-description-cn: 母账户的子账户userId
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
          description: One click arrival deposit apply
          x-description-cn: 一键充值到账申请
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                  message:
                    type: string
                    example: success
                  data:
                    type: boolean
                    example: true
                  success:
                    type: boolean
                    example: true
  /sapi/v1/capital/withdraw/apply:
    post:
      summary: Withdraw (USER_DATA)
      x-summary-cn: 提币 (USER_DATA)
      description: Submit a withdraw request
      x-description-cn: 提币
      tags:
        - capital
      operationId: withdraw
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#withdraw
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/withdraw.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/withdraw.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/withdraw.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/WithdrawExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/Withdraw/Withdraw.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/WithdrawExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 900
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - If `network` not send, return with default network of the coin.

        - You can get `network` and `isDefault` in `networkList` of a coin in the response of `Get
        /sapi/v1/capital/config/getall (HMAC SHA256)`.

        - To check if travel rule is required, by using `GET /sapi/v1/localentity/questionnaire-requirements` and if it
        returns anything other than `NIL` you will need update SAPI to `POST /sapi/v1/localentity/withdraw/apply` else
        you can continue `POST /sapi/v1/capital/withdraw/apply`. Please note that if you are required to comply to
        travel rule please refer to the Travel Rule SAPI.

        - "For networks that do not support memo/tag, submitting a withdrawal request with a non-empty `addressTag` will
        return error `-4106 TAG_NOT_SUPPORTED_FOR_NETWORK`. Please omit the `addressTag` field for such networks. You
        can check whether a network requires a tag via `GET /sapi/v1/capital/config/getall`: If `withdrawTag` = `true` →
        memo/tag is required. If `withdrawTag` = `false` → memo/tag is not supported; omit `addressTag`."
      x-parameters-notes-cn: >-
        - 如果`network`未发送，则返回该币种的默认网络。

        - 您可以在`Get /sapi/v1/capital/config/getall (HMAC SHA256)`的响应中，获取某个币种的`networkList`中的`network`和`isDefault`。

        - 要检查是否需要遵守旅行规则，可以使用接口 `GET /sapi/v1/localentity/questionnaire-requirements`，如果返回结果不是 NIL，则需要使用更新后的 SAPI 接口
        `POST /sapi/v1/localentity/withdraw/apply`；否则，可以继续使用 `POST
        /sapi/v1/capital/withdraw/apply`。请注意，如果需要遵守旅行规则，请参考旅行规则相关的 SAPI 文档。

        - 对于不支持 memo/tag 的网络，提交包含非空 `addressTag` 的提币请求将返回错误 `-4106 TAG_NOT_SUPPORTED_FOR_NETWORK`。请在此类网络中省略 `addressTag`
        字段。您可以通过 `GET /sapi/v1/capital/config/getall` 检查网络是否需要 tag：如果 `withdrawTag` = `true` → memo/tag 为必填。如果
        `withdrawTag` = `false` → 该网络不支持 memo/tag，请省略 `addressTag`。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - coin
                - address
                - amount
                - timestamp
              properties:
                coin:
                  type: string
                  example: BTC
                withdrawOrderId:
                  type: string
                  example: "1"
                  description: |-
                    client side id for withdrawal, if provide here, can be used in GET
                    `/sapi/v1/capital/withdraw/history` for query.
                  x-description-cn: 用户自定义提币ID, 后续可以在GET `/sapi/v1/capital/withdraw/history` 中使用这个字段进行查询
                network:
                  type: string
                  example: null
                  description: Withdrawal network
                  x-description-cn: 提币网络
                address:
                  type: string
                  example: null
                  description: Withdrawal address
                  x-description-cn: 提币地址
                addressTag:
                  type: string
                  example: null
                  description: Secondary address identifier for coins like XRP,XMR etc.
                  x-description-cn: 某些币种例如 XRP,XMR 允许填写次级地址标签
                amount:
                  type: number
                  example: "1.0"
                  format: float
                  description: Amount
                  x-description-cn: 数量
                transactionFeeFlag:
                  type: boolean
                  example: true
                  description: |-
                    When making internal transfer, `true` for returning the fee to the destination account; `false` for
                    returning the fee back to the departure account. Default `false`.
                  x-description-cn: "当站内转账时免手续费, `true`: 手续费归资金转入方; `false`: 手续费归资金转出方; . 默认 `false`."
                name:
                  type: string
                  example: null
                walletType:
                  type: integer
                  example: 0
                  format: int64
                  description: |-
                    The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current
                    "selected wallet" under wallet->Fiat and Spot/Funding->Deposit
                  x-description-cn: 表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。
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
          description: Withdraw
          x-description-cn: 提币
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: 7213fea8e94b4a5593d507237e5a555b
  /sapi/v1/capital/withdraw/history:
    get:
      summary: Withdraw History (supporting network) (USER_DATA)
      x-summary-cn: 获取提币历史(支持多网络) (USER_DATA)
      description: Fetch withdraw history
      x-description-cn: 获取提币历史 (支持多网络)
      tags:
        - capital
      operationId: withdrawHistory
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/capital#withdraw-history
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/CapitalApi/withdrawHistory.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/capital_api/withdraw_history.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Capital/withdraw_history.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/capital/WithdrawHistoryExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/CapitalAPI/WithdrawHistory/WithdrawHistory.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/capital/WithdrawHistoryExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 18000 (10 requests per second)
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: coin
          in: query
          required: false
          schema:
            type: string
            example: BTC
        - name: withdrawOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: |-
            client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for
            query.
          x-description-cn: 用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单
        - name: status
          in: query
          required: false
          schema:
            type: integer
            example: 0
            format: int64
          description: "0(0: Email Sent, 2: Awaiting Approval 3: Rejected 4: Processing 6: Completed)"
          x-description-cn: 0(0:已发送确认Email, 2:等待确认 3:被拒绝 4:处理中 6 提现完成)
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: 0
            format: int64
          description: "Default: 0"
          x-description-cn: 默认值：0
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            default: 1000
            maximum: 1000
            format: int64
        - name: idList
          in: query
          required: false
          schema:
            type: string
            example: null
          description: id list returned in the response of POST `/sapi/v1/capital/withdraw/apply`, separated by `,`
          x-description-cn: POST `/sapi/v1/capital/withdraw/apply` 返回的 id 列表，以 `,` 分隔
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "Default: 90 days from current timestamp"
          x-description-cn: 默认当前时间90天前的时间戳
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "Default: present timestamp"
          x-description-cn: 默认当前时间戳
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
        - `network` may not be in the response for old withdraw.

        - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.

        - If both `startTime` and `endTime`are sent, time between `startTime`and `endTime`must be less than 90 days.

        - If `withdrawOrderId` is sent, time between `startTime` and `endTime` must be less than 7 days.

        - If `withdrawOrderId` is sent, `startTime` and `endTime` are not sent, will return last 7 days records by
        default.

        - Maximum support `idList` number is 45.
      x-parameters-notes-cn: |-
        - 支持多网络提币前的历史记录可能不会返回`network`字段.
        - 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不得超过90天.
        - 同时提交`startTime` 与 `endTime`间隔不得超过90天.
        - 若传了`withdrawOrderId`，则请求的`startTime` 与 `endTime`的时间间隔不得超过7天.
        - 若传了`withdrawOrderId`，没传`startTime` 与 `endTime`，则默认返回最近7天数据.
        - 最大支持的`idList`是 45 个
      responses:
        "200":
          description: Withdraw History
          x-description-cn: 提币历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      example: b6ae22b3aa844210a7041aee7589627c
                      description: Withdrawal id in Binance
                      x-description-cn: 该笔提现在币安的id
                    amount:
                      type: string
                      example: "8.91000000"
                      description: withdrawal amount
                      x-description-cn: 提现转出金额
                    transactionFee:
                      type: string
                      example: "0.004"
                      description: transaction fee
                      x-description-cn: 手续费
                    coin:
                      type: string
                      example: USDT
                    status:
                      type: integer
                      example: 6
                      format: int64
                    address:
                      type: string
                      example: "0x94df8b352de7f46f64b01d3666bf6e936e44ce60"
                    txId:
                      type: string
                      example: "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268"
                      description: withdrawal transaction id
                      x-description-cn: 提现交易id
                    applyTime:
                      type: string
                      example: "2019-10-12 11:12:02"
                      description: UTC time
                      x-description-cn: UTC 时间
                    network:
                      type: string
                      example: ETH
                    transferType:
                      type: integer
                      example: 0
                      format: int64
                      description: 1 for internal transfer, 0 for external transfer
                      x-description-cn: "1: 站内转账, 0: 站外转账"
                    withdrawOrderId:
                      type: string
                      example: WITHDRAWtest123
                      description: will not be returned if there's no withdrawOrderId for this withdraw.
                      x-description-cn: 自定义ID, 如果没有则不返回该字段
                    info:
                      type: string
                      example: The address is not valid. Please confirm with the recipient
                      description: reason for withdrawal failure
                      x-description-cn: 提币失败原因
                    confirmNo:
                      type: integer
                      example: 3
                      format: int64
                      description: confirm times for withdraw
                      x-description-cn: 提现确认数
                    walletType:
                      type: integer
                      example: 1
                      format: int64
                      description: "1: Funding Wallet 0:Spot Wallet"
                      x-description-cn: "1: 资金钱包 0:现货钱包"
                    txKey:
                      type: string
                      example: ""
                    completeTime:
                      type: string
                      example: "2023-03-23 16:52:41"
                      description: complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)
                      x-description-cn: 提现完成，成功下账时间(UTC)，仅当 status = 6(成功) 时返回
  /sapi/v1/spot/delist-schedule:
    get:
      summary: Get Spot Delist Schedule (MARKET_DATA)
      x-summary-cn: 查询现货币对的下架计划 (MARKET_DATA)
      description: Get symbols delist schedule for spot
      x-description-cn: 查询现货币对的下架计划
      tags:
        - others
      operationId: getSymbolsDelistScheduleForSpot
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/others#get-symbols-delist-schedule-for-spot
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/OthersApi/getSymbolsDelistScheduleForSpot.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/others_api/get_symbols_delist_schedule_for_spot.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Others/get_symbols_delist_schedule_for_spot.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/others/GetSymbolsDelistScheduleForSpotExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/OthersAPI/GetSymbolsDelistScheduleForSpot/GetSymbolsDelistScheduleForSpot.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/others/GetSymbolsDelistScheduleForSpotExample.php
      x-ip-weight: 100
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
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
      responses:
        "200":
          description: Get symbols delist schedule for spot
          x-description-cn: 查询现货下架计划
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    delistTime:
                      type: integer
                      example: 1686161202000
                      format: int64
                    symbols:
                      type: array
                      items:
                        type: string
                        example: ADAUSDT
  /sapi/v1/system/status:
    get:
      summary: System Status
      x-summary-cn: 系统状态
      description: Fetch system status.
      x-description-cn: 获取系统状态。
      tags:
        - others
      operationId: systemStatus
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/others#system-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/OthersApi/systemStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/others_api/system_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/Others/system_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/others/SystemStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/OthersAPI/SystemStatus/SystemStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/others/SystemStatusExample.php
      x-ip-weight: 1
      x-security-type: System
      responses:
        "200":
          description: System Status
          x-description-cn: 系统状态
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    example: 0
                    format: int64
                    description: "0: normal，1：system maintenance"
                    x-description-cn: "0: normal，1：system maintenance"
                  msg:
                    type: string
                    example: normal
                    description: '"normal", "system_maintenance"'
                    x-description-cn: '"normal", "system_maintenance"'
  /sapi/v1/localentity/broker/withdraw/apply:
    post:
      summary: Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)
      x-summary-cn: Broker 提币（适用于需要旅行规则的本地实体券商） (USER_DATA)
      description: Submit a withdrawal request for brokers of local entities that required travel rule.
      x-description-cn: 为需要旅行规则的本地实体券商提交提币请求。
      tags:
        - travel-rule
      operationId: brokerWithdraw
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#broker-withdraw
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/brokerWithdraw.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/broker_withdraw.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/broker_withdraw.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/BrokerWithdrawExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/BrokerWithdraw/BrokerWithdraw.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/BrokerWithdrawExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 600
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - If `network` not send, return with default network of the coin, but if the address could not match default
        network, the withdraw will be rejected.

        - You can get `network` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC
        SHA256)`.

        - Questionnaire is different for each local entity, please refer to the `Withdraw Questionnaire Contents` page.

        - If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to
        verify the format of the questionnaire and use URL-encoded format.


        **StandardPii**


        **For Natural Person**


        - `piiType` (INTEGER, Mandatory): Fix to 0: Natural Person

        - `latinNames` (List&lt;PiiName&gt;, Mandatory): In case a person have complicated names or multiple names, this
        parameter is a list

        - `localNames` (List&lt;PiiName&gt;, Optional): In case a person have complicated names or multiple names, this
        parameter is a list

        - `nationality` (STRING, Optional)

        - `residenceCountry` (STRING, Mandatory)

        - `nationalIdentifier` (STRING, Optional)

        - `nationalIdentifierType` (STRING, Optional)

        - `nationalIdentifierIssueCountry` (STRING, Optional)

        - `dateOfBirth` (STRING, Optional): yyyy-mm-dd. Not required but strongly recommended. Providing DOB could
        greatly reduce false positive rate during risk checking process.

        - `placeOfBirth` (STRING, Optional)

        - `address` (STRING, Optional)


        **For Legal Person**


        - `piiType` (INTEGER, Mandatory): Fix to 1: Legal Person

        - `latinName` (STRING, Mandatory): It's company name for Legal Person

        - `localName` (STRING, Optional)

        - `registrationCountry` (STRING, Mandatory)

        - `nationalIdentifier` (STRING, Optional)

        - `nationalIdentifierType` (STRING, Optional)

        - `nationalIdentifierIssueCountry` (STRING, Optional)

        - `registrationDate` (STRING, Optional): yyyy-mm-dd. Not required but strongly recommended.

        - `address` (STRING, Optional)

        - `walletAddress` (STRING, Optional)

        - `walletTag` (STRING, Optional)


        **PiiName**


        - `firstName` (STRING, Mandatory): Mandatory for Natural person

        - `middleName` (STRING, Optional)

        - `lastName` (STRING, Optional)
      x-parameters-notes-cn: >-
        - 如果没有传入 `network`, 则使用对应币种的默认网络, 如果地址格式不能匹配默认网络, 提币将被拒绝。

        - 网络、默认网络的配置列表可以通过以下接口获取 `Get /sapi/v1/capital/config/getall (HMAC SHA256)`。

        - 每个本地站点的问卷内容都不一样，请参考`提币问卷内容`页。

        - 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误，请尝检查Questionnaire格式并使用
        `URL-encoded format`。


        **标准个人身份信息**


        **自然人**


        - `piiType` (INTEGER, 必填): 固定为0：自然人

        - `latinNames` (List&lt;PiiName&gt;, 必填): 如果一个人有复杂的姓名或多个名字，此参数为一个列表

        - `localNames` (List&lt;PiiName&gt;, 选填): 如果一个人有复杂的姓名或多个名字，此参数为一个列表

        - `nationality` (STRING, 选填)

        - `residenceCountry` (STRING, 必填)

        - `nationalIdentifier` (STRING, 选填)

        - `nationalIdentifierType` (STRING, 选填)

        - `nationalIdentifierIssueCountry` (STRING, 选填)

        - `dateOfBirth` (STRING, 选填): yyyy-mm-dd. 非必填，但强烈推荐. 提供出生日期可以大大降低风险审查过程中的误报率.

        - `placeOfBirth` (STRING, 选填)

        - `address` (STRING, 选填)


        **法人**


        - `piiType` (INTEGER, 必填): 固定为1：法人

        - `latinName` (STRING, 必填): 如果是法人，则为公司名称

        - `localName` (STRING, 选填)

        - `registrationCountry` (STRING, 必填)

        - `nationalIdentifier` (STRING, 选填)

        - `nationalIdentifierType` (STRING, 选填)

        - `nationalIdentifierIssueCountry` (STRING, 选填)

        - `registrationDate` (STRING, 选填): yyyy-mm-dd. 非必填，但强烈推荐.

        - `address` (STRING, 选填)

        - `walletAddress` (STRING, 选填)

        - `walletTag` (STRING, 选填)


        **个人身份信息姓名**


        - `firstName` (STRING, 必填): 自然人必填

        - `middleName` (STRING, 选填)

        - `lastName` (STRING, 选填)
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - address
                - coin
                - amount
                - withdrawOrderId
                - questionnaire
                - originatorPii
                - timestamp
              properties:
                address:
                  type: string
                  example: null
                addressTag:
                  type: string
                  example: null
                  description: Secondary address identifier for coins like XRP,XMR etc.
                  x-description-cn: 某些币种例如 XRP,XMR 允许填写次级地址标签
                network:
                  type: string
                  example: null
                coin:
                  type: string
                  example: BTC
                addressName:
                  type: string
                  example: null
                  description: Description of the address. Address book cap is 200, space in name should be encoded into `%20`
                  x-description-cn: 地址描述。地址簿上限为200，名称中的空格应编码为`%20`
                amount:
                  type: number
                  example: "1.0"
                  format: float
                withdrawOrderId:
                  type: string
                  example: "1"
                  description: withdrawID defined by the client (i.e. client's internal withdrawID)
                  x-description-cn: 客户端内部定义的提币ID.
                transactionFeeFlag:
                  type: boolean
                  example: true
                  description: |-
                    When making internal transfer, `true` for returning the fee to the destination account; `false` for
                    returning the fee back to the departure account. Default `false`.
                  x-description-cn: "当站内转账时免手续费,`true`: 手续费归资金转入方;`false`: 手续费归资金转出方; . 默认`false`."
                walletType:
                  type: integer
                  example: 0
                  format: int64
                  description: |-
                    The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current
                    "selected wallet" under wallet->Fiat and Spot/Funding->Deposit
                  x-description-cn: 表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。
                questionnaire:
                  type: string
                  example: null
                  description: JSON format questionnaire answers.
                  x-description-cn: JSON 格式的问卷回答。
                originatorPii:
                  type: string
                  example: null
                  description: JSON format originator Pii, see StandardPii section below
                  x-description-cn: JSON 格式的汇款人个人身份信息, 请参阅下面的标准个人身份信息部分。
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
          description: Broker Withdraw
          x-description-cn: Broker 提币
          content:
            application/json:
              schema:
                type: object
                properties:
                  trId:
                    type: integer
                    example: 123456
                    format: int64
                    description: The travel rule record Id
                    x-description-cn: Travel Rule记录ID
                  accepted:
                    type: boolean
                    example: true
                    description: Whether the withdraw request is accepted
                    x-description-cn: 提币请求是否被接受
                  info:
                    type: string
                    example: Withdraw request accepted
                    description: The detailed infomation of the withdrawal result.
                    x-description-cn: 提现结果的详细信息
  /sapi/v1/localentity/questionnaire-requirements:
    get:
      summary: Check Questionnaire Requirements (for local entities that require travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 检查问卷需求(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)
      description: |-
        This API will return user-specific Travel Rule questionnaire requirement information in reference to the current
        API key.
      x-description-cn: 基于当前的用户的API key，接口讲返回针对改用户提交问卷所需的信息。
      tags:
        - travel-rule
      operationId: checkQuestionnaireRequirements
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#check-questionnaire-requirements
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/checkQuestionnaireRequirements.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/check_questionnaire_requirements.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/check_questionnaire_requirements.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/CheckQuestionnaireRequirementsExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/CheckQuestionnaireRequirements/CheckQuestionnaireRequirements.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/CheckQuestionnaireRequirementsExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Check Questionnaire Requirements
          x-description-cn: 检查询卷要求
          content:
            application/json:
              schema:
                type: object
                properties:
                  questionnaireCountryCode:
                    type: string
                    example: AE
  /sapi/v1/localentity/country/list:
    get:
      summary: Get Country List (USER_DATA)
      x-summary-cn: 国家列表 (USER_DATA)
      description: Query the active country list for travel rule questionnaires. Currently supports AU and BR entities.
      x-description-cn: 查询旅行规则问卷使用的活跃国家列表。目前支持澳大利亚站和巴西站。
      tags:
        - travel-rule
      operationId: getCountryList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#get-country-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/getCountryList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/get_country_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/get_country_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/GetCountryListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/GetCountryList/GetCountryList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/GetCountryListExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Country list
          x-description-cn: 国家列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  countries:
                    type: array
                    items:
                      type: object
                      properties:
                        countryCode:
                          type: string
                          example: au
                          description: ISO 2-digit country code, lowercase.
                          x-description-cn: ISO 2位国家代码，小写。
                        countryName:
                          type: string
                          example: Australia
                          description: Country display name.
                          x-description-cn: 国家显示名称。
                        blockType:
                          type: string
                          example: supported
                          description: "`supported`, `limited`, or `blocked`."
                          x-description-cn: "`supported`、`limited` 或 `blocked`。"
                        depositAllowed:
                          type: boolean
                          example: true
                          description: Whether deposit is allowed for this country.
                          x-description-cn: 该国家是否允许充值。
                        withdrawalAllowed:
                          type: boolean
                          example: true
                          description: Whether withdrawal is allowed for this country.
                          x-description-cn: 该国家是否允许提现。
                        hasRegionRestrictions:
                          type: boolean
                          example: false
                          description: >-
                            Whether this country has region-level restrictions. Always `false` for the BR entity, which
                            does not collect region/city.
                          x-description-cn: 该国家是否存在地区级别的限制。巴西站不采集地区/城市，恒为 `false`。
                  lastUpdated:
                    type: integer
                    format: int64
                    example: 1716300000000
                    description: Last data update timestamp (epoch milliseconds); 0 if empty.
                    x-description-cn: 数据最后更新时间戳（毫秒级 epoch）；为空时返回 0。
  /sapi/v1/localentity/deposit/history:
    get:
      summary: Deposit History Travel Rule (for local entities that required travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 获取充值历史(针对需要旅行规则的本地站) (USER_DATA)
      description: Fetch deposit history for local entities that required travel rule.
      x-description-cn: 获取充值历史(针对需要旅行规则的本地站)(支持多网络)
      tags:
        - travel-rule
      operationId: depositHistoryTravelRule
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#deposit-history-travel-rule
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/depositHistoryTravelRule.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/deposit_history_travel_rule.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/deposit_history_travel_rule.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/DepositHistoryTravelRuleExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/DepositHistoryTravelRule/DepositHistoryTravelRule.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/DepositHistoryTravelRuleExample.php
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
        - name: trId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of travel rule record Ids.
          x-description-cn: 旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔
        - name: txId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of transaction Ids.
          x-description-cn: 链上TxId，支持多条查询，以半角逗号(,) 分隔
        - name: tranId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of wallet tran Ids.
          x-description-cn: 充值记录ID，支持多条查询，以半角逗号(,) 分隔
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
        - name: coin
          in: query
          required: false
          schema:
            type: string
            example: BTC
        - name: travelRuleStatus
          in: query
          required: false
          schema:
            type: integer
            example: 0
            format: int64
          description: "0: Completed,1: Pending,2: Failed"
          x-description-cn: 0:处理完成,1:处理中,2:请求被拒绝
        - name: pendingQuestionnaire
          in: query
          required: false
          schema:
            type: boolean
            example: true
          description: "true: Only return records that pending deposit questionnaire. false/not provided: return all records."
          x-description-cn: "true: 只返回需要回答充值问卷的记录，false/缺省:返回所有记录"
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "Default: 90 days from current timestamp"
          x-description-cn: 默认当前时间90天前的时间戳
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "Default: present timestamp"
          x-description-cn: 默认当前时间戳
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: null
            format: int64
          description: "Default: 0"
          x-description-cn: 默认:0
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            default: 1000
            maximum: 1000
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
      x-parameters-notes: >-
        - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.

        - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.

        - Please, note that due to network-specific characteristics, the returned source address may be inaccurate. If
        multiple source addresses are found, only the first one will be returned.
      x-parameters-notes-cn: |-
        - 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不超过90天。
        - 同时提交`startTime` 与 `endTime`间隔不得超过90天。
        - 请注意，由于网络特定的特性，返回的源地址可能不准确。 如果找到多个源地址，则仅返回第一个地址。
      responses:
        "200":
          description: Deposit History
          x-description-cn: 充值历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    trId:
                      type: integer
                      example: 123451123
                      format: int64
                    tranId:
                      type: integer
                      example: 17644346245865
                      format: int64
                    amount:
                      type: string
                      example: "0.001"
                    coin:
                      type: string
                      example: BNB
                    network:
                      type: string
                      example: BNB
                    depositStatus:
                      type: integer
                      example: 0
                      format: int64
                    travelRuleStatus:
                      type: integer
                      example: 1
                      format: int64
                    travelRuleStatusV2:
                      type: string
                      example: PENDING
                      description: >-
                        Overall travel rule verification status (GTR + sanctions screening combined). "PASSED":
                        verification complete, deposit released. "PENDING": verification in progress, deposit frozen.
                        "REJECTED": verification failed.
                      x-description-cn: '旅行规则整体验证状态（GTR + 制裁筛查）。 "PASSED": 验证完成，充值已释放。 "PENDING": 验证进行中，充值已冻结。 "REJECTED": 验证失败。'
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
                    completeTime:
                      type: integer
                      example: 1661493206000
                      format: int64
                      description: Timestamp when the deposit was fully completed/credited (epoch ms).
                      x-description-cn: 充值完成时间戳（毫秒）。
                    transferType:
                      type: integer
                      example: 0
                      format: int64
                    confirmTimes:
                      type: string
                      example: 1/1
                    requireQuestionnaire:
                      type: boolean
                      example: false
                      description: >-
                        true: This deposit require user to answer questionnaire to get it credited, false: This deposit
                        doesn't require user to answer questionnaire as it's already completed or information has been
                        verified
                      x-description-cn: "true: 该充值需要用户回答问卷才能入账, false: 该充值不需要用户回答问卷，已完成或信息已验证"
                    questionnaire:
                      type: string
                      example: '{"question1":"answer1","question2":"answer2"}'
  /sapi/v2/localentity/deposit/history:
    get:
      summary: Deposit History V2 (for local entities that required travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 获取充值历史V2(针对需要旅行规则的本地站) (USER_DATA)
      description: Fetch deposit history for local entities that with required travel rule information.
      x-description-cn: 获取充值历史(针对需要旅行规则的本地站)(支持多网络)
      tags:
        - travel-rule
      operationId: depositHistoryV2
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#deposit-history-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/depositHistoryV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/deposit_history_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/deposit_history_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/DepositHistoryV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/DepositHistoryV2/DepositHistoryV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/DepositHistoryV2Example.php
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
        - name: depositId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Comma(,) separated list of wallet tran Ids.
          x-description-cn: 入金记录ID，支持多条查询，以半角逗号(,) 分隔
        - name: txId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of transaction Ids.
          x-description-cn: 链上TxId，支持多条查询，以半角逗号(,) 分隔
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
        - name: coin
          in: query
          required: false
          schema:
            type: string
            example: BTC
        - name: retrieveQuestionnaire
          in: query
          required: false
          schema:
            type: boolean
            example: true
          description: "true: return `questionnaire` within response."
          x-description-cn: true:返回的记录中带有问卷内容，false/缺省.
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "Default: 90 days from current timestamp"
          x-description-cn: 默认当前时间90天前的时间戳
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "Default: present timestamp"
          x-description-cn: 默认当前时间戳
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: 0
            default: 0
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            default: 1000
            maximum: 1000
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
      x-parameters-notes: >-
        - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.

        - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.

        - Please, note that due to network-specific characteristics, the returned source address may be inaccurate. If
        multiple source addresses are found, only the first one will be returned.
      x-parameters-notes-cn: |-
        - 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不超过90天。
        - 同时提交`startTime` 与 `endTime`间隔不得超过90天。
        - 请注意，由于网络特定的特性，返回的源地址可能不准确。 如果找到多个源地址，则仅返回第一个地址。
      responses:
        "200":
          description: Deposit History V2
          x-description-cn: 充值历史 V2
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    depositId:
                      type: string
                      example: "4615328107052018945"
                    amount:
                      type: string
                      example: "0.01"
                    network:
                      type: string
                      example: AVAXC
                    coin:
                      type: string
                      example: AVAX
                    depositStatus:
                      type: integer
                      example: 1
                      format: int64
                    travelRuleReqStatus:
                      type: integer
                      example: 0
                      format: int64
                      description: 0:PASS,2:REJECTED,3:PENDING,-1:FAILED
                      x-description-cn: 0:PASS,2:REJECTED,3:PENDING,-1:FAILED
                    address:
                      type: string
                      example: "0x0010627ab66d69232f4080d54e0f838b4dc3894a"
                    addressTag:
                      type: string
                      example: ""
                    txId:
                      type: string
                      example: "0xdde578983015741eed764e7ca10defb5a2caafdca3db5f92872d24a96beb1879"
                    transferType:
                      type: integer
                      example: 0
                      format: int64
                    confirmTimes:
                      type: string
                      example: 12/12
                    requireQuestionnaire:
                      type: boolean
                      example: false
                      description: >-
                        true: This deposit require user to answer questionnaire to get it credited, false: This deposit
                        doesn't require user to answer questionnaire as it's already completed or information has been
                        verified
                      x-description-cn: >-
                        true: This deposit require user to answer questionnaire to get it credited, false: This deposit
                        doesn't require user to answer questionnaire as it's already completed or information has been
                        verified
                    questionnaire:
                      type: object
                      properties:
                        vaspName:
                          type: string
                          example: BINANCE
                        depositOriginator:
                          type: integer
                          example: 0
                          format: int64
                    insertTime:
                      type: integer
                      example: 1753053392000
                      format: int64
  /sapi/v1/addressVerify/list:
    get:
      summary: Fetch address verification list (USER_DATA)
      x-summary-cn: 获取address verification 列表 (USER_DATA)
      description: |-
        Fetch address verification list for user to check on status and other details for the addresses stored in
        Address Book.
      x-description-cn: 获取地址验证列表，以便用户检查地址簿中存储的地址的状态和其他详细信息。
      tags:
        - travel-rule
      operationId: fetchAddressVerificationList
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#fetch-address-verification-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/fetchAddressVerificationList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/fetch_address_verification_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/fetch_address_verification_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/FetchAddressVerificationListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/FetchAddressVerificationList/FetchAddressVerificationList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/FetchAddressVerificationListExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Fetch address verification list
          x-description-cn: 获取地址验证列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    status:
                      type: string
                      example: PENDING
                    token:
                      type: string
                      example: AVAX
                    network:
                      type: string
                      example: AVAXC
                    walletAddress:
                      type: string
                      example: "0xc03a6aa728a8dde7464c33828424ede7553a0021"
                    addressQuestionnaire:
                      type: object
                      properties:
                        sendTo:
                          type: integer
                          example: 1
                          format: int64
                        satoshiToken:
                          type: string
                          example: AVAX
                        isAddressOwner:
                          type: integer
                          example: 1
                          format: int64
                        verifyMethod:
                          type: integer
                          example: 1
                          format: int64
  /sapi/v1/localentity/region/list:
    get:
      summary: Get Region List (USER_DATA)
      x-summary-cn: 地区列表 (USER_DATA)
      description: Query the active region/city list for a given country. Currently, only supports AU entity.
      x-description-cn: 查询指定国家下的活跃地区/城市列表。目前仅支持澳大利亚站。
      tags:
        - travel-rule
      operationId: getRegionList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#get-region-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/getRegionList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/get_region_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/get_region_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/GetRegionListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/GetRegionList/GetRegionList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/GetRegionListExample.php
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
        - name: countryCode
          in: query
          required: true
          schema:
            type: string
            example: au
          description: ISO 2-digit country code (from Country List API).
          x-description-cn: ISO 2位国家代码（来自国家列表接口）。
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
          description: Region list
          x-description-cn: 地区列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  countryCode:
                    type: string
                    example: au
                    description: Echoed country code (lowercase).
                    x-description-cn: 回显查询的国家代码（小写）。
                  regions:
                    type: array
                    items:
                      type: object
                      properties:
                        regionName:
                          type: string
                          example: New South Wales
                          description: Region/city display name (use this value in questionnaire answers).
                          x-description-cn: 地区/城市显示名称（问卷答案中使用此值）。
                        blockType:
                          type: string
                          example: supported
                          description: "`supported`, `limited`, or `blocked`."
                          x-description-cn: "`supported`、`limited` 或 `blocked`。"
                        depositAllowed:
                          type: boolean
                          example: true
                          description: Whether deposit is allowed for this region.
                          x-description-cn: 该地区是否允许充值。
                        withdrawalAllowed:
                          type: boolean
                          example: true
                          description: Whether withdrawal is allowed for this region.
                          x-description-cn: 该地区是否允许提现。
                  lastUpdated:
                    type: integer
                    format: int64
                    example: 1716300000000
                    description: Last data update timestamp (epoch milliseconds); 0 if empty.
                    x-description-cn: 数据最后更新时间戳（毫秒级 epoch）；为空时返回 0。
  /sapi/v1/localentity/broker/deposit/provide-info:
    put:
      summary: >-
        Submit Deposit Questionnaire Broker (For local entities that require travel rule) (supporting network)
        (USER_DATA)
      x-summary-cn: 提交充值问卷（Broker，适用于需要旅行规则的本地实体，支持网络） (USER_DATA)
      description: |-
        Submit questionnaire for brokers of local entities that require travel rule.
        The questionnaire is only applies to transactions from un-hosted wallets or VASPs that are not
        yet onboarded with GTR.
      x-description-cn: |-
        为需要旅行规则的本地实体券商提交问卷。
        该问卷仅适用于来自非托管钱包或尚未接入 GTR 的 VASP 的交易。
      tags:
        - travel-rule
      operationId: submitDepositQuestionnaire
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#submit-deposit-questionnaire
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/submitDepositQuestionnaire.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/submit_deposit_questionnaire.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/submit_deposit_questionnaire.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/SubmitDepositQuestionnaireExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/SubmitDepositQuestionnaire/SubmitDepositQuestionnaire.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/SubmitDepositQuestionnaireExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 600
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.

        - If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to
        verify the format of the questionnaire and use URL-encoded format.


        **StandardPii**


        **For Natural Person**


        - `piiType` (INTEGER, Mandatory): Fix to 0: Natural Person

        - `latinNames` (List&lt;PiiName&gt;, Mandatory): In case a person have complicated names or multiple names, this
        parameter is a list

        - `localNames` (List&lt;PiiName&gt;, Optional): In case a person have complicated names or multiple names, this
        parameter is a list

        - `nationality` (STRING, Optional)

        - `residenceCountry` (STRING, Mandatory)

        - `nationalIdentifier` (STRING, Optional)

        - `nationalIdentifierType` (STRING, Optional)

        - `nationalIdentifierIssueCountry` (STRING, Optional)

        - `dateOfBirth` (STRING, Optional): yyyy-mm-dd. Not required but strongly recommended. Providing DOB could
        greatly reduce false positive rate during risk checking process.

        - `placeOfBirth` (STRING, Optional)

        - `address` (STRING, Optional)


        **For Legal Person**


        - `piiType` (INTEGER, Mandatory): Fix to 1: Legal Person

        - `latinName` (STRING, Mandatory): It's company name for Legal Person

        - `localName` (STRING, Optional)

        - `registrationCountry` (STRING, Mandatory)

        - `nationalIdentifier` (STRING, Optional)

        - `nationalIdentifierType` (STRING, Optional)

        - `nationalIdentifierIssueCountry` (STRING, Optional)

        - `registrationDate` (STRING, Optional): yyyy-mm-dd. Not required but strongly recommended.

        - `address` (STRING, Optional)

        - `walletAddress` (STRING, Optional)

        - `walletTag` (STRING, Optional)


        **PiiName**


        - `firstName` (STRING, Mandatory): Mandatory for Natural person

        - `middleName` (STRING, Optional)

        - `lastName` (STRING, Optional)
      x-parameters-notes-cn: >-
        - 每个本地站点的问卷内容都不一样,请参考`充值问卷内容`页。

        - 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误,请尝检查Questionnaire格式并使用
        `URL-encoded format`。


        **标准个人身份信息**


        **自然人**


        - `piiType` (INTEGER, 必填): 固定为0：自然人

        - `latinNames` (List&lt;PiiName&gt;, 必填): 如果一个人有复杂的姓名或多个名字，此参数为一个列表

        - `localNames` (List&lt;PiiName&gt;, 选填): 如果一个人有复杂的姓名或多个名字，此参数为一个列表

        - `nationality` (STRING, 选填)

        - `residenceCountry` (STRING, 必填)

        - `nationalIdentifier` (STRING, 选填)

        - `nationalIdentifierType` (STRING, 选填)

        - `nationalIdentifierIssueCountry` (STRING, 选填)

        - `dateOfBirth` (STRING, 选填): yyyy-mm-dd. 非必填，但强烈推荐. 提供出生日期可以大大降低风险审查过程中的误报率.

        - `placeOfBirth` (STRING, 选填)

        - `address` (STRING, 选填)


        **法人**


        - `piiType` (INTEGER, 必填): 固定为1：法人

        - `latinName` (STRING, 必填): 如果是法人，则为公司名称

        - `localName` (STRING, 选填)

        - `registrationCountry` (STRING, 必填)

        - `nationalIdentifier` (STRING, 选填)

        - `nationalIdentifierType` (STRING, 选填)

        - `nationalIdentifierIssueCountry` (STRING, 选填)

        - `registrationDate` (STRING, 选填): yyyy-mm-dd. 非必填，但强烈推荐.

        - `address` (STRING, 选填)

        - `walletAddress` (STRING, 选填)

        - `walletTag` (STRING, 选填)


        **个人身份信息姓名**


        - `firstName` (STRING, 必填): 自然人必填

        - `middleName` (STRING, 选填)

        - `lastName` (STRING, 选填)
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - subAccountId
                - depositId
                - questionnaire
                - beneficiaryPii
                - timestamp
              properties:
                subAccountId:
                  type: string
                  example: "1"
                  description: External user ID.
                  x-description-cn: 外部UID
                depositId:
                  type: integer
                  example: 1
                  format: int64
                  description: Wallet deposit ID.
                  x-description-cn: 充值记录ID.
                questionnaire:
                  type: string
                  example: null
                  description: JSON format questionnaire answers.
                  x-description-cn: JSON 格式的问卷回答。
                beneficiaryPii:
                  type: string
                  example: null
                  description: JSON format beneficiary Pii, see StandardPii section below
                  x-description-cn: JSON 格式的收款人个人身份信息, 请参阅下面的标准个人身份信息部分。
                network:
                  type: string
                  example: null
                coin:
                  type: string
                  example: BTC
                amount:
                  type: number
                  example: "1.0"
                  format: float
                address:
                  type: string
                  example: null
                addressTag:
                  type: string
                  example: null
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
          description: Submit Deposit Questionnaire
          x-description-cn: 提交充值问卷
          content:
            application/json:
              schema:
                type: object
                properties:
                  trId:
                    type: integer
                    example: 765127651
                    format: int64
                  accepted:
                    type: boolean
                    example: true
                  info:
                    type: string
                    example: Deposit questionnaire accepted.
  /sapi/v1/localentity/deposit/provide-info:
    put:
      summary: Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 提交充值问卷(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)
      description: |-
        Submit questionnaire for local entities that require travel rule.
        The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not
        yet onboarded with GTR.
      x-description-cn: |-
        提交充值问卷(针对需要旅行规则的本地站)。
        只有来自私有钱包或尚未接入GTR的交易所的充值交易才需要提交充值问卷。
      tags:
        - travel-rule
      operationId: submitDepositQuestionnaireTravelRule
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#submit-deposit-questionnaire-travel-rule
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/submitDepositQuestionnaireTravelRule.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/submit_deposit_questionnaire_travel_rule.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/submit_deposit_questionnaire_travel_rule.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/SubmitDepositQuestionnaireTravelRuleExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/SubmitDepositQuestionnaireTravelRule/SubmitDepositQuestionnaireTravelRule.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/SubmitDepositQuestionnaireTravelRuleExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 600
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.

        - If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to
        verify the format of the questionnaire and use URL-encoded format.
      x-parameters-notes-cn: >-
        - 每个本地站点的问卷内容都不一样，请参考`充值问卷内容`页。

        - 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误，请尝检查Questionnaire格式并使用
        `URL-encoded format`。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - tranId
                - questionnaire
                - timestamp
              properties:
                tranId:
                  type: integer
                  example: 1
                  format: int64
                  description: Wallet tran ID
                  x-description-cn: 充值记录ID
                questionnaire:
                  type: string
                  example: null
                  description: JSON format questionnaire answers.
                  x-description-cn: JSON 格式问卷内容
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
          description: Submit Deposit Questionnaire
          x-description-cn: 提交充值问卷
          content:
            application/json:
              schema:
                type: object
                properties:
                  trId:
                    type: integer
                    example: 765127651
                    format: int64
                  accepted:
                    type: boolean
                    example: true
                  info:
                    type: string
                    example: Deposit questionnaire accepted.
  /sapi/v2/localentity/deposit/provide-info:
    put:
      summary: Submit Deposit Questionnaire V2 (For local entities that require travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 提交充值问卷V2(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)
      description: |-
        Submit questionnaire for local entities that require travel rule.
        The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not
        yet onboarded with GTR.
      x-description-cn: |-
        提交充值问卷(针对需要旅行规则的本地站)。
        只有来自私有钱包或尚未接入GTR的交易所的充值交易才需要提交充值问卷。
      tags:
        - travel-rule
      operationId: submitDepositQuestionnaireV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#submit-deposit-questionnaire-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/submitDepositQuestionnaireV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/submit_deposit_questionnaire_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/submit_deposit_questionnaire_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/SubmitDepositQuestionnaireV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/SubmitDepositQuestionnaireV2/SubmitDepositQuestionnaireV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/SubmitDepositQuestionnaireV2Example.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 600
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.

        - If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to
        verify the format of the questionnaire and use URL-encoded format.
      x-parameters-notes-cn: >-
        - 每个本地站点的问卷内容都不一样,请参考`充值问卷内容`页。

        - 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误,请尝检查Questionnaire格式并使用
        `URL-encoded format`。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - depositId
                - questionnaire
                - timestamp
              properties:
                depositId:
                  type: integer
                  example: 1
                  format: int64
                  description: Wallet deposit ID
                  x-description-cn: 充值记录ID
                questionnaire:
                  type: string
                  example: null
                  description: JSON format questionnaire answers.
                  x-description-cn: JSON 格式问卷内容
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
          description: Submit Deposit Questionnaire V2
          x-description-cn: 提交充值问卷 V2
          content:
            application/json:
              schema:
                type: object
                properties:
                  trId:
                    type: integer
                    example: 765127651
                    format: int64
                  accepted:
                    type: boolean
                    example: true
                  info:
                    type: string
                    example: Deposit questionnaire accepted.
  /sapi/v1/localentity/vasp:
    get:
      summary: VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 获取VASP列表(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)
      description: Fetch the VASP list for local entities.
      x-description-cn: 获取旅行规则的本地站的VASP列表。
      tags:
        - travel-rule
      operationId: vaspList
      externalDocs:
        url: https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#vasp-list
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/vaspList.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/vasp_list.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/vasp_list.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/VaspListExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/VaspList/VaspList.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/VaspListExample.php
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
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: VASP list
          x-description-cn: VASP 列表
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    vaspName:
                      type: string
                      example: Binance
                    vaspCode:
                      type: string
                      example: BINANCE
                    identifier:
                      type: string
                      example: xxx
                      description: For populating the `vasp` field in the deposit/withdrawal questionnaire
                      x-description-cn: 用于填写充值/提现问卷中的 `vasp` 字段
  /sapi/v1/localentity/withdraw/history:
    get:
      summary: Withdraw History Travel Rule (supporting network) (USER_DATA)
      x-summary-cn: 获取提币历史(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)
      description: Fetch withdraw history for local entities that required travel rule.
      x-description-cn: 获取需要旅行规则的本地站的提币历史记录
      tags:
        - travel-rule
      operationId: withdrawHistoryV1
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#withdraw-history-v1
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/withdrawHistoryV1.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/withdraw_history_v1.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/withdraw_history_v1.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/WithdrawHistoryV1Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/WithdrawHistoryV1/WithdrawHistoryV1.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/WithdrawHistoryV1Example.php
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
        - name: trId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of travel rule record Ids.
          x-description-cn: 旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔
        - name: txId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of transaction Ids.
          x-description-cn: 链上TxId，支持多条查询，以半角逗号(,) 分隔.
        - name: withdrawOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: |-
            client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for
            query.
          x-description-cn: 用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
        - name: coin
          in: query
          required: false
          schema:
            type: string
            example: BTC
        - name: travelRuleStatus
          in: query
          required: false
          schema:
            type: integer
            example: 0
            format: int64
          description: "0: Completed,1: Pending,2: Failed"
          x-description-cn: 0:处理完成,1:处理中,2:请求被拒绝
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: 0
            default: 0
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            default: 1000
            maximum: 1000
            format: int64
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "Default: 90 days from current timestamp"
          x-description-cn: 默认当前时间90天前的时间戳
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "Default: present timestamp"
          x-description-cn: 默认当前时间戳
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
        - `network` may not be in the response for old withdraw.
        - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
        - If both `startTime` and `endTime`are sent, time between `startTime`and `endTime`must be less than 90 days.
      x-parameters-notes-cn: |-
        - 支持多网络提币前的历史记录可能不会返回`network`字段。
        - 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不得超过90天。
        - 同时提交`startTime` 与 `endTime`间隔不得超过90天。
      responses:
        "200":
          description: Withdraw History
          x-description-cn: 提币历史
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      example: b6ae22b3aa844210a7041aee7589627c
                      description: Withdrawal id in Binance
                      x-description-cn: 该笔提现在币安的id, 只在sAPI提现的记录中返回
                    trId:
                      type: integer
                      example: 1234456
                      format: int64
                      description: Travel rule record id
                      x-description-cn: 旅行规则记录Id
                    amount:
                      type: string
                      example: "8.91000000"
                      description: withdrawal amount
                      x-description-cn: 提现转出金额
                    transactionFee:
                      type: string
                      example: "0.004"
                      description: only available for sAPI requests
                      x-description-cn: 手续费, 只在sAPI提现的记录中返回
                    coin:
                      type: string
                      example: USDT
                    withdrawalStatus:
                      type: integer
                      example: 6
                      format: int64
                      description: Capital withdrawal status, only available for sAPI requests
                      x-description-cn: 提币状态, 只在sAPI提现的记录中返回
                    travelRuleStatus:
                      type: integer
                      example: 0
                      format: int64
                      description: Travel rule status.
                      x-description-cn: 旅行规则处理状态，处理完成(0)之后才会继续提币流程
                    address:
                      type: string
                      example: "0x94df8b352de7f46f64b01d3666bf6e936e44ce60"
                    txId:
                      type: string
                      example: "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268"
                      description: withdrawal transaction id
                      x-description-cn: 提现交易id
                    applyTime:
                      type: string
                      example: "2019-10-12 11:12:02"
                      description: UTC time
                      x-description-cn: UTC 时间
                    network:
                      type: string
                      example: ETH
                    transferType:
                      type: integer
                      example: 0
                      format: int64
                      description: 1 for internal transfer, 0 for external transfer, only available for sAPI requests
                      x-description-cn: "1: 站内转账, 0: 站外转账, 只在sAPI提现的记录中返回"
                    withdrawOrderId:
                      type: string
                      example: WITHDRAWtest123
                      description: >-
                        will not be returned if there's no withdrawOrderId for this withdraw, only available for sAPI
                        requests
                      x-description-cn: 自定义ID, 如果没有则不返回该字段, 只在sAPI提现的记录中返回
                    info:
                      type: string
                      example: The address is not valid. Please confirm with the recipient
                      description: reason for withdrawal failure, only available for sAPI requests
                      x-description-cn: 提币失败原因, 只在sAPI提现的记录中返回
                    confirmNo:
                      type: integer
                      example: 3
                      format: int64
                      description: confirm times for withdraw, only available for sAPI requests
                      x-description-cn: 提现确认数, 只在sAPI提现的记录中返回
                    walletType:
                      type: integer
                      example: 1
                      format: int64
                      description: "1: Funding Wallet 0:Spot Wallet, only available for sAPI requests"
                      x-description-cn: "1: 资金钱包 0:现货钱包, 只在sAPI提现的记录中返回"
                    txKey:
                      type: string
                      example: ""
                      description: only available for sAPI requests
                      x-description-cn: 只在sAPI提现的记录中返回
                    questionnaire:
                      type: string
                      example: '{"question1":"answer1","question2":"answer2"}'
                      description: The answers of the questionnaire
                      x-description-cn: 问卷回答
                    completeTime:
                      type: string
                      example: "2023-03-23 16:52:41"
                      description: complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)
                      x-description-cn: 提现完成，成功下账时间(UTC)，仅当 status = 6(成功) 时返回
  /sapi/v2/localentity/withdraw/history:
    get:
      summary: Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)
      x-summary-cn: 获取提币历史V2(针对需要旅行规则的本地站)(支持多网络) (USER_DATA)
      description: Fetch withdraw history for local entities that required travel rule.
      x-description-cn: 获取需要旅行规则的本地站的提币历史记录
      tags:
        - travel-rule
      operationId: withdrawHistoryV2
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#withdraw-history-v2
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/withdrawHistoryV2.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/withdraw_history_v2.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/withdraw_history_v2.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/WithdrawHistoryV2Example.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/WithdrawHistoryV2/WithdrawHistoryV2.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/WithdrawHistoryV2Example.php
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
        - name: trId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of travel rule record Ids.
          x-description-cn: 旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔
        - name: txId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: Comma(,) separated list of transaction Ids.
          x-description-cn: 链上TxId，支持多条查询，以半角逗号(,) 分隔.
        - name: withdrawOrderId
          in: query
          required: false
          schema:
            type: string
            example: "1"
          description: |-
            client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for
            query.
          x-description-cn: 用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单
        - name: network
          in: query
          required: false
          schema:
            type: string
            example: null
        - name: coin
          in: query
          required: false
          schema:
            type: string
            example: null
        - name: travelRuleStatus
          in: query
          required: false
          schema:
            type: integer
            example: 0
            format: int64
          description: "0: Completed,1: Pending,2: Failed"
          x-description-cn: 0:处理完成,1:处理中,2:请求被拒绝
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            example: 0
            default: 0
            format: int64
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            example: 1000
            default: 1000
            maximum: 1000
            format: int64
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: "Default: 90 days from current timestamp"
          x-description-cn: 默认当前时间90天前的时间戳
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: "Default: present timestamp"
          x-description-cn: 默认当前时间戳
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
        - `network` may not be in the response for old withdraw.
        - Withdrawal made through /sapi/v1/capital/withdraw/apply may not be in the response.
        - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
        - If both `startTime` and `endTime`are sent, time between `startTime`and `endTime`must be less than 90 days.
        - If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
        - If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.
        - Maximum support trId,txId number is 45.
        - WithdrawOrderId only support 1.
        - If responsible does not include withdrawalStatus, please input trId or txId retrieve the data.
      x-parameters-notes-cn: |-
        - 支持多网络提币前的历史记录可能不会返回`network`字段。
        - 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不得超过90天。
        - 同时提交`startTime` 与 `endTime`间隔不得超过90天。
        - 通过API：/sapi/v1/capital/withdraw/apply 提交的提币记录，可能通过该API无法获取内容。
        - 如果通过`withdrawOrderId`查询`startTime`和`endTime`的默认时间间隔为7天.
        - 如果通过`withdrawOrderId`查询`startTime`和`endTime`间隔不得超过7天.
        - 如果通过`trId`,`txId`查询，最大支持的ID数量是45.
        - 如果通过`WithdrawOrderId` 查询，ID最多只支持一个.
        - 如果返回结果中不包含`withdrawalStatus`等信息, 请传入`trId`或者`txId`来查询数据.
      responses:
        "200":
          description: Withdraw History V2
          x-description-cn: 提币历史 V2
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      example: b6ae22b3aa844210a7041aee7589627c
                      description: Withdrawal id in Binance
                      x-description-cn: 该笔提现在币安的id, 只在sAPI提现的记录中返回
                    trId:
                      type: integer
                      example: 1234456
                      format: int64
                      description: Travel rule record id
                      x-description-cn: 旅行规则记录Id
                    amount:
                      type: string
                      example: "8.91000000"
                      description: withdrawal amount
                      x-description-cn: 提现转出金额
                    transactionFee:
                      type: string
                      example: "0.004"
                      description: only available for sAPI requests
                      x-description-cn: 手续费, 只在sAPI提现的记录中返回
                    coin:
                      type: string
                      example: USDT
                    withdrawalStatus:
                      type: integer
                      example: 6
                      format: int64
                      description: Capital withdrawal status, only available for sAPI requests
                      x-description-cn: 提币状态, 只在sAPI提现的记录中返回
                    travelRuleStatus:
                      type: integer
                      example: 0
                      format: int64
                      description: Travel rule status.
                      x-description-cn: 旅行规则处理状态，处理完成(0)之后才会继续提币流程
                    address:
                      type: string
                      example: "0x94df8b352de7f46f64b01d3666bf6e936e44ce60"
                    txId:
                      type: string
                      example: "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268"
                      description: withdrawal transaction id
                      x-description-cn: 提现交易id
                    applyTime:
                      type: string
                      example: "2019-10-12 11:12:02"
                      description: UTC time
                      x-description-cn: UTC 时间
                    network:
                      type: string
                      example: ETH
                    transferType:
                      type: integer
                      example: 0
                      format: int64
                      description: 1 for internal transfer, 0 for external transfer, only available for sAPI requests
                      x-description-cn: "1: 站内转账, 0: 站外转账, 只在sAPI提现的记录中返回"
                    withdrawOrderId:
                      type: string
                      example: WITHDRAWtest123
                      description: >-
                        will not be returned if there's no withdrawOrderId for this withdraw, only available for sAPI
                        requests
                      x-description-cn: 自定义ID, 如果没有则不返回该字段, 只在sAPI提现的记录中返回
                    info:
                      type: string
                      example: The address is not valid. Please confirm with the recipient
                      description: reason for withdrawal failure, only available for sAPI requests
                      x-description-cn: 提币失败原因, 只在sAPI提现的记录中返回
                    confirmNo:
                      type: integer
                      example: 3
                      format: int64
                      description: confirm times for withdraw, only available for sAPI requests
                      x-description-cn: 提现确认数, 只在sAPI提现的记录中返回
                    walletType:
                      type: integer
                      example: 1
                      format: int64
                      description: "1: Funding Wallet 0:Spot Wallet, only available for sAPI requests"
                      x-description-cn: "1: 资金钱包 0:现货钱包, 只在sAPI提现的记录中返回"
                    txKey:
                      type: string
                      example: ""
                      description: only available for sAPI requests
                      x-description-cn: 只在sAPI提现的记录中返回
                    questionnaire:
                      type: string
                      example: '{"question1":"answer1","question2":"answer2"}'
                      description: The answers of the questionnaire
                      x-description-cn: 问卷回答
                    completeTime:
                      type: string
                      example: "2023-03-23 16:52:41"
                      description: complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)
                      x-description-cn: 提现完成，成功下账时间(UTC)，仅当 status = 6(成功) 时返回
  /sapi/v1/localentity/withdraw/apply:
    post:
      summary: Withdraw Travel Rule (USER_DATA)
      x-summary-cn: 提币(针对需要旅行规则的本地站) (USER_DATA)
      description: Submit a withdrawal request for local entities that required travel rule.
      x-description-cn: 向需要旅行规则的本地站发起提币请求
      tags:
        - travel-rule
      operationId: withdrawTravelRule
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/core-trading-wallet/api/rest-api/travel-rule#withdraw-travel-rule
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/wallet/examples/rest-api/TravelRuleApi/withdrawTravelRule.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/wallet/rest_api/travel_rule_api/withdraw_travel_rule.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/wallet/examples/rest_api/TravelRule/withdraw_travel_rule.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/wallet/src/main/java/com/binance/connector/client/wallet/rest/travelrule/WithdrawTravelRuleExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/wallet/examples/restapi/TravelRuleAPI/WithdrawTravelRule/WithdrawTravelRule.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/wallet/travelrule/WithdrawTravelRuleExample.php
      x-security-type: USER_DATA
      x-signed: true
      x-uid-weight: 600
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
        - If `network` not send, return with default network of the coin, but if the address could not match default
        network, the withdraw will be rejected.

        - You can get `network` and `isDefault` in `networkList` of a coin in the response of `Get
        /sapi/v1/capital/config/getall (HMAC SHA256)`.

        - Questionnaire is different for each local entity, please refer to the `Withdraw Questionnaire Contents` page.

        - If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to
        verify the format of the questionnaire and use URL-encoded format.
      x-parameters-notes-cn: >-
        - 如果没有传入 `network`, 则使用对应币种的默认网络, 如果地址格式不能匹配默认网络, 提币将被拒绝。

        - 网络、默认网络的配置列表可以通过以下接口获取 `Get /sapi/v1/capital/config/getall (HMAC SHA256)`。

        - 每个本地站点的问卷内容都不一样，请参考`提币问卷内容`页。

        - 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误，请尝检查Questionnaire格式并使用
        `URL-encoded format`。
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - coin
                - address
                - amount
                - questionnaire
                - timestamp
              properties:
                coin:
                  type: string
                  example: BTC
                withdrawOrderId:
                  type: string
                  example: "1"
                  description: withdrawID defined by the client (i.e. client's internal withdrawID)
                  x-description-cn: 客户端内部定义的提币ID.
                network:
                  type: string
                  example: null
                  description: Withdrawal network
                  x-description-cn: 提币网络
                address:
                  type: string
                  example: null
                  description: Withdrawal address
                  x-description-cn: 提币地址
                addressTag:
                  type: string
                  example: null
                  description: Secondary address identifier for coins like XRP,XMR etc.
                  x-description-cn: 某些币种例如 XRP,XMR 允许填写次级地址标签
                amount:
                  type: number
                  example: "1.0"
                  format: float
                  description: Amount
                  x-description-cn: 数量
                transactionFeeFlag:
                  type: boolean
                  example: true
                  description: |-
                    When making internal transfer, `true` for returning the fee to the destination account; `false` for
                    returning the fee back to the departure account. Default `false`.
                  x-description-cn: "当站内转账时免手续费, `true`: 手续费归资金转入方; `false`: 手续费归资金转出方; . 默认 `false`."
                name:
                  type: string
                  example: null
                walletType:
                  type: integer
                  example: 0
                  format: int64
                  description: |-
                    The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current
                    "selected wallet" under wallet->Fiat and Spot/Funding->Deposit
                  x-description-cn: 表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。
                recvWindow:
                  type: integer
                  example: 5000
                  format: int64
                  maximum: 60000
                questionnaire:
                  type: string
                  example: null
                  description: JSON format questionnaire answers.
                  x-description-cn: JSON 格式的问卷回答。
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
          description: Withdraw
          x-description-cn: 提币
          content:
            application/json:
              schema:
                type: object
                properties:
                  trId:
                    type: integer
                    example: 123456
                    format: int64
                    description: The travel rule record Id
                    x-description-cn: Travel Rule记录ID
                  accepted:
                    type: boolean
                    example: true
                    description: Whether the withdraw request is accepted
                    x-description-cn: 提币请求是否被接受
                  info:
                    type: string
                    example: Withdraw request accepted
                    description: The detailed infomation of the withdrawal result.
                    x-description-cn: 提现结果的详细信息
```