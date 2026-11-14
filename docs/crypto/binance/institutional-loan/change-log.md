---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/institutional-loan/change-log
api_type: REST
updated_at: 2026-11-13 20:31:21.946327
---

# Change Log

## 2026-09-24

  * **GET /sapi/v1/margin/loan-group/ltv-details** : documented the response fields `leverageTier`, `initialLtv`, `marginCallLtv`, `liquidationLtv`, `liquidationExitLtv`, `maxTransferOutLtv` and `transferOutLtv`. These fields are already returned by the endpoint; there is no change to endpoint behaviour. `transferOutLtv` is the LTV used for transfer-out checks and excludes collateral in Spot wallets.



## 2026-06-23

  * New endpoint **GET /sapi/v1/margin/loan-group/max-borrowable** : Query the maximum borrowable amount of a given asset for an institutional loan risk unit. Accessible from either the parent account or the credit account API key.



## 2025-12-26

### Time-sensitive Notice

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/en/docs/products/institutional-loan/error-code#-1022-invalid_signature). Please review and update your signing logic accordingly.



### REST API

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/en/docs/products/institutional-loan/general-info#signed-endpoint-examples-for-post-apiv3order).



## 2025-12-16

  * 1 new endpoint has been released for the Risk Unit , as well as 1 key parameters added into the LTV detail response sample.
    * GET /sapi/v1/margin/loan-group/liquidation-transfer-record: New endpoint . Query the institution loan risk unit transfer records during forced liquidation. More detail see the API description below.
    * GET /sapi/v1/margin/loan-group/borrow-repay : Normal Repayment and Repayment from forced liquidation can be shown on the response.



## 2025-08-20

  * Update 2 endpoints as below：
    * POST /sapi/v1/margin/loan-group/repay : Description updated about the real repaid amount = min(available amount in account, input repay amount) .
    * POST /v1/margin/loan-group/transfer-out: Description updated about the real transferred amount = min(risk unit max transfer amount, collateral account max transfer amount).



## 2025-08-01

  * Update 4 endpoints as below:
    * GET /sapi/v1/margin/loan-group/borrow-repay : support historical risk unit query
    * GET /sapi/v1/margin/loan-group/interest-history : support historical risk unit query
    * GET /sapi/v1/margin/loan-group/force-liquidation : support historical risk unit query with specific groupId
    * POST /v1/margin/loan-group/transfer-out : support parent account to transfer the asset with the specific subEmail
  * Add new endpoint as below
    * GET /sapi/v1/margin/loan-groups/closed ：Query closed risk unit record by credit account



## 2025-07-11

  * 3 new endpoints have been released for the Risk Unit , as well as 3 key parameters added into the LTV detail response example.:
    * New endpoint **GET /sapi/v1/margin/loan-group/borrow-repay** : Get borrow/repay records in the Institution Loan Risk Unit. This endpoint is accessible only with the credit account API key.
    * New endpoint **GET /sapi/v1/margin/loan-group/force-liquidation** : Get Institution Loan Risk Unit Force Liquidation Record. This endpoint is accessible only with the credit account API key.
    * New endpoint **POST /v1/margin/loan-group/transfer-out** : The risk unit endpoint allows users to perform transfer of assets under specific rules . More detail see the API description below.
    * **GET /sapi/v1/margin/loan-group/ltv-details** : parentAccountFrozenAmount, maxTransferOutAmount , maxAllowedBorrowLimit added into response Example.



## 2025-06-20

  * 6 endpoints now are released in Institutional Loan :
    * **DELETE /sapi/v1/margin/loan-group** : Close Institution Loan Group, can only operate by credit account.
    * **POST /sapi/v1/margin/loan-group/edit-member** : Add or unlink collateral accounts from a Risk Unit Group. Edit should be made by the parent account.
    * **GET /sapi/v1/margin/loan-groups/activated** : Query Activated Institution Loan Risk Unit Groups List.
    * **POST /sapi/v1/margin/loan-group/repay** : Institution Loan Group Repay
    * **POST /sapi/v1/margin/loan-group/borrow** : Institution Loan Risk Unit Group Borrow
    * **GET /sapi/v1/margin/loan-group/interest-history** : Query Institution Loan Risk Unit Interest History.



## 2025-06-16

  * The endpoint of LTV query now is released in Institutional Loan :
    * **GET`/sapi/v1/margin/loan-group/ltv-details`** : Parent account and credit account can use this endpoint to query group loan ltv detail information with groupId



## 2025-05-16

  * Binance Margin offers institutional loan with the SAPI support loan detail information query on the first version.

The endpoint below is available :

    * **GET /sapi/v1/margin/loan-groups ** : Parent account can use this endpoint to query group loan detail information with groupId
    * **GET /sapi/v1/margin/loan-group **: Only credit account can use this endpoint to query its own group loan detail information.



Was this page helpful?

Last modified on November 12, 2026

[Introduction](/en/docs/products/institutional-loan/Introduction)[Public API Definitions](/en/docs/products/institutional-loan/common-definition)

