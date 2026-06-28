---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/change-log
api_type: Account
updated_at: 2026-05-27 19:02:47.864304
---

# Change Log

## 2025-12-26[​](/docs/sub_account/change-log#2025-12-26 "Direct link to 2025-12-26")

### Time-sensitive Notice[​](/docs/sub_account/change-log#time-sensitive-notice "Direct link to Time-sensitive Notice")

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:**   
When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/docs/sub_account/error-code#-1022-invalid_signature). Please review and update your signing logic accordingly.



### REST API[​](/docs/sub_account/change-log#rest-api "Direct link to REST API")

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/docs/sub_account/general-info#signed-endpoint-examples-for-post-apiv3order).



* * *

## 2025-09-17[​](/docs/sub_account/change-log#2025-09-17 "Direct link to 2025-09-17")

  * Update GET `/sapi/v1/sub-account/transaction-statistics` endpoints.
  * Supports returning the transaction information of the master account by default (without sending the email parameter)



* * *

## 2025-06-03[​](/docs/sub_account/change-log#2025-06-03 "Direct link to 2025-06-03")

  * Remove POST `/sapi/v1/sub-account/blvt/enable` and POST `/sapi/v1/sub-account/margin/enable` endpoints.
  * User now should make the initial transfer in the Margin account to enable it.



* * *

## 2025-04-30[​](/docs/sub_account/change-log#2025-04-30 "Direct link to 2025-04-30")

  * Update universal transfer endpoints for Sub-Account: `POST /sapi/v1/sub-account/universalTransfer ` to accept 'ALPHA' to 'ALPHA' transfer.



* * *

## 2025-04-08[​](/docs/sub_account/change-log#2025-04-08 "Direct link to 2025-04-08")

  * Update the weight of endpoints for Sub-Account: 
    * The UID request weight of `POST /sapi/v1/sub-account/universalTransfer ` is 360.



* * *

## 2025-03-26[​](/docs/sub_account/change-log#2025-03-26 "Direct link to 2025-03-26")

  *     * New endpoints for Sub-Account to support move position function：
    * `POST /sapi/v1/sub-account/futures/move-position`: Move position between sub-master, master-sub, or sub-sub accounts
    * `GET /sapi/v1/sub-account/futures/move-position`: Query move position history



## 2024-11-22[​](/docs/sub_account/change-log#2024-11-22 "Direct link to 2024-11-22")

  * Update endpoints for Managed Sub-Account: 
    * GET `/sapi/v1/managed-subaccount/marginAsset`: Add a new request parameter to determine which margin account type is queried.
    * GET `/sapi/v1/managed-subaccount/fetch-future-asset`: Add a new request parameter to determine which futures account type is queried.



* * *

## 2024-11-04[​](/docs/sub_account/change-log#2024-11-04 "Direct link to 2024-11-04")

  * Update endpoints for Sub-Account: 
    * `GET /sapi/v1/sub-account/universalTransfer`: The query time period must be less then 7 days. If startTime and endTime not sent, return records of the last 7 days by default.



* * *

## 2024-10-24[​](/docs/sub_account/change-log#2024-10-24 "Direct link to 2024-10-24")

  * Update endpoints for Sub-Account: 
    * `GET /sapi/v4/sub-account/assets ` and `GET /sapi/v3/sub-account/assets`: Add 2 new asset types to the response.



* * *

