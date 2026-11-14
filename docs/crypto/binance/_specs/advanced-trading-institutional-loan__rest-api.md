---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:16.090911
---

# advanced-trading-institutional-loan__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Institutional Loan REST API
  description: Access institutional loan services for portfolio margin and futures trading.
  x-description-cn: 访问机构借贷服务，用于统一账户和合约交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/institutional-loan/general-info#limits
x-rate-limits-guide-cn: products/institutional-loan/general-info#访问限制
x-security-guide: products/institutional-loan/general-info#request-security
x-security-guide-cn: products/institutional-loan/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Institutional Loan docs
  url: https://developers.binance.com/en/docs/products/institutional-loan/Introduction
tags:
  - name: account
    x-displayName: Account
    x-displayName-cn: 账户接口
  - name: borrow-repay
    x-displayName: Borrow and Repay
    x-displayName-cn: 借还款接口
  - name: trade
    x-displayName: Trade
    x-displayName-cn: 交易接口
  - name: transfer
    x-displayName: Transfer
    x-displayName-cn: 划转接口
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/margin/loan-group/edit-member:
    post:
      summary: Add Collateral Accounts (TRADE)
      x-summary-cn: 添加抵押子账户 (TRADE)
      description: >-
        Add new collateral accounts for the Risk Unit. This endpoint is accessible only with the parent account API key.


        * For the credit account, the enableMargin should always be TRUE.

        * Collateral sub-accounts can be added to the Risk Unit but cannot be removed. Therefore, the enableSpot or
        enableMargin parameters cannot be switched from TRUE to FALSE once the sub-account is activated in the Risk
        Unit. If you need to remove credit or collateral sub-accounts from the Risk Unit, please contact the Binance
        Margin team for support.
      x-description-cn: |-
        添加风险单位的抵押子账户，仅支持母账户调用该接口。

        * 如果参数subEmail 为信用贷账号，则参数enableMargin必须设置为TRUE，不能设置为FALSE。
        * 参数enableSpot 和 enableMargin 只能从FALSE变更到TRUE，不能从TRUE变更到FALSE。即不能通过该接口移除抵押子账户，若想要移除抵押子账户，需联系杠杆团队。
      tags:
        - account
      operationId: addCollateralAccounts
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/account#add-collateral-accounts
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 1000
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
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
                - groupId
                - subEmail
                - enableSpot
                - enableMargin
                - timestamp
              properties:
                groupId:
                  type: integer
                  example: 1
                  format: int64
                subEmail:
                  type: string
                  example: abc@test.com
                enableSpot:
                  type: boolean
                  example: true
                enableMargin:
                  type: boolean
                  example: true
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
          description: Add Collateral Accounts
          x-description-cn: 添加抵押子账户
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    example: 0
                    format: int64
  /sapi/v1/margin/loan-group:
    delete:
      summary: Close Risk Unit (TRADE)
      x-summary-cn: 关闭风险单位 (TRADE)
      description: |-
        The closure of the Institutional Loan risk unit can only be initiated by API calls from the credit account. If
        the closure is successful all the collateral accounts will be unlinked. Please note the following conditions
        must be met:
          * The Institution Loan risk unit is active.
          * The outstanding institutional loan liabilities for that particular risk unit have been repaid.
      x-description-cn: |-
        关闭操作仅支持通过机构借贷子账户 API 执行。成功关闭后，系统将自动解除该风险单位与所有抵押账户的关联。请注意，操作前需满足以下条件：
          * 机构贷单位处于生效活跃状态。
          * 已全额偿还此风险单位内贷款及利息。
      tags:
        - account
      operationId: closeRiskUnit
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/account#close-risk-unit
      x-security-type: TRADE
      x-signed: true
      x-uid-weight: 1000
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: groupId
          in: query
          required: true
          schema:
            type: integer
            example: 1
            format: int64
          description: Risk unit unique identifier
          x-description-cn: 唯一风险单位标识符
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
          description: Close Risk Unit
          x-description-cn: 关闭风险单位
          content:
            application/json:
              schema:
                type: object
                properties:
                  groupId:
                    type: integer
                    example: 10001
                    format: int64
                    description: Risk unit unique identifier
                    x-description-cn: 唯一风险单位标识符
                  status:
                    type: string
                    example: CLOSED
                    description: "CLOSED: This risk unit has been closed successfully"
                    x-description-cn: "CLOSED: 此风险单位已成功关闭"
    get:
      summary: Query One Risk Unit Detail (USER_DATA)
      x-summary-cn: 查询单个风险单元详情 (USER_DATA)
      description: Query One Institution Loan Group Details which is executed by credit account
      x-description-cn: 查询单个机构贷风险单位详情，仅支持放贷账户调用该接口。
      tags:
        - account
      operationId: queryOneRiskUnitDetail
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/account#query-one-risk-unit-detail
      x-ip-weight: 3000
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
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: One Risk Unit Detail
          x-description-cn: 单个风险单元详情
          content:
            application/json:
              schema:
                type: object
                properties:
                  groupId:
                    type: integer
                    format: int64
                    example: 3
                  parentEmail:
                    type: string
                    example: parent001@test.com
                  creditEmail:
                    type: string
                    example: credit001@test.com
                  updateTime:
                    type: integer
                    format: int64
                    example: 1747910351205
                  ltv:
                    type: string
                    example: "0.336"
                  totalNetEquity:
                    type: string
                    example: "598569.620904"
                  totalMaintenanceMargin:
                    type: string
                    example: "375.23555369"
                  totalLiability:
                    type: string
                    example: "200850.274625"
                  liabilities:
                    type: array
                    items:
                      type: object
                      properties:
                        assetName:
                          type: string
                          example: USDT
                        principal:
                          type: string
                          example: "200099.9"
                        interest:
                          type: string
                          example: "750.374625"
                  accountInfos:
                    type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          example: collateral001@test.com
                        accountType:
                          type: string
                          example: PORTFOLIO_MARGIN
                        netEquity:
                          type: string
                          example: "219961.43492975"
                        maintainMargin:
                          type: string
                          example: "50.10676987"
  /sapi/v1/margin/loan-groups/closed:
    get:
      summary: Query Closed Risk Unit Record (USER_DATA)
      x-summary-cn: 查询关闭的风险单元记录 (USER_DATA)
      description: Query closed risk unit record. This endpoint is accessible only with the credit account API key.
      x-description-cn: 查询已关闭的风险单元记录。仅支持放贷账户调用该接口。
      tags:
        - account
      operationId: queryClosedRiskUnitRecord
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/account#query-closed-risk-unit-record
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
        - name: current
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
            default: 1
          description: Current page number. Starts from 1.
          x-description-cn: 当前页码，从 1 开始。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 10
            default: 10
            maximum: 100
          description: Number of records per page.
          x-description-cn: 每页记录条数。
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Closed Risk Unit Records
          x-description-cn: 关闭的风险单元记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    format: int64
                    example: 2
                    description: Total number of risk units returned by the query.
                    x-description-cn: 查询返回的风险单元总数。
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        groupId:
                          type: integer
                          format: int64
                          example: 72
                          description: Risk unit unique identifier.
                          x-description-cn: 唯一风险单位标识符。
                        parentEmail:
                          type: string
                          example: wdywgceiwbfq@test.com
                          description: Parent account  email
                          x-description-cn: 母账户邮箱。
                        creditEmail:
                          type: string
                          example: wdywaxmzlnah@test.com
                          description: Credit account  email
                          x-description-cn: 放贷账户邮箱。
                        enabled:
                          type: boolean
                          example: false
                          description: The status of the group. TRUE for enabled; FALSE for disabled.
                          x-description-cn: 风险单位状态。TRUE 表示活跃；FALSE 表示关闭。
                        createTime:
                          type: integer
                          format: int64
                          example: 1753410654608
                          description: The group create  timestamp (milliseconds)
                          x-description-cn: 风险单位创建时间戳（毫秒）。
                        closeTime:
                          type: integer
                          format: int64
                          example: 1753422899052
                          description: The group close timestamp (milliseconds)
                          x-description-cn: 风险单位关闭时间戳（毫秒）。
  /sapi/v1/margin/loan-groups/activated:
    get:
      summary: Query Active Risk Units (USER_DATA)
      x-summary-cn: 查询有效风险单位 (USER_DATA)
      description: |-
        Retrieves the list of active institutional loan risk units. This endpoint is accessible only with the parent
        account API key.
      x-description-cn: 查询生效状态的机构贷风险单位列表。仅支持母账户查询该接口。
      tags:
        - account
      operationId: queryActiveRiskUnits
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/account#query-active-risk-units
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
          description: Active Risk Units
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    groupId:
                      type: integer
                      example: 10001
                      format: int64
                      description: Risk unit unique identifier
                      x-description-cn: 唯一风险单位标识符
                    members:
                      type: array
                      items:
                        type: object
                        properties:
                          email:
                            type: string
                            example: 1001@test.com
                            description: Account registered email
                            x-description-cn: 账户注册邮箱
                          type:
                            type: string
                            example: CREDIT
                            description: Credit sub account or Collateral sub account
                            x-description-cn: 放贷子账户或抵押子账户
                          enableMargin:
                            type: boolean
                            example: true
                            description: >-
                              TRUE: include margin account as collateral. <br />FALSE: exclude margin account as
                              collateral
                            x-description-cn: "TRUE: 杠杆账户包括在抵押账户内；FALSE: 杠杆账户不包括在抵押账户内"
                          enableSpot:
                            type: boolean
                            example: true
                            description: "TRUE: include spot account as collateral<br />FALSE: exclude spot account as collateral"
                            x-description-cn: "TRUE: 现货账户包括在抵押账户内；FALSE: 现货账户不包括在抵押账户内"
                    createTime:
                      type: integer
                      example: 1747637956083
                      format: int64
                      description: Last update timestamp in milliseconds
                      x-description-cn: 最后更新时间戳（毫秒）
  /sapi/v1/margin/loan-group/ltv-details:
    get:
      summary: Query Risk Unit Details (USER_DATA)
      x-summary-cn: 查询风险单元详情 (USER_DATA)
      description: |-
        Queries institutional loan risk unit details. Both master accounts and borrowing accounts can call this
        endpoint.

        * Master account:
          * If `groupId` is not provided, details of all risk units are returned.
          * If a specific `groupId` is provided, details of that risk unit are returned.

        * Borrowing account:
          * Only risk units bound to that borrowing account can be queried.

        * Other account types:
          * LTV details cannot be queried and no results are returned.
      x-description-cn: |-
        查询机构贷风险单位详情，母账户和借贷账户均可调用该接口。

        * 母账户：

        * 当未提供 groupId 时，可以查询所有风险单位详情。
        * 当提供特定 groupId 时，可以查询单个风险单位详情。
        * 信用账户：

        * 仅支持查询与该借贷账户绑定的风险单位详情。
        * 其他账户：

        * 无法查询LTV详情，无结果返回。
      tags:
        - account
      operationId: queryRiskUnitDetails
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/account#query-risk-unit-details
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
        - name: groupId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Risk unit unique identifier
          x-description-cn: 唯一风险单位标识符
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Risk Unit Details
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    groupId:
                      type: integer
                      example: 1
                      format: int64
                    leverageTier:
                      type: string
                      example: 5X
                      description: Leverage tier of the risk unit, e.g. `5X`. It determines the LTV thresholds below.
                      x-description-cn: 风险单位的杠杆档位，例如 `5X`，决定以下各 LTV 阈值。
                    initialLtv:
                      type: string
                      example: "0.8"
                      description: >-
                        Initial LTV threshold. A new borrow is rejected if it would raise the risk unit LTV above this
                        value.
                      x-description-cn: 初始 LTV 阈值。若新借款会使风险单位 LTV 超过该值，借款将被拒绝。
                    marginCallLtv:
                      type: string
                      example: "0.85"
                      description: Margin call LTV threshold. A margin call is triggered when the risk unit LTV reaches this value.
                      x-description-cn: 追加保证金 LTV 阈值。风险单位 LTV 达到该值时触发追加保证金通知。
                    liquidationLtv:
                      type: string
                      example: "0.9"
                      description: >-
                        Liquidation LTV threshold. Liquidation of the risk unit is triggered when its LTV reaches this
                        value.
                      x-description-cn: 强平 LTV 阈值。风险单位 LTV 达到该值时触发强制平仓。
                    liquidationExitLtv:
                      type: string
                      example: "0.8"
                      description: Liquidation exit LTV threshold. Liquidation stops once the risk unit LTV falls below this value.
                      x-description-cn: 强平结束 LTV 阈值。风险单位 LTV 降至该值以下时停止强平。
                    maxTransferOutLtv:
                      type: string
                      example: "0.83"
                      description: >-
                        Transfer-out LTV threshold. Assets can be transferred out of the risk unit only while
                        `transferOutLtv` is below this value.
                      x-description-cn: 允许划出的 LTV 阈值。仅当 `transferOutLtv` 低于该值时，才可从风险单位划出资产。
                    parentEmail:
                      type: string
                      example: andrew.kemmer001@test.com
                    creditEmail:
                      type: string
                      example: tst20241120@test.com
                    updateTime:
                      type: integer
                      example: 1752137105623
                      format: int64
                    ltv:
                      type: string
                      example: "0.592"
                    totalNetEquity:
                      type: string
                      example: "26.35196946"
                    totalMaintenanceMargin:
                      type: string
                      example: "0.50106177"
                    totalLiability:
                      type: string
                      example: "15.30718771"
                    transferOutLtv:
                      type: string
                      example: "0.61"
                      description: >-
                        LTV used for transfer-out checks. Calculated in the same way as `ltv`, but only the net equity
                        of Cross Margin and Portfolio Margin accounts is counted; collateral in Spot wallets is
                        excluded, so it can be higher than `ltv`. `maxTransferOutAmount` and `parentAccountFrozenAmount`
                        are based on this value.
                      x-description-cn: >-
                        用于划出校验的 LTV。计算方式与 `ltv` 相同，但仅计入全仓杠杆账户和统一账户的净资产，不计入现货钱包中的抵押品，因此可能高于 `ltv`。`maxTransferOutAmount`
                        与 `parentAccountFrozenAmount` 均基于该值计算。
                    parentAccountFrozenAmount:
                      type: string
                      example: "8.18753688"
                    maxTransferOutAmount:
                      type: string
                      example: "0"
                    maxAllowedBorrowLimit:
                      type: string
                      example: "16.32397222"
                      description: >-
                        The USDT-equivalent maximum borrowable amount for this risk unit. Note: this value does not
                        account for the borrowed asset's collateral ratio. For assets with a collateral ratio below
                        100%, the actual maximum borrowable quantity still considers the borrowed asset's collateral
                        ratio. The applicable collateral ratio depends on the margin mode of the credit account.
                      x-description-cn: >-
                        该风险单元的最大可借金额（以 USDT 等值计算）。注意：此数值未计入借入资产的抵押率。对于抵押率低于 100%
                        的借入资产，实际最大可借数量还需考虑借入资产的抵押率。适用的抵押率取决于放贷账户的杠杆模式。
                    liabilities:
                      type: array
                      items:
                        type: object
                        properties:
                          assetName:
                            type: string
                            example: USDT
                          principal:
                            type: string
                            example: "15.30718771"
                          interest:
                            type: string
                            example: "0"
                    collateralAccounts:
                      type: array
                      items:
                        type: object
                        properties:
                          email:
                            type: string
                            example: collateral001@test.com
                          type:
                            type: string
                            example: COLLATERAL
                          wallets:
                            type: array
                            items:
                              type: object
                              properties:
                                accountType:
                                  type: string
                                  example: SPOT
                                netEquity:
                                  type: string
                                  example: "5"
                                maintainMargin:
                                  type: string
                                  example: "0"
  /sapi/v1/margin/loan-group/borrow:
    post:
      summary: Risk Unit Borrow (TRADE)
      x-summary-cn: 风险单位借款 (TRADE)
      description: >-
        This endpoint is used to perform a borrow request for that specified risk unit. This endpoint is accessible only

        with the credit account API key.


        * You need to open **Enable Spot & Margin Trading** permission for the API Key which requests this endpoint.

        * The `amount` field refers to the quantity of the borrowed asset. The maximum allowable amount is subject to
        collateral ratio adjustment. The applicable collateral ratio depends on the margin mode of the credit account.
      x-description-cn: |-
        机构贷风险单位借款。仅支持放贷账户调用该接口。

        * 您需要打开 API Key 的 **Spot & Margin Trading** 权限以使用此接口。
        * `amount` 字段为借入资产的数量。最大可借数量须经抵押率调整，适用的抵押率取决于放贷账户的杠杆模式。
      tags:
        - borrow-repay
      operationId: riskUnitBorrow
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#risk-unit-borrow
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - groupId
                - assetName
                - amount
                - timestamp
              properties:
                groupId:
                  type: integer
                  example: 1
                  format: int64
                assetName:
                  type: string
                  example: USDT
                  description: Asset Name , USDT or USDC or BTC or U
                  x-description-cn: 资产名称，如 USDT 或 USDC 或 BTC 或 U
                amount:
                  type: number
                  example: 1
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
          description: Risk Unit Borrow
          x-description-cn: 风险单位借款
          content:
            application/json:
              schema:
                type: object
                properties:
                  transactionId:
                    type: integer
                    example: 12317283617
                    format: int64
                  amount:
                    type: number
                    example: 123456.78
                    format: float
                  status:
                    type: string
                    example: success
  /sapi/v1/margin/loan-group/borrow-repay:
    get:
      summary: Risk Unit Borrow/Repay Records (USER_DATA)
      x-summary-cn: 查询风险单元借贷/还款记录 (USER_DATA)
      description: >-
        Get borrow/repay records in the Institution Loan Risk Unit. This endpoint is accessible only with the credit
        account API key.
      x-description-cn: 查询风险单位借贷/还款记录，仅支持放贷账户调用该接口。
      tags:
        - borrow-repay
      operationId: riskUnitBorrowRepayRecords
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#risk-unit-borrow-repay-records
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
        - name: groupId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
          description: Risk unit unique identifier
          x-description-cn: 唯一风险单位标识符
        - name: type
          in: query
          required: true
          schema:
            type: string
            example: BORROW
            enum:
              - BORROW
              - REPAY
          description: BORROW or REPAY
          x-description-cn: 操作类型：BORROW 或 REPAY
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: USDT
          description: Asset name, for example USDT or USDC
          x-description-cn: 资产名称，例如 USDT 或 USDC
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1750420000000
          description: Start time in milliseconds.
          x-description-cn: 开始时间戳（毫秒）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1750420899036
          description: End time in milliseconds.
          x-description-cn: 结束时间戳（毫秒）。
        - name: current
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
            default: 1
          description: Current page number. Starts from 1.
          x-description-cn: 当前页码，从 1 开始。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 10
            default: 10
            maximum: 100
          description: Number of records per page.
          x-description-cn: 每页记录条数。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 5000
            maximum: 60000
          description: Request validity window in milliseconds.
          x-description-cn: 请求有效时间窗口，单位为毫秒。
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Credit account can query either activated risk unit or closed risk unit with the specific groupId. The current
        activated risk unit will be returned if the parameter of groupId is not input.

        - Response in descending order

        - If  the asset parameter is provided, the maximum query time range is 30 days ahead of  endTime;  if the asset
        parameter is not provided the maximum query time range is 7 days ahead of endTime

        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.

        - startTime set as endTime - 7days by default, endTime set as current time by default

        - The length of startTime and  endTime  cannot exceed 100 days, otherwise an error is reported and no record is
        returned.
      x-parameters-notes-cn: >-
        - 放贷账户可根据参数 groupId 查询当前生效状态风险单位和已关闭风险单位；若 groupId 为空，则返回当前生效状态风险单位。 * 响应返回为降序排列。 * 若传了 `asset` 参数，最大查询时间范围为
        `endTime` 往前 30 天；不传 `asset` 参数，最大查询时间范围为 `endTime` 往前 7 天。 * 若 `startTime` 和 `endTime` 都未传，则默认返回最近 7 天数据。 * 默认
        `startTime = endTime - 7 天`，`endTime = 当前时间`。 * `startTime` 和 `endTime` 时间长度不能超过 100 天。
      responses:
        "200":
          description: Risk Unit Borrow/Repay Records
          x-description-cn: 风险单元借贷/还款记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    format: int64
                    example: 1
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        tranId:
                          type: integer
                          format: int64
                          example: 1648963682
                        assetName:
                          type: string
                          example: USDT
                        amount:
                          type: number
                          format: float
                          example: 300
                        principal:
                          type: number
                          format: float
                          example: 298
                        interest:
                          type: number
                          format: float
                          example: 2
                        status:
                          type: string
                          example: CONFIRM
                        type:
                          type: string
                          example: BORROW
                          description: BORROW, NORMAL_REPAY, FORCE_REPAY
                          x-description-cn: BORROW、NORMAL_REPAY、FORCE_REPAY
                        timestamp:
                          type: integer
                          format: int64
                          example: 1750420899036
                          description: Create Time
                          x-description-cn: Create Time
  /sapi/v1/margin/loan-group/interest-history:
    get:
      summary: Risk Unit Interest History (USER_DATA)
      x-summary-cn: 风险单位历史利息 (USER_DATA)
      description: |-
        Query Institutional loan risk unit interest history. This endpoint is accessible only with the credit account
        API key.
      x-description-cn: 查询机构贷风险单位给定时间段内的利息历史记录。此接口仅可使用信用账户API Key访问。
      tags:
        - borrow-repay
      operationId: riskUnitInterestHistory
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#risk-unit-interest-history
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
        - name: groupId
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
          description: Unique risk unit identifier
          x-description-cn: 唯一风险单位标识符
        - name: asset
          in: query
          required: false
          schema:
            type: string
            example: USDT
          description: Asset name, for example USDT or USDC.
          x-description-cn: 资产名称，例如 USDT 或 USDC。
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            example: 1623319461670
            format: int64
          description: Start time in milliseconds.
          x-description-cn: 开始时间戳（毫秒）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            example: 1641782889000
            format: int64
          description: End time in milliseconds.
          x-description-cn: 结束时间戳（毫秒）。
        - name: current
          in: query
          required: false
          schema:
            type: integer
            example: 1
            format: int64
            default: 1
          description: Current page number. Starts from 1.
          x-description-cn: 当前页码，从 1 开始。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            example: 10
            format: int64
            default: 10
            maximum: 100
          description: Number of records per page.
          x-description-cn: 每页记录条数。
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
        - Credit account can query currently activated and closed risk units using the parameter groupId. If groupId is
        empty, only currently activated risk units are returned.

        - Responses are returned in descending order.

        - The max interval between startTime and endTime is 100 days. This is required to ensure data accuracy.

        - If startTime and endTime are not provided, data from the last 7 days is returned by default.

        - If startTime is provided but endTime is omitted, returns records of [max(startTime, now-30d), now].

        - If startTime is omitted but endTime is provided, returns records of [endTime-7, endTime].
      x-parameters-notes-cn: >-
        - 放贷账户可根据参数 `groupId` 查询当前生效状态风险单位和已关闭风险单位；若 `groupId` 为空，则仅返回当前生效状态风险单位。 * 响应返回为降序排列。 * `startTime` 和 `endTime`
        的最大间隔为 100 天，以确保数据准确性。 * 若 `startTime` 和 `endTime` 未传，则默认返回最近 7 天数据。 * 若传了 `startTime` 但未传 `endTime`，返回区间
        `[max(startTime, 当前时间-30天), 当前时间]` 的记录。 * 若未传 `startTime` 但传了 `endTime`，返回区间 `[endTime-7天, endTime]` 的记录。
      responses:
        "200":
          description: Risk Unit Interest History
          x-description-cn: 风险单位利息历史
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 2
                    format: int64
                    description: Number of historical interest records.
                    x-description-cn: 历史利息记录总数。
                  rows:
                    type: array
                    description: Interest history records.
                    x-description-cn: 利息历史记录列表。
                    items:
                      type: object
                      properties:
                        groupId:
                          type: integer
                          example: 2
                          format: int64
                        assetName:
                          type: string
                          example: USDC
                        principal:
                          type: number
                          example: 851340.57601652
                          format: float
                        interestRate:
                          type: number
                          example: 0.00000833
                          format: float
                        interest:
                          type: number
                          example: 7.09447643
                          format: float
                        interestTimestamp:
                          type: integer
                          example: 1746442800000
                          format: int64
  /sapi/v1/margin/loan-group/repay:
    post:
      summary: Risk Unit Repay (TRADE)
      x-summary-cn: 风险单位还款 (TRADE)
      description: >-
        This endpoint is used to perform full or partial repayment of the specified risk unit. This endpoint is

        accessible only with the credit account API key.


        By default (repayFrom=MARGIN), funds are deducted from the credit account's Margin account. When repayFrom=SPOT,
        funds are deducted directly from the credit account's Spot account.


        * You need to open **Enable Spot & Margin Trading** permission for the API Key which requests this endpoint.
      x-description-cn: |-
        机构贷风险单位全部或部分还款，仅支持放贷账户调用该接口。

        默认情况下（repayFrom=MARGIN），资金从放贷账户的杠杆账户中扣除。当 repayFrom=SPOT 时，资金直接从放贷账户的现货账户中扣除。

        * 您需要打开 API Key 的 **Spot & Margin Trading** 权限以使用此接口。
      tags:
        - borrow-repay
      operationId: riskUnitRepay
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#risk-unit-repay
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
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              required:
                - groupId
                - assetName
                - amount
                - timestamp
              properties:
                groupId:
                  type: integer
                  example: 1
                  format: int64
                assetName:
                  type: string
                  example: USDT
                  description: Asset name to repay
                  x-description-cn: 还款资产名称
                amount:
                  type: number
                  example: 1
                  format: float
                repayFrom:
                  type: string
                  example: MARGIN
                  description: >-
                    Funding source for repayment. MARGIN (default): deduct from credit account's Margin account. SPOT:
                    deduct directly from credit account's Spot account.
                  x-description-cn: 还款资金来源。MARGIN（默认）：从放贷账户杠杆账户扣款；SPOT：直接从放贷账户现货账户扣款。
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
          description: Risk Unit Repay
          x-description-cn: 风险单位还款
          content:
            application/json:
              schema:
                type: object
                properties:
                  transactionId:
                    type: integer
                    example: 12317283617
                    format: int64
                  amount:
                    type: number
                    example: 123456.78
                    format: float
                  repayFrom:
                    type: string
                    example: MARGIN
                    description: Funding source used for this repayment.
                    x-description-cn: 还款资金来源。
  /sapi/v1/margin/loan-group/interest-rebate-balance:
    get:
      summary: Query Interest Rebate Balance (USER_DATA)
      x-summary-cn: 查询利息减免额度 (USER_DATA)
      description: >-
        Query the interest rebate balance for an institutional loan master account, including the remaining balance,
        total granted amount, and total consumed amount, all denominated in USDT. This endpoint requires authentication
        with the parent account API key.
      x-description-cn: 查询机构借贷的利息减免额度，包括剩余可用额度、累计发放金额及累计消耗金额，所有金额均以 USDT 计价。仅支持母账户调用该接口。
      tags:
        - borrow-repay
      operationId: queryInterestRebateBalance
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#query-interest-rebate-balance
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
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Please refer to [this article](https://www.binance.com/en/support/faq/detail/3a6b5c4a6ed34bff9d56cfe172e6d6ee)
        for more details.
      x-parameters-notes-cn: "- 请参阅[此文章](https://www.binance.com/zh-CN/support/faq/detail/3a6b5c4a6ed34bff9d56cfe172e6d6ee)了解详情。"
      responses:
        "200":
          description: Query Interest Rebate Balance
          x-description-cn: 查询利息减免额度
          content:
            application/json:
              schema:
                type: object
                properties:
                  asset:
                    type: string
                    example: USDT
                    description: Asset name
                    x-description-cn: 资产名称
                  balance:
                    type: string
                    example: "91.64958606"
                    description: >-
                      Current rebate balance remaining; represents the amount still available to offset future interest
                      charges
                    x-description-cn: 当前剩余可用利息减免额度，代表仍可用于抵扣未来机构借贷利息的金额
                  totalGranted:
                    type: string
                    example: "150.00000000"
                    description: The total rebate amount that has ever been credited to your account
                    x-description-cn: 账户累计获得的减免总金额
                  totalConsumed:
                    type: string
                    example: "58.35041394"
                    description: The total rebate amount that has already been used up to pay off interest
                    x-description-cn: 已用于抵扣利息的减免总金额
  /sapi/v1/margin/loan-group/interest-rebate-balance/records:
    get:
      summary: Query Interest Rebate Balance Records (USER_DATA)
      x-summary-cn: 查询利息减免额度变动记录 (USER_DATA)
      description: >-
        Query change records for an institutional loan interest rebate balance. Includes ADD (admin grant), DEDUCT
        (admin deduction), and INTEREST_OFFSET (system interest deduction) types.
      x-description-cn: 查询机构贷利息减免额度的加减流水。包括发放(ADD)、扣减(DEDUCT)、利息抵扣(INTEREST_OFFSET)三种类型。
      tags:
        - borrow-repay
      operationId: queryInterestRebateBalanceRecords
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#query-interest-rebate-balance-records
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
        - name: type
          in: query
          schema:
            type: integer
            example: 0
            enum:
              - 0
              - 1
              - 2
          description: "Record type filter: 0=ADD, 1=DEDUCT, 2=INTEREST_OFFSET. Returns all if not specified."
          x-description-cn: "记录类型筛选: 0=发放, 1=扣减, 2=利息抵扣。不传则返回全部。"
        - name: startTime
          in: query
          schema:
            type: integer
            format: int64
            example: 1711843200000
          description: Start time in ms
          x-description-cn: 开始时间（毫秒）
        - name: endTime
          in: query
          schema:
            type: integer
            format: int64
            example: 1712102400000
          description: End time in ms
          x-description-cn: 结束时间（毫秒）
        - name: current
          in: query
          schema:
            type: integer
            format: int64
            default: 1
            example: 1
          description: Page number, default 1
          x-description-cn: 页码，默认 1
        - name: size
          in: query
          schema:
            type: integer
            format: int64
            default: 10
            maximum: 100
            example: 10
          description: Page size, default 10, max 100
          x-description-cn: 每页数量，默认 10，最大 100
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Query Interest Rebate Balance Records
          x-description-cn: 查询利息减免额度变动记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    example: 3
                    format: int64
                    description: Total number of records
                    x-description-cn: 记录总数
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        type:
                          type: string
                          example: ADD
                          enum:
                            - ADD
                            - DEDUCT
                            - INTEREST_OFFSET
                          description: ADD / DEDUCT / INTEREST_OFFSET
                          x-description-cn: 发放(ADD) / 扣减(DEDUCT) / 利息抵扣(INTEREST_OFFSET)
                        groupId:
                          type: integer
                          example: 10005
                          format: int64
                          description: Loan group ID (only for INTEREST_OFFSET)
                          x-description-cn: 贷款组 ID（仅利息抵扣）
                        rebateAsset:
                          type: string
                          example: USDT
                          description: Rebate asset (USDT)
                          x-description-cn: 额度币种（USDT）
                        delta:
                          type: string
                          example: "5000.00000000"
                          description: Amount change. Positive for ADD, negative for DEDUCT/INTEREST_OFFSET
                          x-description-cn: 变动金额。发放为正，扣减/抵扣为负
                        liabilityAsset:
                          type: string
                          example: BTC
                          description: Liability asset (only for INTEREST_OFFSET)
                          x-description-cn: 负债币种（仅利息抵扣）
                        deductedInterest:
                          type: string
                          example: "0.00050123"
                          description: Deducted interest in liability asset (only for INTEREST_OFFSET)
                          x-description-cn: 抵扣利息金额，以负债币种计（仅利息抵扣）
                        exchangeRate:
                          type: string
                          example: "0.00001000"
                          description: Exchange rate snapshot (only for INTEREST_OFFSET)
                          x-description-cn: 汇率快照（仅利息抵扣）
                        createTime:
                          type: integer
                          example: 1711843200000
                          format: int64
                          description: Record creation time in ms
                          x-description-cn: 记录创建时间（毫秒）
  /sapi/v1/margin/loan-group/max-borrowable:
    get:
      summary: Query Loan Group Max Borrowable (USER_DATA)
      x-summary-cn: 查询风险单位最大可借金额 (USER_DATA)
      description: >-
        Query the maximum borrowable amount of a given asset for an institutional loan risk unit.


        This endpoint can be accessed using the API key from either the parent or the credit account:


        - If the API key belongs to the **credit account**, `groupId` is optional. When omitted, the member's own risk
        unit is used; when provided, it must match the member's risk unit, otherwise an empty result is returned.

        - If the API key belongs to the **parent account**, `groupId` is **required** and must be owned by the parent
        account, otherwise an empty result is returned.

        - If the caller is neither the parent account nor the credit member of the group (e.g., a collateral member, or
        no matching risk unit), `maxBorrowableAmount` is returned as empty/null.
      x-description-cn: |-
        查询机构借贷风险单位内指定币种的最大可借金额。

        本接口可使用母账户或放贷账户的 API Key 进行访问：

        - 若 API key 属于**放贷账户 (credit account)**：`groupId` 可选。不传时使用该成员所属的风险单位；传了则必须与成员所属风险单位一致，否则返回空结果。
        - 若 API key 属于**母账户**：`groupId` **必传**，且必须归属于该母账户，否则返回空结果。
        - 若调用方既不是母账户也不是该风险单位的放贷账户（如抵押子账户，或没有匹配的风险单位）：`maxBorrowableAmount` 返回空/null。
      tags:
        - borrow-repay
      operationId: queryLoanGroupMaxBorrowable
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/borrow-repay#query-loan-group-max-borrowable
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
        - name: groupId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 123456789
          description: >-
            Loan group id. Optional when the API key belongs to the credit member; required when it belongs to the
            parent account.
          x-description-cn: 风险单位组 ID。key 为 credit 成员时可选；key 为母账户时必填。
        - name: assetName
          in: query
          required: true
          schema:
            type: string
            example: USDT
          description: >-
            Asset to borrow, e.g., `USDT`. Case-insensitive (normalized to upper-case). Must be a borrowable asset,
            otherwise an error is returned.
          x-description-cn: 借贷币种，如 `USDT`。大小写不敏感（自动转大写）。必须是可借币种，否则报错。
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
          description: Query Loan Group Max Borrowable
          x-description-cn: 查询风险单位最大可借金额
          content:
            application/json:
              schema:
                type: object
                properties:
                  maxBorrowableAmount:
                    type: string
                    example: "12345.67890000"
                    description: >-
                      Max borrowable amount of the asset for the risk unit. Empty/null when the caller has no matching
                      risk unit.
                    x-description-cn: 该风险单位下指定币种的最大可借金额。无匹配的风险单位时返回空/null。
  /sapi/v1/margin/loan-group/force-liquidation:
    get:
      summary: Get Risk Unit Force Liquidation Record (USER_DATA)
      x-summary-cn: 查询风险单元强制平仓记录 (USER_DATA)
      description: >-
        Get institutional loan risk unit force liquidation records. This endpoint is accessible only with the credit
        account API key.
      x-description-cn: 获取风险单位强制平仓记录。仅支持放贷账户调用该接口。
      tags:
        - trade
      operationId: getRiskUnitForceLiquidationRecord
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/trade#get-risk-unit-force-liquidation-record
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
        - name: groupId
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 6
          description: Risk unit unique identifier
          x-description-cn: 唯一风险单位标识符
        - name: startTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1748381716906
          description: Start time in milliseconds.
          x-description-cn: 开始时间戳（毫秒）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1748525848742
          description: End time in milliseconds.
          x-description-cn: 结束时间戳（毫秒）。
        - name: current
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
            default: 1
          description: Current page number. Starts from 1.
          x-description-cn: 当前页码，从 1 开始。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 10
            default: 10
            maximum: 100
          description: Number of records per page.
          x-description-cn: 每页记录条数。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 5000
            maximum: 60000
          description: Request validity window in milliseconds.
          x-description-cn: 请求有效时间窗口，单位为毫秒。
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: Unix timestamp in milliseconds used to sign the request.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Credit account may query currently activated and closed risk unit based on the parameter groupId. If groupId
        is empty, only currently activated risk units will be returned.

        - Responses are returned in descending order.

        - If startTime and endTime are not provided, data from the last 7 days will be returned by default.

        - If startTime is omitted, it defaults to endTime minus 7 days.

        - If endTime is omitted, it defaults to the current time.

        - The time span between startTime and endTime must not exceed 100 days; otherwise, an error will be returned
        with no records.
      x-parameters-notes-cn: >-
        - 放贷账户可根据 `groupId` 查询当前生效状态风险单位和已关闭风险单位；若 `groupId` 为空，则仅返回当前生效状态风险单位。 * 响应返回为降序排列。 * 若 `startTime` 和 `endTime`
        未传，则默认返回最近 7 天数据。 * 若 `startTime` 未传，默认 `endTime - 7 天`；若 `endTime` 未传，默认当前时间。 * `startTime` 和 `endTime`
        的时间跨度不能超过 100 天。
      responses:
        "200":
          description: Risk Unit Force Liquidation Records
          x-description-cn: 风险单元强制平仓记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    format: int64
                    example: 2
                    description: Total risk unit number
                    x-description-cn: 风险单位数量
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        groupId:
                          type: integer
                          format: int64
                          example: 6
                          description: Risk unit unique identifier.
                          x-description-cn: 唯一风险单位标识符。
                        startLtv:
                          type: integer
                          format: int64
                          example: 1
                          description: The initial LTV for the risk unit
                          x-description-cn: 初始贷款价值比。
                        endLtv:
                          type: integer
                          format: int64
                          example: 0
                          description: The current LTV for the risk unit
                          x-description-cn: 最新贷款价值比。
                        liquidationStartTime:
                          type: integer
                          format: int64
                          example: 1748381716906
                          description: Liquidation start timestamp (milliseconds)
                          x-description-cn: 强平开始时间（毫秒）。
                        liquidationEndTime:
                          type: integer
                          format: int64
                          example: 1748525848742
                          description: Liquidation end timestamp (milliseconds)
                          x-description-cn: 强平结束时间（毫秒）。
                        totalNetEquity:
                          type: string
                          example: "16671.5507973"
                          description: >-
                            ∑Equity in all PM sub account + ( ∑Collateral Value - ∑(Liability + Interest) in all Cross
                            Margin account + Free accepted tokens in spot
                          x-description-cn: Σ所有统一账户子账户抵押品权益 + Σ 抵押品价值 - Σ 全仓杠杆账户（负债 + 利息） + 现货可用资产
                        totalMaintenanceMargin:
                          type: string
                          example: "0"
                          description: Aggregated Maintenance Margin
                          x-description-cn: 维持保证金总额。
                        totalLiability:
                          type: string
                          example: "16667.926"
                          description: Outstanding Loan Principal + Outstanding Loan Interest
                          x-description-cn: 未偿还贷款本金 + 未偿还贷款利息
                        liquidationSnapshot:
                          type: object
                          properties:
                            snapshots:
                              type: array
                              items:
                                type: object
                                properties:
                                  subEmail:
                                    type: string
                                    example: 1000255973134@test.com
                                    description: Sub account registered email
                                    x-description-cn: 子账户注册邮箱
                                  memberType:
                                    type: string
                                    example: CREDIT
                                    description: member type, "CREDIT" or "COLLATERAL"
                                    x-description-cn: 子账号类型，可取值"CREDIT" 或 "COLLATERAL"
                                  walletType:
                                    type: string
                                    example: PORTFOLIO_MARGIN
                                    description: SPOT or PORTFOLIO MARGIN or CROSS MARGIN ACCOUNT
                                    x-description-cn: 钱包类型，可取值 "PORTFOLIO_MARGIN", "SPOT" 或 "CROSS_MARGIN"
                                  netEquity:
                                    type: string
                                    example: "12671.05079731"
                                    description: account net equity
                                    x-description-cn: 账户净资产
                                  maintainMargin:
                                    type: string
                                    example: "0E-8"
                                    description: maintenance margin
                                    x-description-cn: 维持保证金
                            liabilities:
                              type: array
                              items:
                                type: object
                                properties:
                                  assetName:
                                    type: string
                                    example: USDT
                                    description: asset name
                                    x-description-cn: 币种名称
                                  principal:
                                    type: string
                                    example: "11667.92600000"
                                    description: outstanding principal
                                    x-description-cn: 未偿还贷款本金
                                  interest:
                                    type: string
                                    example: "5000.00000000"
                                    description: outstanding interest
                                    x-description-cn: 未偿还利息
  /sapi/v1/margin/loan-group/liquidation-transfer-record:
    get:
      summary: Query Risk Unit Liquidation Transfer Records (USER_DATA)
      x-summary-cn: 查询机构贷强制平仓划转记录 (USER_DATA)
      description: >-
        Query transfer records during institutional loan risk unit forced liquidation. This endpoint is accessible only
        with the credit account API key.
      x-description-cn: 查询机构贷款风险单位强制平仓期间的资金划转记录。仅支持放贷账户调用该接口。
      tags:
        - transfer
      operationId: queryRiskUnitLiquidationTransferRecords
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/transfer#query-risk-unit-liquidation-transfer-records
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
            format: int64
            example: 1765374361589
          description: Start time in milliseconds.
          x-description-cn: 开始时间戳（毫秒）。
        - name: endTime
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1765378830528
          description: End time in milliseconds.
          x-description-cn: 结束时间戳（毫秒）。
        - name: current
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 1
            default: 1
          description: Current page number. Starts from 1.
          x-description-cn: 当前页码，从 1 开始。
        - name: size
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 10
            default: 10
            maximum: 100
          description: Number of records per page.
          x-description-cn: 每页记录条数。
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            format: int64
            example: 5000
            maximum: 60000
          description: Request validity window in milliseconds.
          x-description-cn: 请求有效时间窗口，单位为毫秒。
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            format: int64
            example: 1770736694138
          description: >-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      x-parameters-notes: >-
        - Response in descending order

        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.

        - If startTime is not sent,  default is  endTime - 7days. If  endTime is not sent, current time will be returned
        by default.

        - startTime set as endTime - 7days by default, endTime set as current time by default.

        - The length between  startTime and endTime cannot exceed 100 days, otherwise an error is reported and no record
        is returned.
      x-parameters-notes-cn: >-
        - 响应返回为降序排列。 * 若 `startTime` 和 `endTime` 未传，则默认返回最近 7 天数据。 * 若 `startTime` 未传，默认 `endTime - 7 天`；若 `endTime`
        未传，默认当前时间。 * `startTime` 和 `endTime` 时间长度不能超过 100 天。
      responses:
        "200":
          description: Forced Liquidation Transfer Records
          x-description-cn: 强制平仓划转记录
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    format: int64
                    example: 2
                  rows:
                    type: array
                    items:
                      type: object
                      properties:
                        liquidationId:
                          type: integer
                          format: int64
                          example: 56
                          description: Risk unit liquidation unique identifier.
                          x-description-cn: 唯一风险单位强制平仓标识符。
                        liquidationTransferRecord:
                          type: array
                          description: List of transfer records related to the liquidationId.
                          x-description-cn: 与 liquidationId 相关的划转记录列表。
                          items:
                            type: object
                            properties:
                              transferTime:
                                type: integer
                                format: int64
                                example: 1765378400855
                                description: Timestamp of the transfer event.
                                x-description-cn: 划转时间戳。
                              fromUid:
                                type: string
                                example: "1000277033525"
                                description: UID of the account transferring assets.
                                x-description-cn: 划出资产账号 UID。
                              fromAccountType:
                                type: string
                                example: PORTFOLIO_MARGIN
                                description: SPOT or PORTFOLIO_MARGIN or CROSS_MARGIN.
                                x-description-cn: 账户类型：SPOT、PORTFOLIO_MARGIN 或 CROSS_MARGIN。
                              toUid:
                                type: string
                                example: "1000277033505"
                                description: UID of the account receiving assets.
                                x-description-cn: 接收资产账号 UID。
                              toAccountType:
                                type: string
                                example: PORTFOLIO_MARGIN
                                description: SPOT or PORTFOLIO_MARGIN or CROSS_MARGIN.
                                x-description-cn: 账户类型：SPOT、PORTFOLIO_MARGIN 或 CROSS_MARGIN。
                              status:
                                type: string
                                example: CONFIRM
                                description: Current transfer status.
                                x-description-cn: 当前划转状态。
                              assets:
                                type: array
                                description: Transferred asset list.
                                x-description-cn: 划转资产列表。
                                items:
                                  type: object
                                  properties:
                                    assetName:
                                      type: string
                                      example: USDT
                                      description: Name of the transferred token.
                                      x-description-cn: 划转资产名称。
                                    amount:
                                      type: string
                                      example: "17750.6316"
                                      description: Amount of the transferred token.
                                      x-description-cn: 划转资产金额。
  /sapi/v1/margin/loan-group/transfer-out:
    post:
      summary: Risk Unit Transfer (TRADE)
      x-summary-cn: 风险单位资金划转 (TRADE)
      description: >-
        When specified risk unit LTV thresholds and/or the relevant product transfer out rules are met, the Risk Unit
        Transfer API allows users to perform the following:


        Transfer of assets from margin collateral/credit accounts to spot accounts with the same Spot UID. This endpoint
        is accessible via each of the credit/collateral accounts with its API Key or parent account .

        Please Note: To transfer funds out of the Institutional Loan Risk Unit, first transfer to the spot wallet using
        the dedicated Risk Unit Transfer API. After that, use the Universal Transfer API to move the assets to an
        account outside of the risk unit.


        For all other designated use cases shown below, please use the Universal Transfer API.


        Transfer assets between Credit Account and other Margin Collateral Accounts within the risk unit without LTV
        restrictions. Please see Universal Transfer API, this needs to be done via master account API key.

        Transfers between Spot collateral account and accounts outside of the risk unit.
      x-description-cn: |-
        当达到特定的风险单位 LTV 阈值和/或相关产品的转出规则时，风险单位资金划转 API 允许用户执行以下操作：

        将资产从杠杆抵押账户或放贷账户转至相同现货 UID 下的现货账户，此接口可支持单个抵押账户或放贷账户调用，也可由母账户调用。
        请注意：要将资金转出机构借贷风险单位，首先要使用机构借贷特定的转账 API 将资金转入现货钱包。然后，使用万向转账 API 将资产转移到风险单元之外的账户。

        此外的划转场景，请您使用万向转账 API 操作。

        资金在放贷账户与风险单位内其他杠杆抵押账户之间划转，此划转不受转出 LTV 的限制，此接口需要通过母账户 API Key 操作。
        现货账户与风险单位外的账户之间转账。
      tags:
        - transfer
      operationId: riskUnitTransfer
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/transfer#risk-unit-transfer
      x-ip-weight: 1000
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
                - asset
                - amount
                - timestamp
              properties:
                subEmail:
                  type: string
                  example: collateral001@test.com
                  description: |-
                    When the parent account calls this endpoint, the subEmail field is mandatory. If left empty, error
                    code -27026 will be returned.<br/>When a credit or collateral account calls this endpoint, the
                    subEmail field may be omitted and will default to the account's own subEmail.<br/>If the wrong
                    subEmail is inputted, error code -3003 will be returned.
                  x-description-cn: 抵押子账户或放贷子账户的邮箱地址<br/>母账户调用该接口时，subEmail必填，为空则报错；<br/>放贷账户或抵押账户调用该接口时，subEmail可为空，默认为其本身subEmail.
                asset:
                  type: string
                  example: USDT
                  description: Asset name, for example USDT or USDC
                  x-description-cn: 资产名称，例如 USDT 或 USDC
                amount:
                  type: number
                  format: float
                  example: 1000.5
                  description: >-
                    Transfer amount of the asset. The real transferred amount = min(risk unit max transfer amount,
                    collateral account max transfer amount).
                  x-description-cn: 转出金额。 注意 实际可转出金额取值于 min(风险单位最大可转出金额, 抵押账号最大可转出金额)， 两者取小。
                recvWindow:
                  type: integer
                  format: int64
                  example: 5000
                  maximum: 60000
                  description: Request validity window in milliseconds.
                  x-description-cn: 请求有效时间窗口，单位为毫秒。
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
          description: Risk Unit Transfer Out Submitted
          x-description-cn: 风险单位资金划转已提交
```