---

# 更新日志

## 2026-09-24

  * **GET /sapi/v1/margin/loan-group/ltv-details** ：补充响应字段说明 `leverageTier`、`initialLtv`、 `marginCallLtv`、`liquidationLtv`、`liquidationExitLtv`、`maxTransferOutLtv` 及 `transferOutLtv`。上述字段已在接口中返回，接口行为无变化。`transferOutLtv` 为划出校验所使用的 LTV，不计入现货钱包中的抵押品。



## 2026-06-23

  * 新接口 **GET /sapi/v1/margin/loan-group/max-borrowable** :查询机构借贷风险单位内指定币种的最大可借金额。可使用母账户或放贷账户的API Key 访问。



## 2025-12-26

### 时效性通知

  * **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** 调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/zh-CN/docs/products/institutional-loan/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。



### REST API

  * 更新了 REST API 文档中有关于 [签名请求示例](/zh-CN/docs/products/institutional-loan/general-info#post-apiv3order-%E7%9A%84%E7%AD%BE%E5%90%8D%E7%A4%BA%E4%BE%8B) 的部分。



## 2025-12-16

  * 新增一个接口，并更新一个接口参数，详细如下：
    * GET /sapi/v1/margin/loan-group/liquidation-transfer-record: 新增接口，提供风险单位在强平时的划转记录查询，更多详情请参考接口描述。
    * GET /sapi/v1/margin/loan-group/borrow-repay : 在响应示例中，可返回"Type" 为“NORMAL_REPAY” 和 "FORCE_REPAY" 的查询结果。



## 2025-08-20

  * 更新以下2个接口：
    * POST /sapi/v1/margin/loan-group/repay : 添加备注，说明实际还款金额 取值于 min(账户实际可还款金额, 输入的金额)，两者取小。
    * POST /v1/margin/loan-group/transfer-out: 添加备注，说明实际可转出金额取值于 min(风险单位最大可转出金额, 抵押账号最大可转出金额)， 两者取小。



## 2025-08-01

  * 更新以下4个接口：
    * GET /sapi/v1/margin/loan-group/borrow-repay : 支持查询历史风险单位
    * GET /sapi/v1/margin/loan-group/interest-history : 支持查询历史风险单位
    * GET /sapi/v1/margin/loan-group/force-liquidation :支持查询历史风险单位
    * POST /v1/margin/loan-group/transfer-out : 支持母账户根据给定的子账号邮箱地址划转资金
  * 新增以下一个接口
    * GET /sapi/v1/margin/loan-groups/closed ：支持放贷账户查询历史风险单位



## 2025-07-11

  * 机构贷新增3个接口，同时机构贷详情查询接口新增3个返回参数。具体如下:
    * 新接口 **GET /sapi/v1/margin/loan-group/borrow-repay** : 查询机构贷借贷/还款记录，该接口仅供信用账户调用。
    * 新接口 **GET /sapi/v1/margin/loan-group/force-liquidation** : 查询机构贷强制平仓记录，该接口仅供信用账户调用。
    * 新接口 **POST /v1/margin/loan-group/transfer-out** : 该接口允许用户在特定条件下从划转资金到现货账户，详情可参考接口说明。
    * **GET /sapi/v1/margin/loan-group/ltv-details** : 详情查询接口新增以下3个返回参数，parentAccountFrozenAmount, maxTransferOutAmount , maxAllowedBorrowLimit 。



## 2025-06-20

  * 机构贷新增以下6个接口 :
    * **DELETE /sapi/v1/margin/loan-group** : 关闭机构贷风险单位，仅支持由放贷子账户操作。
    * **POST /sapi/v1/margin/loan-group/edit-member** : 添加或删除抵押子账户至风险单位内，仅支持通过母账户操作修改。
    * **GET /sapi/v1/margin/loan-groups/activated** : 查询生效状态的机构贷风险单位列表。
    * **POST /sapi/v1/margin/loan-group/repay** : 机构贷风险单位还款
    * **POST /sapi/v1/margin/loan-group/borrow** : 机构贷风险单位借款
    * **GET /sapi/v1/margin/loan-group/interest-history** : 查询机构贷风险单位给定时间段内的利息历史记录。



## 2025-06-16

  * 机构贷更新以下查询接口 :
    * **GET`/sapi/v1/margin/loan-group/ltv-details`** : 母账户和信用账户可根据groupId查询ltv详细信息。



## 2025-05-16

  * 币安杠杆交易为VIP5及以上的用户提供了机构贷信用额度产品。该产品当前发布第一版本，并提供以下查询接口：
    * **GET /sapi/v1/margin/loan-groups ** : 母账户可通过该接口获取指定groupId的机构贷详情。
    * **GET /sapi/v1/margin/loan-group **: 信用账户可通过该接口获取所在结构贷详情。



此页面是否有帮助？

Last modified on November 12, 2026

[概述](/zh-CN/docs/products/institutional-loan/Introduction)[公开 API 参数](/zh-CN/docs/products/institutional-loan/common-definition)