## 2024-05-21[​](/docs/sub_account/change-log#2024-05-21 "Direct link to 2024-05-21")

  * Update endpoints for Sub-Account: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`: update response field `fromAccountType` and `toAccountType`. Return USDT_FUTURE/COIN_FUTURE in order to differentiate 2 futures wallets.



* * *

## 2023-06-22[​](/docs/sub_account/change-log#2023-06-22 "Direct link to 2023-06-22")

  * New endpoints for Sub-Account: 
    * `POST /sapi/v1/sub-account/eoptions/enable`: enable Options for Sub-account
    * `GET /sapi/v1/managed-subaccount/query-trans-log`: Query Managed Sub Account Transfer Log (For Trading Team Sub Account)



* * *

## 2023-04-20[​](/docs/sub_account/change-log#2023-04-20 "Direct link to 2023-04-20")

  * New endpoints for Sub-Account： 
    * `GET /sapi/v1/managed-subaccount/deposit/address`: get managed sub-account deposit address



* * *

## 2023-03-23[​](/docs/sub_account/change-log#2023-03-23 "Direct link to 2023-03-23")

  * Update endpoints for Sub-Account: 
    * `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: Add response field `tranId`
    * `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: Add response field `tranId`
  * New endpoints for Sub-Account: 
    * `GET /sapi/v1/managed-subaccount/info`: query investor's managed sub-account list
    * `GET /sapi/v1/sub-account/transaction-statistics`: Query sub-account transaction tatistics



* * *

## 2023-02-13[​](/docs/sub_account/change-log#2023-02-13 "Direct link to 2023-02-13")

  * New endpoints for Sub-Account: 
    * `GET /sapi/v4/sub-account/assets`: Fetch sub-account assets



* * *

## 2023-01-13[​](/docs/sub_account/change-log#2023-01-13 "Direct link to 2023-01-13")

  * The following endpoints will be discontinued on January 13, 2023 6:00 AM UTC: 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and disable IP restriction for a sub-account API Key
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP list for a sub-account API Key
  * New endpoints for Sub-Account: 
    * `GET /sapi/v1/managed-subaccount/fetch-future-asset`: Investor can use this api to query managed sub account futures asset details
    * `GET /sapi/v1/managed-subaccount/marginAsset`: Investor can use this api to query managed sub account margin asset details
  * New endpoin for Margin: 
    * `GET /sapi/v1/margin/crossMarginCollateralRatio`: Get cross margin collateral ratio



* * *

## 2023-01-05[​](/docs/sub_account/change-log#2023-01-05 "Direct link to 2023-01-05")

  * New endpoints for Sub-Account: 
    * `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: Investor can use this api to query managed sub account transfer log
    * `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: Trading team can use this api to query managed sub account transfer log



* * *

## 2022-11-18[​](/docs/sub_account/change-log#2022-11-18 "Direct link to 2022-11-18")

  * New endpoints for Sub-account: 
    * `POST /sapi/v2/sub-account/subAccountApi/ipRestriction`: To support master account update IP Restriction for Sub-Account API key



* * *

## 2022-09-22[​](/docs/sub_account/change-log#2022-09-22 "Direct link to 2022-09-22")

  * Update endpoint for Sub-Account: 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction`: Add new param `thirdParty`
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`: Add new param `thirdPartyName`
    * `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`: Add new param `thirdPartyName`



* * *

## 2022-09-12[​](/docs/sub_account/change-log#2022-09-12 "Direct link to 2022-09-12")

  * Update endpoint for Sub-account: * `GET /sapi/v1/sub-account/subAccountApi/ipRestriction`: To support master account query Third party IP list name for a sub account API key



* * *

## 2022-06-02[​](/docs/sub_account/change-log#2022-06-02 "Direct link to 2022-06-02")

  * Update endpoint for Subaccount: 
    * `GET /sapi/v1/sub-account/sub/transfer/history`: fromEmail and toEmail can be master email.



* * *

## 2022-3-29[​](/docs/sub_account/change-log#2022-3-29 "Direct link to 2022-3-29")

The following updates will take effect on **March 31, 2022 08:00 AM UTC**

  * Update endpoint for Sub-account： 
    * `GET /sapi/v1/sub-account/universalTransfer`



The query time period must be less then 30 days; If `startTime` and `endTime` not sent, return records of the last 30 days by default

* * *

## 2022-03-25[​](/docs/sub_account/change-log#2022-03-25 "Direct link to 2022-03-25")

  * Update endpoint for Sub-Account: 
    * New endpoint`GET /sapi/v1/managed-subaccount/accountSnapshot` to support investor master account query asset snapshot of managed sub-account



* * *

## 2022-03-08[​](/docs/sub_account/change-log#2022-03-08 "Direct link to 2022-03-08")

  * Update endpoint for Sub-Account: 
    * New transfer types`MARGIN`,`ISOLATED_MARGIN` and parameter`symbol`added in`POST /sapi/v1/sub-account/universalTransfer` to support transfer to sub-account cross margin account and isolated margin account



* * *

## 2022-2-18[​](/docs/sub_account/change-log#2022-2-18 "Direct link to 2022-2-18")

  * Update endpoint for Sub-Account: 
    * New fields `isManagedSubAccount`and `isAssetManagementSubAccount` added in`GET /sapi/v1/sub-account/list`to support query whether the sub-account is a managed sub-account or a asset management sub-account



* * *

## 2021-12-24[​](/docs/sub_account/change-log#2021-12-24 "Direct link to 2021-12-24")

  * Update endpoints for Sub-Account: 
    * New parameter`clientTranId`added in`POST /sapi/v1/sub-account/universalTransfer` and `GET /sapi/v1/sub-account/universalTransfer` to support custom transfer id



* * *

## 2021-11-16[​](/docs/sub_account/change-log#2021-11-16 "Direct link to 2021-11-16")

  * New endpoints for Sub-Account: 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and disable IP whitelist for a sub-account API Key
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP Whitelist Address List for a sub-account API Key
    * `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account query IP whitelist for a sub-account API Key
    * `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account delete IP Whitelist Address List for a sub-account API Key



* * *

## 2021-07-29[​](/docs/sub_account/change-log#2021-07-29 "Direct link to 2021-07-29")

  * Update endpoint for Sub-Account: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory` if `startTime`and`endTime`are not sent, the recent 30-day data will be returned by default



* * *

## 2021-06-15[​](/docs/sub_account/change-log#2021-06-15 "Direct link to 2021-06-15")

  * New endpoints for Sub-Account: 
    * `POST /sapi/v1/managed-subaccount/deposit ` to deposit assets into the managed sub-account (only for investor master account)
    * `GET /sapi/v1/managed-subaccount/asset` to query managed sub-account asset details (only for investor master account)
    * `POST /sapi/v1/managed-subaccount/withdraw` to withdrawal assets from the managed sub-account (only for investor master account)



* * *

## 2021-04-08[​](/docs/sub_account/change-log#2021-04-08 "Direct link to 2021-04-08")

  * Update endpoint for Sub-Account: 
    * `GET /sapi/v1/sub-account/futures/accountSummary` and `GET /sapi/v2/sub-account/futures/accountSummary` the unit of field `asset` changed to USD valued summary of sub-account assets



* * *

## 2021-04-02[​](/docs/sub_account/change-log#2021-04-02 "Direct link to 2021-04-02")

  * New endpoint for Sub-Account: 
    * `GET /sapi/v3/sub-account/assets` to query sub-account assets



* * *

## 2021-04-01[​](/docs/sub_account/change-log#2021-04-01 "Direct link to 2021-04-01")

  * Update endpoint for Sub-Account: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory` new fields `fromAccountType` and `toAccountType` added in response



* * *

## 2021-03-31[​](/docs/sub_account/change-log#2021-03-31 "Direct link to 2021-03-31")

  * Update endpoint for Sub-Account: 
    * `GET /wapi/v3/sub-account/transfer/history.html` added new parameters `fromEmail` and `toEmail`, the original parameter`email` is equal to`fromEmail`by default



* * *

## 2021-03-08[​](/docs/sub_account/change-log#2021-03-08 "Direct link to 2021-03-08")

  * New endpoint for Sub-Account: 
    * `POST /sapi/v1/sub-account/virtualSubAccount` to support create a virtual sub-account
    * `GET /sapi/v1/sub-account/list` to support query sub-account list
    * `POST /sapi/v1/sub-account/blvt/enable` to support enable blvt for sub-account



* * *

## 2020-12-22[​](/docs/sub_account/change-log#2020-12-22 "Direct link to 2020-12-22")

  * New endpoint for Sub-Account: 
    * `GET /sapi/v1/sub-account/sub/transfer/history` to get spot asset transfer history.



* * *

## 2020-12-02[​](/docs/sub_account/change-log#2020-12-02 "Direct link to 2020-12-02")

  * New endpoints for Sub-Account: 
    * `GET /sapi/v2/sub-account/futures/account` to get detail on sub-account's USDT margined futures account and COIN margined futures account.
    * `GET /sapi/v2/sub-account/futures/accountSummary` to get summary of sub-account's USDT margined futures account and COIN margined futures account.
    * `GET /sapi/v2/sub-account/futures/positionRisk` to get position risk of sub-account's USDT margined futures account and COIN margined futures account.



* * *

## 2020-11-13[​](/docs/sub_account/change-log#2020-11-13 "Direct link to 2020-11-13")

  * New endpoints for Sub-Account: 
    * `POST /sapi/v1/sub-account/universalTransfer` to transfer spot and futures asset between master account and sub accounts.
    * `GET /sapi/v1/sub-account/universalTransfer` to search transfer records.



* * *

## 2020-11-09[​](/docs/sub_account/change-log#2020-11-09 "Direct link to 2020-11-09")

  * New field `tranId` is available from endpoints: 
    * `GET /sapi/v1/sub-account/futures/internalTransfer`
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`



* * *

## 2020-10-10[​](/docs/sub_account/change-log#2020-10-10 "Direct link to 2020-10-10")

  * New `type` added in the endpoint `POST /sapi/v1/sub-account/futures/transfer`to support transfer asset from subaccount's spot account to its COIN-margined futures account and transfer asset from subaccount's COIN-margined futures account to its spot account.



* * *

## 2020-09-03[​](/docs/sub_account/change-log#2020-09-03 "Direct link to 2020-09-03")

  * New endpoint `POST /sapi/v1/sub-account/futures/internalTransfer` to transfer futures asset between master account and subaccount.
  * New endpoint`GET /sapi/v1/sub-account/futures/internalTransfer` to get futures transfer history of subaccount.



* * *

## 2020-09-01[​](/docs/sub_account/change-log#2020-09-01 "Direct link to 2020-09-01")

  * New parameter `masterAccountTotalAsset` added in the endpoint `GET /sapi/v1/sub-account/spotSummary` to get BTC valued asset summary of master account.



* * *

## 2020-08-27[​](/docs/sub_account/change-log#2020-08-27 "Direct link to 2020-08-27")

  * New endpoint `GET /sapi/v1/sub-account/spotSummary` to get BTC valued asset summary of subaccout.



* * *

## 2020-02-05[​](/docs/sub_account/change-log#2020-02-05 "Direct link to 2020-02-05")

  * New sub account endpoints: 
    * `POST /sapi/v1/sub-account/futures/transfer` to transfer between futures and spot accout of sub-account.
    * `POST /sapi/v1/sub-account/margin/transfer` to transfer between margin and spot accout of sub-account.
    * `POST /sapi/v1/sub-account/transfer/subToSub` to transfer to another account by sub-account.
    * `POST /sapi/v1/sub-account/transfer/subToMaster` to transfer to same master by sub-account.
    * `GET /sapi/v1/sub-account/transfer/subUserHistory` to get transfer history of sub-account.



* * *

## 2019-11-19[​](/docs/sub_account/change-log#2019-11-19 "Direct link to 2019-11-19")

  * `GET /sapi/v1/sub-account/margin/account` has new field: `marginTradeCoeffVo` which contains 
    * `forceLiquidationBar` for liquidation margin ratio
    * `marginCallBar` for margin call margin ratio
    * `normalBar` for initial margin ratio



* * *

## 2019-11-08[​](/docs/sub_account/change-log#2019-11-08 "Direct link to 2019-11-08")

  * New sapi for subaccount management on margin and futures: 
    * `GET /sapi/v1/sub-account/status (HMAC SHA256)`
    * `POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/margin/account (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)`
    * `POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/futures/account (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)`



* * *

## 2019-11-04[​](/docs/sub_account/change-log#2019-11-04 "Direct link to 2019-11-04")

  * New sapi endpoints for subaccount wallet. 
    * `GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256))`: fetch subaccount deposit address.
    * `GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256))`: fetch subaccount deposit history.

---

# 更新日志

## 2025-12-26[​](/docs/zh-CN/sub_account/change-log#2025-12-26 "2025-12-26的直接链接")

### 时效性通知[​](/docs/zh-CN/sub_account/change-log#时效性通知 "时效性通知的直接链接")

  * **以下有关于REST API变更将在 2026-01-15 07:OO UTC 发生:**   
调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/docs/zh-CN/sub_account/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。



### REST API[​](/docs/zh-CN/sub_account/change-log#rest-api "REST API的直接链接")

  * 更新了 REST API 文档中有关于 [签名请求示例](/docs/zh-CN/sub_account/general-info#post-apiv3order-%E7%9A%84%E7%AD%BE%E5%90%8D%E7%A4%BA%E4%BE%8B) 的部分。



* * *

## 2025-09-17[​](/docs/zh-CN/sub_account/change-log#2025-09-17 "2025-09-17的直接链接")

  * 更新 GET `/sapi/v1/sub-account/transaction-statistics` 接口
  * 支持默认返回母账户的交易信息（不发送email参数）



* * *

## 2025-06-03[​](/docs/zh-CN/sub_account/change-log#2025-06-03 "2025-06-03的直接链接")

  * 移除 POST `/sapi/v1/sub-account/blvt/enable` 与 POST `/sapi/v1/sub-account/margin/enable` 接口。
  * 用户可划入首笔资金开启杠杆帐户。



* * *

## 2025-04-30[​](/docs/zh-CN/sub_account/change-log#2025-04-30 "2025-04-30的直接链接")

  * 更新子母账户划转接口:`POST /sapi/v1/sub-account/universalTransfer `支持`ALPHA` 划转到 `ALPHA` (无论母账户或子账户)。



* * *

## 2025-04-08[​](/docs/zh-CN/sub_account/change-log#2025-04-08 "2025-04-08的直接链接")

  * 更新子母账户接口请求权重(UID): 
    * `POST /sapi/v1/sub-account/universalTransfer `请求权重(UID)更新為360。



* * *

## 2025-03-26[​](/docs/zh-CN/sub_account/change-log#2025-03-26 "2025-03-26的直接链接")

  * 新增子母账户移仓接口： 
    * `POST /sapi/v1/sub-account/futures/move-position`: 支持母账户和子账户，子账户和子账户的移仓
    * `GET /sapi/v1/sub-account/futures/move-position`: 获取账户移仓历史记录



## 2024-11-22[​](/docs/zh-CN/sub_account/change-log#2024-11-22 "2024-11-22的直接链接")

  * 更新託管子母账户接口： 
    * GET `/sapi/v1/managed-subaccount/marginAsset`: 添加新的入参判定请求的杠杆帐户类型。
    * GET `/sapi/v1/managed-subaccount/fetch-future-asset`: 添加新的入参判定请求的期货帐户类型。



* * *

## 2024-11-04[​](/docs/zh-CN/sub_account/change-log#2024-11-04 "2024-11-04的直接链接")

  * 更新子母账户接口： 
    * `GET /sapi/v1/sub-account/universalTransfer `: 若 startTime 和 endTime 都未传，则只可查询最近7天的记录。查询时间范围最大不得超过7天。



* * *

## 2024-10-24[​](/docs/zh-CN/sub_account/change-log#2024-10-24 "2024-10-24的直接链接")

  * 更新子母账户接口： 
    * `GET /sapi/v4/sub-account/assets ` 及 `GET /sapi/v3/sub-account/assets`: 新增 2 种资产类型



* * *

## 2024-05-21[​](/docs/zh-CN/sub_account/change-log#2024-05-21 "2024-05-21的直接��链接")

  * 更新子母账户接口： 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`: 更新返回字段`fromAccountType`和 `toAccountType`. 合约钱包划转时返回USDT_FUTURE/COIN_FUTURE以区分钱包



* * *

## 2023-04-20[​](/docs/zh-CN/sub_account/change-log#2023-04-20 "2023-04-20的直接链接")

  * 新增子母账户接口： 
    * `GET /sapi/v1/managed-subaccount/deposit/address`：支持获取投资人之托管子账户充值地址



* * *

## 2023-03-23[​](/docs/zh-CN/sub_account/change-log#2023-03-23 "2023-03-23的直接链接")

  * 更新子母账户接口: 
    * `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: 响应出参增加字段`tranId`
    * `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: 响应出参增加字段`tranId`
  * 添加子母账户接口: 
    * `GET /sapi/v1/managed-subaccount/info`: 查询托管子账户列表
    * `GET /sapi/v1/sub-account/transaction-statistics`: 查询子账户交易量统计列表



* * *

## 2023-02-13[​](/docs/zh-CN/sub_account/change-log#2023-02-13 "2023-02-13的直接链接")

  * 添加子母账户接口: 
    * `GET /sapi/v4/sub-account/assets`: 查询子账户资产



* * *

## 2023-01-13[​](/docs/zh-CN/sub_account/change-log#2023-01-13 "2023-01-13的直接链接")

  * 以下接口将于 1 月 13, 2023 6:00 AM UTC 停止使用： 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` 以支持母账户为子账户 API Key 开启或关闭 IP 白名单
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` 以支持母账户为子账户 API Key 添加 IP 白名单地址列表
  * 添加子母账户接口： 
    * `GET /sapi/v1/managed-subaccount/fetch-future-asset`: Investor can use this api to query managed sub account futures asset details
    * `GET /sapi/v1/managed-subaccount/marginAsset`: Investor can use this api to query managed sub account margin asset details



* * *

## 2023-01-05[​](/docs/zh-CN/sub_account/change-log#2023-01-05 "2023-01-05的直接链接")

  * 添加子母账户接口: 
    * `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: 投资人可以根据此接口查询其托管子账户划转记录
    * `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: 交易团队可以根据此接口查询其托管子账户划转记录



* * *

## 2022-11-18[​](/docs/zh-CN/sub_account/change-log#2022-11-18 "2022-11-18的直接链接")

  * 新增子母账户接口: 
    * `POST /sapi/v2/sub-account/subAccountApi/ipRestriction`: 为子账户 API Key 更新 IP 白名单



* * *

## 2022-09-22[​](/docs/zh-CN/sub_account/change-log#2022-09-22 "2022-09-22的直接链接")

  * 更新子母账户接口： 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction`：添加一个新的参数 `thirdParty`
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`：添加一个新的参数 `thirdPartyName`
    * `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`：添加一个新的参数 `thirdPartyName`



* * *

## 2022-09-12[​](/docs/zh-CN/sub_account/change-log#2022-09-12 "2022-09-12的直接链接")

  * 更新子母账户接口： * `GET /sapi/v1/sub-account/subAccountApi/ipRestriction`： 以支持母账户为子账户 API Key 查询三方 IP 白名单



* * *

## 2022-06-02[​](/docs/zh-CN/sub_account/change-log#2022-06-02 "2022-06-02的直接链接")

  * 更新子母账户接口: 
    * `GET /sapi/v1/sub-account/sub/transfer/history`：fromEmail 及 toEmail 可以是母账户 email。



* * *

## 2022-3-29[​](/docs/zh-CN/sub_account/change-log#2022-3-29 "2022-3-29的直接链接")

以下更新于**3 月 31, 2022 08:00 AM UTC** 生效

  * 更新子母账户接口： 
    * `GET /sapi/v1/sub-account/universalTransfer`



接口查询时间窗口缩短为 30 天；若`startTime`和`endTime`没传，则默认返回最近 30 天数据。

* * *

## 2022-03-25[​](/docs/zh-CN/sub_account/change-log#2022-03-25 "2022-03-25的直接链接")

  * 更新子母账户接口: 
    * 新增接口 `GET /sapi/v1/managed-subaccount/accountSnapshot`以支持投资人母账户查询托管子账户资产快照



* * *

## 2022-03-08[​](/docs/zh-CN/sub_account/change-log#2022-03-08 "2022-03-08的直接链接")

  * 更新子母账户接口: 
    * 新增划转类型`MARGIN `,`ISOLATED_MARGIN `以及传参`symbol`于子母账户万能划转接口`POST /sapi/v1/sub-account/universalTransfer` 以支持母账户现货账户划转到子账户杠杆全仓账户和杠杆逐仓账户



* * *

## 2022-2-18[​](/docs/zh-CN/sub_account/change-log#2022-2-18 "2022-2-18的直接链接")

  * 更新子母账户接口: 
    * 新增响应参数 `isManagedSubAccount`和 `isAssetManagementSubAccount` 于接口 `GET /sapi/v1/sub-account/list` 以支持查询子账户是否是托管子账户或资产管理子账户



* * *

## 2021-12-24[​](/docs/zh-CN/sub_account/change-log#2021-12-24 "2021-12-24的直接链接")

  * 更新子母账户接口: 
    * 新增传参`clientTranId`于子母账户万能划转接口`POST /sapi/v1/sub-account/universalTransfer` 和查询子母账户万能划转历史接口 `GET /sapi/v1/sub-account/universalTransfer` 以支持用户自定义划转 id



* * *

## 2021-11-16[​](/docs/zh-CN/sub_account/change-log#2021-11-16 "2021-11-16的直接链接")

  * 新增子母账户接口: 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` 以支持母账户为子账户 API Key 开启或关闭 IP 白名单
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` 以支持母账户为子账户 API Key 添加 IP 白名单地址列表
    * `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` 以支持母账户为子账户 API Key 查询 IP 白名单
    * `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` 以支持母账户为子账户 API Key 删除 IP 白名单地址列表



* * *

## 2021-07-29[​](/docs/zh-CN/sub_account/change-log#2021-07-29 "2021-07-29的直接链接")

  * 子母账户接口更新: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory` 如果`startTime`和`endTime`均未发送，默认只返回最近 30 天数据



* * *

## 2021-06-15[​](/docs/zh-CN/sub_account/change-log#2021-06-15 "2021-06-15的直接链接")

  * 新增子母账户接口: 
    * `POST /sapi/v1/managed-subaccount/deposit ` 以支持投资人账户为托管子账户充值资产（仅投资人账户方使用）
    * `GET /sapi/v1/managed-subaccount/asset` 以支持投资人账户查询托管子账户资产（仅投资人账户方使用）
    * `POST /sapi/v1/managed-subaccount/withdraw`以支持投资人账户为托管子账户提币资产（仅投资人账户方使用）



* * *

## 2021-04-08[​](/docs/zh-CN/sub_account/change-log#2021-04-08 "2021-04-08的直接链接")

  * 子母账户接口更新: 
    * `GET /sapi/v1/sub-account/futures/accountSummary` 和 `GET /sapi/v2/sub-account/futures/accountSummary` 接口返回字段`asset` 更新为以 USD 计价的资产汇总，即子账户 USDT，BUSD 等保证金总和



* * *

## 2021-04-01[​](/docs/zh-CN/sub_account/change-log#2021-04-01 "2021-04-01的直接链接")

  * 子母账户接口更新: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory` 新增返回字段 `fromAccountType` 和 `toAccountType`为用户转出账户类型和转入账户类型



* * *

## 2021-03-31[​](/docs/zh-CN/sub_account/change-log#2021-03-31 "2021-03-31的直接链接")

  * 子母账户接口更新: 
    * `GET /wapi/v3/sub-account/transfer/history.html` 新增参数 `fromEmail` 和 `toEmail`，原有参数`email` 将默认查询`fromEmail`的记录



* * *

## 2021-03-08[​](/docs/zh-CN/sub_account/change-log#2021-03-08 "2021-03-08的直接链接")

  * 新增子母账户接口： 
    * `POST /sapi/v1/sub-account/virtualSubAccount` 以支持母账户创建虚拟子账户
    * `GET /sapi/v1/sub-account/list` 以支持查询子账户列表
    * `POST /sapi/v1/sub-account/blvt/enable` 以支持为子账户开通杠杆代币



* * *

## 2020-12-22[​](/docs/zh-CN/sub_account/change-log#2020-12-22 "2020-12-22的直接链接")

  * 新增子母账户接口: 
    * `GET /sapi/v1/sub-account/sub/transfer/history` 以支持查询子母账户现货资金划转历史。



* * *

## 2020-12-02[​](/docs/zh-CN/sub_account/change-log#2020-12-02 "2020-12-02的直接链接")

  * 新增子母账户接口: 
    * `GET /sapi/v2/sub-account/futures/account` 以支持查询子账户 USDT 合约和币本位合约账户详情。
    * `GET /sapi/v2/sub-account/futures/accountSummary` 以支持查询子账户 USDT 合约和币本位合约账户汇总。
    * `GET /sapi/v2/sub-account/futures/positionRisk` 以支持查询子账户 USDT 合约和币本位合约持仓信息。



* * *

## 2020-11-13[​](/docs/zh-CN/sub_account/change-log#2020-11-13 "2020-11-13的直接链接")

  * 新增子母账户接口: 
    * `POST /sapi/v1/sub-account/universalTransfer` 以支持子母账户，现货和合约账户之间相互划转。
    * `GET /sapi/v1/sub-account/universalTransfer` 以查询划转记录。



* * *

## 2020-11-09[​](/docs/zh-CN/sub_account/change-log#2020-11-09 "2020-11-09的直接链接")

  * 新增返回字段 `tranId` 于子母账户接口: 
    * `GET /sapi/v1/sub-account/futures/internalTransfer`
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`



* * *

## 2020-10-10[​](/docs/zh-CN/sub_account/change-log#2020-10-10 "2020-10-10的直接链接")

  * 子母账户接口`POST /sapi/v1/sub-account/futures/transfer`新增划转类型`type` 以支持子账户现货账户和币本位合约账户间相互划转。



* * *

## 2020-09-03[​](/docs/zh-CN/sub_account/change-log#2020-09-03 "2020-09-03的直接链接")

  * 新增子母账户接口`POST /sapi/v1/sub-account/futures/internalTransfer` 以执行子账户合约资金直接划转。
  * 新增子母账户接口`GET /sapi/v1/sub-account/futures/internalTransfer` 以查询子账户合约资金直接划转历史。



* * *

## 2020-09-01[​](/docs/zh-CN/sub_account/change-log#2020-09-01 "2020-09-01的直接链接")

  * 子母账户接口`GET /sapi/v1/sub-account/spotSummary` 返回内容中新增字段 `masterAccountTotalAsset`以获取 BTC 计价的母账户资产。



* * *

## 2020-08-27[​](/docs/zh-CN/sub_account/change-log#2020-08-27 "2020-08-27的直接链接")

  * 新增接口 `GET /sapi/v1/sub-account/spotSummary` 以获取 BTC 计价的子账户现货资产汇总。



* * *

## 2020-02-05[​](/docs/zh-CN/sub_account/change-log#2020-02-05 "2020-02-05的直接链接")

  * 新增子账户相关接口: 
    * `POST /sapi/v1/sub-account/futures/transfer`: 对子账户实施 futures 账户划转
    * `POST /sapi/v1/sub-account/margin/transfer`: 对子账户实施 margin 账户划转
    * `POST /sapi/v1/sub-account/transfer/subToSub`: 向兄弟子账户划转
    * `POST /sapi/v1/sub-account/transfer/subToMaster`: 向母账户划转
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`: 子账户获取自身划转历史



* * *

## 2019-11-08[​](/docs/zh-CN/sub_account/change-log#2019-11-08 "2019-11-08的直接链接")

  * 新增以下 sapi 接口用以管理子账户的杠杆与期货： 
    * `GET /sapi/v1/sub-account/status (HMAC SHA256)`
    * `POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/margin/account (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)`
    * `POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/futures/account (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)`
    * `GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)`



* * *

## 2019-11-04[​](/docs/zh-CN/sub_account/change-log#2019-11-04 "2019-11-04的直接链接")

  * 新增管理子账户充值功能相关的 sapi 接口 
    * `GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256))`: 获取子账户充值地址。
    * `GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256))`: 获取子账户充值记录。



* * *

## 2019-11-19[​](/docs/zh-CN/sub_account/change-log#2019-11-19 "2019-11-19的直接链接")

  * `GET /sapi/v1/sub-account/margin/account` 返回内容新增: `marginTradeCoeffVo` 其中包括 
    * `forceLiquidationBar`: 强平风险率;
    * `marginCallBar`: 补仓风险率;
    * `normalBar`: 初始风险率