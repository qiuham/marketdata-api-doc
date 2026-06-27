---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/withdraw-history
api_type: REST
updated_at: 2026-05-27 18:59:37.762588
---

# Change Log

## 2026-05-22[​](/docs/wallet/change-log#2026-05-22 "Direct link to 2026-05-22")

  * Added `accountType` parameter to the following endpoints: 
    * `POST /sapi/v1/asset/dust-convert/convert`
    * `POST /sapi/v1/asset/dust-convert/query-convertible-assets`



* * *

## 2026-04-28[​](/docs/wallet/change-log#2026-04-28 "Direct link to 2026-04-28")

  * Added error code `-4106 TAG_NOT_SUPPORTED_FOR_NETWORK` to the [error code table](/docs/wallet/error-code).
  * Updated `POST /sapi/v1/capital/withdraw/apply` documentation to clarify `addressTag` behavior for networks that do not support memo/tag.



* * *

## 2026-02-27[​](/docs/wallet/change-log#2026-02-27 "Direct link to 2026-02-27")

  * Added a new field `identifier` to the response of `GET /sapi/v1/localentity/vasp`.
  * Updated the Travel Rule deposit and withdrawal questionnaire: 
    * The input parameter `vasp` should now use the `identifier` field from the `GET /sapi/v1/localentity/vasp` response instead of the previously expected `vaspCode`.
    * Both `vaspCode` and `identifier` will be accepted for the `vasp` field in the deposit and withdrawal questionnaires during the transition period until **28 May 2026**.



* * *

## 2025-12-26[​](/docs/wallet/change-log#2025-12-26 "Direct link to 2025-12-26")

### Time-sensitive Notice[​](/docs/wallet/change-log#time-sensitive-notice "Direct link to Time-sensitive Notice")

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:**   
When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/docs/wallet/error-code#-1022-invalid_signature). Please review and update your signing logic accordingly.



### REST API[​](/docs/wallet/change-log#rest-api "Direct link to REST API")

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/docs/wallet/general-info#signed-endpoint-examples-for-post-apiv3order).



* * *

## 2025-12-19[​](/docs/wallet/change-log#2025-12-19 "Direct link to 2025-12-19")

  * Add new API for travel rule: 
    * `PUT /sapi/v2/localentity/deposit/provide-info` \- V2 version that uses `depositId` parameter instead of `tranId`.



* * *

## 2025-09-18[​](/docs/wallet/change-log#2025-09-18 "Direct link to 2025-09-18")

  * Change menu `Onboarded VASP List` to `VASP List`.



* * *

## 2025-09-12[​](/docs/wallet/change-log#2025-09-12 "Direct link to 2025-09-12")

  * Add 1 response field `travelRuleStatus` to `GET /sapi/v1/capital/deposit/hisrec`. travelRuleStatus: 0: travel rule not required OR info already provided and funds ready to use, 1: travel rule required to provide deposit info.



* * *

## 2025-09-08[​](/docs/wallet/change-log#2025-09-08 "Direct link to 2025-09-08")

  * Add 1 response field `withdrawTag` to `GET /sapi/v1/capital/config/getall`. To replace `sameAddress` use before. We provide same value for these two fields for now, recommend user to switch to `withdrawTag`.



* * *

## 2025-08-25[​](/docs/wallet/change-log#2025-08-25 "Direct link to 2025-08-25")

  * Add new deposit history api.
  * Update description of the address verify list api.
  * Update weight description of following pages: 
    * /travel-rule/withdraw-history
    * /travel-rule/withdraw-history-v2
    * /travel-rule/questionnaire-requirements
    * /travel-rule/onboarded-vasp-list



* * *

## 2025-08-05[​](/docs/wallet/change-log#2025-08-05 "Direct link to 2025-08-05")

  * Update footnote of `POST /sapi/v1/capital/withdraw/apply` related to travel rule.



* * *

## 2025-07-11[​](/docs/wallet/change-log#2025-07-11 "Direct link to 2025-07-11")

  * Add appendix: 
    * Name restriction rules.
    * Country code for travelrule.
  * Add new API for travel rule questionnaire requirements. 
    * `GET /sapi/v1/localentity/questionnaire-requirements`



* * *

## 2025-06-25[​](/docs/wallet/change-log#2025-06-25 "Direct link to 2025-06-25")

  * Update travel rule Japan documentation: 
    * Modify withdrawal questionnaire's `txnPurpose`: 
      * 1: Purchase of goods within Japan
      * 2: Inheritance, gift or living expenses
      * 3: Investment
      * 5: Use of services provided by the beneficiary VASP
      * 6: Loan repayment
      * 7: Gifts & Donations
    * Remove `txnPurposeOthers`



* * *

## 2025-06-12[​](/docs/wallet/change-log#2025-06-12 "Direct link to 2025-06-12")

  * Enable SAPI for France.
  * Fix issues in Chinese version.



* * *

## 2025-06-09[​](/docs/wallet/change-log#2025-06-09 "Direct link to 2025-06-09")

  * Explained withdrawOrderId in POST `/sapi/v1/capital/withdraw/apply` and GET `/sapi/v1/capital/withdraw/history` in detail.



* * *

## 2025-05-29[​](/docs/wallet/change-log#2025-05-29 "Direct link to 2025-05-29")

  * Update withdraw questionnaire of New Zealand to support travel rule requirements.



* * *

## 2025-05-19[​](/docs/wallet/change-log#2025-05-19 "Direct link to 2025-05-19")

  * Update withdraw/deposit questionnaire of Bahrain 
    * Withdraw:`bnfName` change to `bnfFirstName` and `bnfLastName`
    * Deposit: `orgName` change to `orgFirstName` and `orgLastName`
    * Remove residency field for withdraw/deposit.
  * Update withdraw/deposit questionnaire of Poland 
    * Withdraw:`bnfName` change to `bnfFirstName` and `bnfLastName`
    * Deposit: `orgName` change to `orgFirstName` and `orgLastName`



* * *

## 2025-05-12[​](/docs/wallet/change-log#2025-05-12 "Direct link to 2025-05-12")

  * Questionnaire update for entity KZ and IN.



* * *

## 2025-03-27[​](/docs/wallet/change-log#2025-03-27 "Direct link to 2025-03-27")

  * Add new API `GET sapi/v1/capital/withdraw/quota`，Gets the user's withdrawal quota



* * *

## 2025-02-27[​](/docs/wallet/change-log#2025-02-27 "Direct link to 2025-02-27")

  * Add 1 response field to `GET /sapi/v1/capital/config/getall`. To fetch "denomination of the coin", default 1



* * *

## 2025-01-15[​](/docs/wallet/change-log#2025-01-15 "Direct link to 2025-01-15")

  * Changed Request Weight description from IP to UID for `GET /sapi/v2/localentity/withdraw/history`
  * Changed UID rate limit description from 600 to 900 for `GET /sapi/v1/capital/withdraw/apply`.



* * *

## 2025-01-08[​](/docs/wallet/change-log#2025-01-08 "Direct link to 2025-01-08")

  * Add new API `GET /sapi/v1/localentity/vasp` to fetch onboarded VASP list for the local entity.
  * Add new API `GET /sapi/v2/localentity/withdraw/history` to improve the performance of the query.
  * Support all the Binance entities combination.



* * *

## 2024-11-21[​](/docs/wallet/change-log#2024-11-21 "Direct link to 2024-11-21")

  * Add 1 response fields to `GET /sapi/v1/capital/config/getall`. To fetch "Minimum internal withdraw amount".
  * The following APIs will no longer be supported from 2024-11-21: 
    * `POST /sapi/v1/asset/convert-transfer` BUSD asset conversion function is offline. For compatible calls, it now returns: "{"tranId":null,"status":"F","response":"No longer supported"}".
    * `GET /sapi/v1/capital/contract/convertible-coins` BUSD asset convertible stablecoin query function is offline. For compatible calls, it now returns: "{"convertEnabled":false,"coins":[],"exchangeRates":{}}".
    * `POST /sapi/v1/capital/contract/convertible-coins` BUSD asset convertible stablecoin editing function is offline. For compatible calls, there will be no changes in the backend.
  * Changed maximum idList in `GET /sapi/v1/capital/withdraw/history` to 45.



* * *

## 2024-11-08[​](/docs/wallet/change-log#2024-11-08 "Direct link to 2024-11-08")

  * Add 2 new response fields to `GET /sapi/v1/account/info`. To fetch the "European Options account enable status" and the "Portfolio Margin enable status".
  * Add 2 new response fields to `GET /sapi/v1/account/apiRestrictions`. To fetch "FIX API trading permission" and "FIX API reading permission".



* * *

## 2024-10-28[​](/docs/wallet/change-log#2024-10-28 "Direct link to 2024-10-28")

  * The Withdraw Query History API now supports `withdrawOrderId` as a query parameter.
  * The Withdraw Apply API has been updated to include logic for handling cases where the network parameter is empty.



* * *

## 2024-10-18[​](/docs/wallet/change-log#2024-10-18 "Direct link to 2024-10-18")

  * Add the onboarded VASP list for each entity.



* * *

## 2024-10-16[​](/docs/wallet/change-log#2024-10-16 "Direct link to 2024-10-16")

  * Add the onboarded VASP list of Travel Rule.



* * *

## 2024-10-09[​](/docs/wallet/change-log#2024-10-09 "Direct link to 2024-10-09")

  * Update travel rule questionnaire content: 
    * Add withdrawal/deposit questionnaire for India: India users can now use sAPI to withdraw/deposit funds



* * *

## 2025-06-25[​](/docs/wallet/change-log#2025-06-25-1 "Direct link to 2025-06-25")

  * Update travel rule Japan documentation: 
    * Modify withdrawal questionnaire's `txnPurpose`: 
      * 1: Purchase of goods within Japan
      * 2: Inheritance, gift or living expenses
      * 3: Investment
      * 5: Use of services provided by the beneficiary VASP
      * 6: Loan repayment
      * 7: Gifts & Donations
    * Remove `txnPurposeOthers`



* * *

## 2024-08-14[​](/docs/wallet/change-log#2024-08-14 "Direct link to 2024-08-14")

  * Fix travel rule api documentation: 
    * For NZ travel rule content: `isAddressOwner` should be `1`: Yes, `2`: No
    * Add comments to withdrawal/deposit API regarding url parameters



* * *

## 2024-07-09[​](/docs/wallet/change-log#2024-07-09 "Direct link to 2024-07-09")

  * Update travel rule questionnaire content: 
    * Add withdrawal/deposit questionnaire for Bahrain: Bahrain users can now use sAPI to withdraw/deposit funds
    * Update deposit questionnaire for Japan: Adding new required filled `isAttested` and fix some text issue



* * *

## 2024-06-21[​](/docs/wallet/change-log#2024-06-21 "Direct link to 2024-06-21")

  * Adding local entity withdrawal/deposit APIs to support travel rule requirements: 
    * `POST /sapi/v1/localentity/withdraw/apply`
    * `GET /sapi/v1/localentity/withdraw/history`
    * `PUT /sapi/v1/localentity/deposit/provide-info`
    * `GET /sapi/v1/localentity/deposit/history`



* * *

## 2024-06-04[​](/docs/wallet/change-log#2024-06-04 "Direct link to 2024-06-04")

  * Wallet Endpoints adjustment: for internal transfers, the txid prefix has been replaced to “Off-chain transfer”on 28 May 2024. “internal transfer” flag is no longer available in the TXID field, including historical transactions, the following endpoints are impacted: 
    * `GET /sapi/v1/capital/deposit/hisrec`
    * `GET /sapi/v1/capital/withdraw/history`
    * `GET /sapi/v1/capital/deposit/subHisrec`



* * *

## 2024-05-22[​](/docs/wallet/change-log#2024-05-22 "Direct link to 2024-05-22")

  * Update Sub Account Endpoint: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`: update response field `fromAccountType` and `toAccountType`. Return USDT_FUTURE/COIN_FUTURE in order to differentiate 2 futures wallets.
  * New Wallet Endpoint: 
    * `GET /sapi/v1/account/info`: To fetch the “VIP Level”, “whether Margin account is enabled” and “whether Futures account is enabled”



* * *

## 2024-04-08[​](/docs/wallet/change-log#2024-04-08 "Direct link to 2024-04-08")

  * Update Wallet Endpoint: 
    * `GET /sapi/v1/capital/config/getall`: delete response field `resetAddressStatus`



* * *

## 2024-01-15[​](/docs/wallet/change-log#2024-01-15 "Direct link to 2024-01-15")

  * New Endpoints for Wallet: 
    * `GET /sapi/v1/spot/delist-schedule`: Query spot delist schedule
  * Update Endpoints for Wallet: 
    * `GET /sapi/v1/asset/dribblet`：add parameter `accountType`
    * `POST /sapi/v1/asset/dust-btc`：add parameter `accountType`
    * `POST /sapi/v1/asset/dust`：add parameter `accountType`



* * *

## 2023-11-21[​](/docs/wallet/change-log#2023-11-21 "Direct link to 2023-11-21")

  * New endpoint for Wallet: 
    * `GET /sapi/v1/capital/deposit/address/list`: Fetch deposit address list with network.



* * *

## 2023-11-02[​](/docs/wallet/change-log#2023-11-02 "Direct link to 2023-11-02")

  * Changes to Wallet Endpoint: 
    * `GET /sapi/v1/account/apiRestrictions`: add new response field `enablePortfolioMarginTrading`



* * *

## 2023-09-22[​](/docs/wallet/change-log#2023-09-22 "Direct link to 2023-09-22")

  * New endpoints for Wallet: 
    * `GET /sapi/v1/asset/wallet/balance`: query user wallet balance
    * `GET /sapi/v1/asset/custody/transfer-history`: query user delegation history(For Master Account)



* * *

## 2023-09-04[​](/docs/wallet/change-log#2023-09-04 "Direct link to 2023-09-04")

  * Rate limit adjustment for Wallet Endpoint: 
    * `GET /sapi/v1/capital/withdraw/history`: UID rate limit is adjusted to 18000, maxmium 10 requests per second. Please refer to the endpoint description for detail



* * *

## 2023-05-18[​](/docs/wallet/change-log#2023-05-18 "Direct link to 2023-05-18")

  * New endpoints for Wallet： 
    * `POST /sapi/v1/capital/deposit/credit-apply`: apply deposit credit for expired address



* * *

## 2023-05-09[​](/docs/wallet/change-log#2023-05-09 "Direct link to 2023-05-09")

  * Update endpoints for Wallet: 
    * `POST /sapi/v1/asset/transfer`: add enum `MAIN_PORTFOLIO_MARGIN` and `PORTFOLIO_MARGIN_MAIN`



* * *

## 2023-02-02[​](/docs/wallet/change-log#2023-02-02 "Direct link to 2023-02-02")

  * Update endpoints for Wallet: 
    * Universal Transfer `POST /sapi/v1/asset/transfer` support option transfer



* * *

## 2022-12-26[​](/docs/wallet/change-log#2022-12-26 "Direct link to 2022-12-26")

  * New endpoints for wallet: 
    * `GET /sapi/v1/capital/contract/convertible-coins`: Get a user's auto-conversion settings in deposit/withdrawal
    * `POST /sapi/v1/capital/contract/convertible-coins`: User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.



* * *

## 2022-11-18[​](/docs/wallet/change-log#2022-11-18 "Direct link to 2022-11-18")

  * New endpoint for Wallet: 
    * `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`: The query of Cloud-Mining payment and refund history



* * *

## 2022-11-02[​](/docs/wallet/change-log#2022-11-02 "Direct link to 2022-11-02")

  * Update endpoints for Wallet: 
    * `POST /sapi/v1/capital/withdraw/apply`: Weight changed to Weight(UID): 600



* * *

## 2022-10-28[​](/docs/wallet/change-log#2022-10-28 "Direct link to 2022-10-28")

  * Update endpoints for Wallet: 
    * `POST /sapi/v1/asset/convert-transfer`: New parameter `accountType`
    * `POST /sapi/v1/asset/convert-transfer/queryByPage`: request method is changed to `GET`, new parameter `clientTranId`



* * *

## 2022-09-29[​](/docs/wallet/change-log#2022-09-29 "Direct link to 2022-09-29")

  * New endpoints for Wallet: 
    * `POST /sapi/v1/asset/convert-transfer`: Convert transfer, convert between BUSD and stablecoins.
    * `POST /sapi/v1/asset/convert-transfer/queryByPage`: Query convert transfer



* * *

## 2022-07-01[​](/docs/wallet/change-log#2022-07-01 "Direct link to 2022-07-01")

  * New endpoint for Wallet: 
    * `POST /sapi/v3/asset/getUserAsset` to get user assets.



* * *

## 2022-2-17[​](/docs/wallet/change-log#2022-2-17 "Direct link to 2022-2-17")

The following updates will take effect on **February 24, 2022 08:00 AM UTC**

  * Update endpoint for Wallet： 
    * `GET /sapi/v1/accountSnapshot`



The time limit of this endpoint is shortened to only support querying the data of the latest month

* * *

## 2022-02-09[​](/docs/wallet/change-log#2022-02-09 "Direct link to 2022-02-09")

  * New endpoint for Wallet: 
    * `POST /sapi/v1/asset/dust-btc` to get assets that can be converted into BNB



* * *

## 2021-12-30[​](/docs/wallet/change-log#2021-12-30 "Direct link to 2021-12-30")

  * Update endpoint for Wallet： 
    * As the Mining account is merged into Funding account, transfer types MAIN_MINING, MINING_MAIN, MINING_UMFUTURE, MARGIN_MINING, and MINING_MARGIN will be discontinued in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` on **January 05, 2022 08:00 AM UTC**



* * *

## 2021-11-19[​](/docs/wallet/change-log#2021-11-19 "Direct link to 2021-11-19")

  * Update endpoint for Wallet: 
    * New field`info`added in`GET /sapi/v1/capital/withdraw/history`to show the reason for withdrawal failure



* * *

## 2021-11-18[​](/docs/wallet/change-log#2021-11-18 "Direct link to 2021-11-18")

The following updates will take effect on **November 25, 2021 08:00 AM UTC**

  * Update endpoint for Wallet： 
    * `GET /sapi/v1/accountSnapshot`



The query time range of both endpoints are shortened to support data query within the last 6 months only, where startTime does not support selecting a timestamp beyond 6 months. If you do not specify startTime and endTime, the data of the last 7 days will be returned by default.

* * *

## 2021-11-17[​](/docs/wallet/change-log#2021-11-17 "Direct link to 2021-11-17")

  * The following endpoints will be discontinued on **November 17, 2021 13:00 PM UTC** : 
    * `POST /sapi/v1/account/apiRestrictions/ipRestriction` to support user enable and disable IP restriction for an API Key
    * `POST /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user add IP list for an API Key
    * `GET /sapi/v1/account/apiRestrictions/ipRestriction` to support user query IP restriction for an API Key
    * `DELETE /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user delete IP list for an API Key



* * *

## 2021-11-16[​](/docs/wallet/change-log#2021-11-16 "Direct link to 2021-11-16")

  * New endpoints for Sub-Account: 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and disable IP restriction for a sub-account API Key
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP list for a sub-account API Key
    * `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account query IP restriction for a sub-account API Key
    * `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account delete IP list for a sub-account API Key



* * *

## 2021-11-05[​](/docs/wallet/change-log#2021-11-05 "Direct link to 2021-11-05")

  * Update endpoint for Wallet: 
    * New parameter `walletType `added in `POST /sapi/v1/capital/withdraw/apply` to support user choose wallet type `spot wallet` and `funding wallet` when withdraw crypto.



* * *

## 2021-11-04[​](/docs/wallet/change-log#2021-11-04 "Direct link to 2021-11-04")

The following updates will take effect on **November 11, 2021 08:00 AM UTC**

  * Update endpoints for Wallet and Futures： 
    * `GET /sapi/v1/asset/transfer`
    * `GET /sapi/v1/futures/transfer`



The query time range of both endpoints are shortened to support data query within the last 6 months only, where startTime does not support selecting a timestamp beyond 6 months. If you do not specify startTime and endTime, the data of the last 7 days will be returned by default.

* * *

## 2021-10-22[​](/docs/wallet/change-log#2021-10-22 "Direct link to 2021-10-22")

  * Update endpoint for Wallet: 
    * New transfer types `MAIN_FUNDING`,`FUNDING_MAIN`,`FUNDING_UMFUTURE`,`UMFUTURE_FUNDING`,`MARGIN_FUNDING`,`FUNDING_MARGIN`,`FUNDING_CMFUTURE`and `CMFUTURE_FUNDING` added in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support transfer assets among funding account and other accounts
    * As the C2C account, Binance Payment, Binance Card and other business account are merged into a Funding account, transfer types `MAIN_C2C`,`C2C_MAIN`,`C2C_UMFUTURE`,`C2C_MINING`,`UMFUTURE_C2C`,`MINING_C2C`,`MARGIN_C2C`,`C2C_MARGIN`,`MAIN_PAY`and `PAY_MAIN` will be discontinued in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` on **November 04, 2021 08:00 AM UTC**



* * *

## 2021-09-03[​](/docs/wallet/change-log#2021-09-03 "Direct link to 2021-09-03")

  * Update endpoint for Wallet: _ New fields `sameAddress`,`depositDust` and `specialWithdrawTips`added in `GET /sapi/v1/capital/config/getall` `sameAddress` means if the coin needs to provide memo to withdraw `depositDust` means minimum creditable amount `specialWithdrawTips` means special tips for withdraw _ New field `confirmNo`added in `GET /sapi/v1/capital/withdraw/history` to support query confirm times for withdraw history



* * *

## 2021-08-27[​](/docs/wallet/change-log#2021-08-27 "Direct link to 2021-08-27")

  * Update endpoint for Wallet: 
    * New parameter `withdrawOrderId`added in `GET /sapi/v1/capital/withdraw/history` to support user query withdraw history by withdrawOrderId
    * New field `unlockConfirm`added in `GET /sapi/v1/capital/deposit/hisrec` to support query network confirm times for unlocking



* * *

## 2021-08-20[​](/docs/wallet/change-log#2021-08-20 "Direct link to 2021-08-20")

  * Update endpoint for Wallet: 
    * New parameters`fromSymbol`,`toSymbol`and new transfer types `ISOLATEDMARGIN_MARGIN`, `MARGIN_ISOLATEDMARGIN`and `ISOLATEDMARGIN_ISOLATEDMARGIN` added in `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support user transfer assets between Margin(cross) account and Margin(isolated) account



* * *

## 2021-07-16[​](/docs/wallet/change-log#2021-07-16 "Direct link to 2021-07-16")

  * New endpoint for Wallet: 
    * `GET /sapi/v1/account/apiRestrictions` to query user API Key permission



* * *

## 2021-07-09[​](/docs/wallet/change-log#2021-07-09 "Direct link to 2021-07-09")

  * New endpoint for Wallet: 
    * `POST /sapi/v1/asset/get-funding-asset` to query funding wallet, includes Binance Pay, Binance Card, Binance Gift Card, Stock Token



* * *

## 2021-06-24[​](/docs/wallet/change-log#2021-06-24 "Direct link to 2021-06-24")

  * Update endpoints for Wallet: 
    * `GET /sapi/v1/capital/withdraw/history` added default value 1000, max value 1000 for the parameter`limit`
    * `GET /sapi/v1/capital/deposit/hisrec` added default value 1000, max value 1000 for the parameter`limit`



* * *

## 2021-05-26[​](/docs/wallet/change-log#2021-05-26 "Direct link to 2021-05-26")

  * Update endpoint for Wallet: 
    * New transfer types `MAIN_PAY` ,`PAY_MAIN` added in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support trasnfer assets between spot account and pay account



* * *

## 2020-12-30[​](/docs/wallet/change-log#2020-12-30 "Direct link to 2020-12-30")

  * New endpoint for Wallet: 
    * `POST /sapi/v1/asset/transfer` to support user universal transfer among Spot, Margin, Futures, C2C, MINING accounts.
    * `GET /sapi/v1/asset/transfer` to get user universal transfer history.



* * *

## 2020-04-02[​](/docs/wallet/change-log#2020-04-02 "Direct link to 2020-04-02")

  * New fields in response to endpoint`GET /sapi/v1/capital/config/getall`： 
    * `minConfirm` for min number for balance confirmation
    * `unLockConfirm` for confirmation number for balance unlock



* * *

## 2020-03-13[​](/docs/wallet/change-log#2020-03-13 "Direct link to 2020-03-13")

  * New parameter `transactionFeeFlag` is available in endpoint: 
    * `POST /sapi/v1/capital/withdraw/apply` and
    * `POST /wapi/v3/withdraw.html`



* * *

## 2020-01-15[​](/docs/wallet/change-log#2020-01-15 "Direct link to 2020-01-15")

  * New parameter `withdrawOrderId` for client customized withdraw id for endpoint `POST /wapi/v3/withdraw.html`.
  * New field `withdrawOrderId` in response to `GET /wapi/v3/withdrawHistory.html`



* * *

## 2019-12-25[​](/docs/wallet/change-log#2019-12-25 "Direct link to 2019-12-25")

  * Added time interval limit in  
`GET /sapi/v1/capital/withdraw/history`,  
`GET /wapi/v3/withdrawHistory.html`,  
`GET /sapi/v1/capital/deposit/hisrec` and  
`GET /wapi/v3/depositHistory.html`: _ The default `startTime` is 90 days from current time, and the default `endTime` is current time. _ Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days. * If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.



* * *

## 2019-12-18[​](/docs/wallet/change-log#2019-12-18 "Direct link to 2019-12-18")

  * New endpoint to get daily snapshot of account:  
`GET /sapi/v1/accountSnapshot`



* * *

## 2019-11-30[​](/docs/wallet/change-log#2019-11-30 "Direct link to 2019-11-30")

  * Added parameter `sideEffectType` in `POST /sapi/v1/margin/order (HMAC SHA256)` with enums:

    * `NO_SIDE_EFFECT` for normal trade order;
    * `MARGIN_BUY` for margin trade order;
    * `AUTO_REPAY` for making auto repayment after order filled.
  * New field `marginBuyBorrowAmount` and `marginBuyBorrowAsset` in `FULL` response to `POST /sapi/v1/margin/order (HMAC SHA256)`




* * *

## 2019-10-29[​](/docs/wallet/change-log#2019-10-29 "Direct link to 2019-10-29")

  * New sapi endpoints for wallet. 
    * `POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)`: withdraw.
    * `Get /sapi/v1/capital/withdraw/history (HMAC SHA256)`: fetch withdraw history with network.



* * *

## 2019-10-14[​](/docs/wallet/change-log#2019-10-14 "Direct link to 2019-10-14")

  * New sapi endpoints for wallet. 
    * `GET /sapi/v1/capital/config/getall (HMAC SHA256)`: get all coins' information for user.
    * `GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)`: fetch deposit history with network.
    * `GET /sapi/v1/capital/deposit/address (HMAC SHA256)`: fetch deposit address with network.

---

# 更新日志

## 2026-05-22[​](/docs/zh-CN/wallet/change-log#2026-05-22 "2026-05-22的直接链接")

  * 以下接口新增 `accountType` 参数： 
    * `POST /sapi/v1/asset/dust-convert/convert`
    * `POST /sapi/v1/asset/dust-convert/query-convertible-assets`



* * *

## 2026-04-28[​](/docs/zh-CN/wallet/change-log#2026-04-28 "2026-04-28的直接链接")

  * 在[错误代码表](/docs/zh-CN/wallet/error-code)中新增错误代码 `-4106 TAG_NOT_SUPPORTED_FOR_NETWORK`。
  * 更新 `POST /sapi/v1/capital/withdraw/apply` 文档，说明不支持 memo/tag 的网络中 `addressTag` 的使用规则。



* * *

## 2026-02-27[​](/docs/zh-CN/wallet/change-log#2026-02-27 "2026-02-27的直接链接")

  * 在 `GET /sapi/v1/localentity/vasp` 的响应中新增了字段 `identifier`。
  * 更新了旅行规则（Travel Rule）存取款问卷： 
    * 输入参数 `vasp` 现在应使用 `GET /sapi/v1/localentity/vasp` 响应中的 `identifier` 字段，替代之前预期的 `vaspCode`。
    * 在过渡期内，存取款问卷的 `vasp` 字段将同时接受 `vaspCode` 和 `identifier`，该过渡期截至 **2026年5月28日** 。



* * *

## 2025-12-26[​](/docs/zh-CN/wallet/change-log#2025-12-26 "2025-12-26的直接链接")

### 时效性通知[​](/docs/zh-CN/wallet/change-log#时效性通知 "时效性通知的直接链接")

  * **以下有关于REST API变更将在 2026-01-15 07:OO UTC 发生:**   
调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/docs/zh-CN/wallet/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。



### REST API[​](/docs/zh-CN/wallet/change-log#rest-api "REST API的直接链接")

  * 更新了 REST API 文档中有关于 [签名请求示例](/docs/zh-CN/wallet/general-info#post-apiv3order-%E7%9A%84%E7%AD%BE%E5%90%8D%E7%A4%BA%E4%BE%8B) 的部分。



* * *

## 2025-12-19[​](/docs/zh-CN/wallet/change-log#2025-12-19 "2025-12-19的直接链接")

  * 新增旅行规则 API: 
    * `PUT /sapi/v2/localentity/deposit/provide-info` \- V2 版本，使用 `depositId` 参数替代 `tranId`。



* * *

## 2025-09-18[​](/docs/zh-CN/wallet/change-log#2025-09-18 "2025-09-18的直接链接")

  * 修改菜单名称 `Onboarded VASP List` 到 `VASP List`.



* * *

## 2025-09-12[​](/docs/zh-CN/wallet/change-log#2025-09-12 "2025-09-12的直接链接")

  * 新增一个返回字段 `travelRuleStatus` 在 `GET /sapi/v1/capital/deposit/hisrec`. travelRuleStatus: 0: travel rule not required OR info already provided and funds ready to use, 1: travel rule required to provide deposit info.



* * *

## 2025-09-08[​](/docs/zh-CN/wallet/change-log#2025-09-08 "2025-09-08的直接链接")

  * 新增一个返回字段 `withdrawTag` 在 `GET /sapi/v1/capital/config/getall`接口上. 替换原有的 `sameAddress` 字段. 建议用户使用新的 `withdrawTag` 字段，暂时会保留 `sameAddress` 并且值与 `withdrawTag` 相同.



* * *

## 2025-08-25[​](/docs/zh-CN/wallet/change-log#2025-08-25 "2025-08-25的直接链接")

  * 添加新的充值历史记录V2 API。
  * 更新地址验证列表 API 的描述。
  * 更新以下页面的权重描述： 
    * /travel-rule/withdraw-history
    * /travel-rule/withdraw-history-v2
    * /travel-rule/questionnaire-requirements
    * /travel-rule/onboarded-vasp-list



* * *

## 2025-08-05[​](/docs/zh-CN/wallet/change-log#2025-08-05 "2025-08-05的直接链接")

  * 更新 `POST /sapi/v1/capital/withdraw/apply` 接口关于旅行规则的脚注说明。



* * *

## 2025-07-11[​](/docs/zh-CN/wallet/change-log#2025-07-11 "2025-07-11的直接链接")

  * 添加附录： 
    * 姓名限制规则。
    * 旅行规则的国家/地区代码。
  * 添加用于旅行规则问卷要求的新 API。 
    * `GET /sapi/v1/localentity/questionnaire-requirements`



* * *

## 2025-06-25[​](/docs/zh-CN/wallet/change-log#2025-06-25 "2025-06-25的直接链接")

  * 修改Travel Rule API文档: 
    * 修改提币问卷`txnPurpose`选项: 
      * 1: 在日本国内购物
      * 2: 遗产、赠予或生活费
      * 4: 投资
      * 5: 支付第三方VASP的服务费用
      * 6: 偿还贷款
      * 7: 礼物或捐款
    * 删除`txnPurposeOthers`



* * *

## 2025-06-12[​](/docs/zh-CN/wallet/change-log#2025-06-12 "2025-06-12的直接链接")

  * 开启法国SAPI支持，问卷中增加法国问卷内容。
  * 修复文档中文版本的若干问题。



* * *

## 2025-06-10[​](/docs/zh-CN/wallet/change-log#2025-06-10 "2025-06-10的直接链接")

  * 详细解释了 withdrawOrderId 在 POST `/sapi/v1/capital/withdraw/apply` 和 GET `/sapi/v1/capital/withdraw/history` 中的使用



* * *

## 2025-05-12[​](/docs/zh-CN/wallet/change-log#2025-05-12 "2025-05-12的直接链接")

  * 合规站KZ，IN，问卷更新.



* * *

## 2025-03-27[​](/docs/zh-CN/wallet/change-log#2025-03-27 "2025-03-27的直接链接")

  * 新增接口`GET sapi/v1/capital/withdraw/quota`，获取用户提现额度



* * *

## 2025-02-27[​](/docs/zh-CN/wallet/change-log#2025-02-27 "2025-02-27的直接链接")

  * `GET /sapi/v1/capital/config/getall`接口增加了一个`币种面值`的返回，默认不返回代表为1.



* * *

## 2025-01-15[​](/docs/zh-CN/wallet/change-log#2025-01-15 "2025-01-15的直接链接")

  * 更新 `GET /sapi/v2/localentity/withdraw/history` 接口 `请求权重` 描述为 UID.
  * 更新 `GET /sapi/v1/capital/withdraw/apply` 接口 `请求权重` 描述从 600 到 900.



* * *

## 2025-01-08[​](/docs/zh-CN/wallet/change-log#2025-01-08 "2025-01-08的直接链接")

  * 增加新接口 `GET /sapi/v1/localentity/vasp` 用来获取本地站支持的VASP列表.
  * 增加新接口 `GET /sapi/v2/localentity/withdraw/history` 改善提币历史查询的效率.
  * 支持问卷中合并`Binance`的逻辑。



* * *

## 2024-11-21[​](/docs/zh-CN/wallet/change-log#2024-11-21 "2024-11-21的直接链接")

  * `GET /sapi/v1/capital/config/getall`接口增加了一个`内部转账最小提现数`的返回.
  * 以下接口功能将于 2024-11-21 不再提供支持： 
    * `POST /sapi/v1/asset/convert-transfer` BUSD的资产相互转换接口功能下线，为兼容调用，现固定返回："{"tranId":null,"status":"F","response":"No longer supported"}"
    * `GET /sapi/v1/capital/contract/convertible-coins` BUSD资产可相互转换的稳定币查询功能下线，为兼容调用，现固定返回:"{"convertEnabled":false,"coins":[],"exchangeRates":{}}"
    * `POST /sapi/v1/capital/contract/convertible-coins` BUSD资产可相互转换稳定币编辑功能下线，为兼容调用，后台不再有任何更改
  * 将 `GET /sapi/v1/capital/withdraw/history` 接口参数 idList 最大值调整为 45



* * *

## 2024-11-08[​](/docs/zh-CN/wallet/change-log#2024-11-08 "2024-11-08的直接链接")

  * 更新 `GET /sapi/v1/account/info`：新增 "European Options account enable status" 與 "Portfolio Margin enable status"。
  * 更新 `GET /sapi/v1/account/apiRestrictions`：新增 "FIX API trading permission" 與 "FIX API reading permission"。



* * *

## 2024-10-28[​](/docs/zh-CN/wallet/change-log#2024-10-28 "2024-10-28的直接链接")

  * 提现查询历史 API 现在支持 `withdrawOrderId` 作为查询参数。
  * 提现申请 API 已更新，增加了处理网络参数为空的逻辑。



* * *

## 2024-10-18[​](/docs/zh-CN/wallet/change-log#2024-10-18 "2024-10-18的直接链接")

  * 为每一个主题添加对应的预先加载的VASP列表.



* * *

## 2024-10-16[​](/docs/zh-CN/wallet/change-log#2024-10-16 "2024-10-16的直接链接")

  * 为Travel Rule API增加预先加载的VASP列表



* * *

## 2024-10-09[​](/docs/zh-CN/wallet/change-log#2024-10-09 "2024-10-09的直接链接")

  * 更新Travel Rule问卷内容: 
    * 新增印度的提现/充值问卷: 印度用户现在可以参考问卷内容使用sAPI进行提现/充值



* * *

## 2025-06-25[​](/docs/zh-CN/wallet/change-log#2025-06-25-1 "2025-06-25的直接链接")

  * 修改Travel Rule API文档: 
    * 修改提币问卷`txnPurpose`选项: 
      * 1: 在日本国内购物
      * 2: 遗产、赠予或生活费
      * 4: 投资
      * 5: 支付第三方VASP的服务费用
      * 6: 偿还贷款
      * 7: 礼物或捐款
    * 删除`txnPurposeOthers`



* * *

## 2024-08-14[​](/docs/zh-CN/wallet/change-log#2024-08-14 "2024-08-14的直接链接")

  * 修改Travel Rule API文档: 
    * 新西兰问卷内容: `isAddressOwner` 的枚举值应为 `1`:是, `2`:不是
    * 增加出金/入金API文档对于URL参数的补充描述



* * *

## 2024-07-09[​](/docs/zh-CN/wallet/change-log#2024-07-09 "2024-07-09的直接链接")

  * 更新Travel Rule问卷内容: 
    * 新增巴林的提现/充值问卷: 巴林用户现在可以参考问卷内容使用sAPI进行提现/充值
    * 更新日本充值问卷: 新增必填项目`声明`，并修改了一些文本错误



* * *

## 2024-06-21[​](/docs/zh-CN/wallet/change-log#2024-06-21 "2024-06-21的直接链接")

  * 新增本地站用充值/提币接口以满足旅行规则的合规需求: 
    * `POST /sapi/v1/localentity/withdraw/apply`
    * `GET /sapi/v1/localentity/withdraw/history`
    * `PUT /sapi/v1/localentity/deposit/provide-info`
    * `GET /sapi/v1/localentity/deposit/history`



* * *

## 2024-06-04[​](/docs/zh-CN/wallet/change-log#2024-06-04 "2024-06-04的直接链接")

  * 钱包接口调整：对于内部转账，TXID前缀已于2024年5月28日被替换为“Off-chain transfer”。"Internal transfer"标记不再出现在TXID字段中，包括历史交易，以下接口受到影响： 
    * `GET /sapi/v1/capital/deposit/hisrec`
    * `GET /sapi/v1/capital/withdraw/history`
    * `GET /sapi/v1/capital/deposit/subHisrec`



* * *

## 2024-05-22[​](/docs/zh-CN/wallet/change-log#2024-05-22 "2024-05-22的直接链接")

  * 更新子账户接口: 
    * `GET /sapi/v1/sub-account/transfer/subUserHistory`: 更新返回字段`fromAccountType`和 `toAccountType`. 合约钱包划转时返回USDT_FUTURE/COIN_FUTURE以区分钱包
  * 新增钱包接口: 
    * `GET /sapi/v1/account/info`: 取得 “VIP 等级”, “是否开启杠杆帐户” 及 “是否开启合约帐户”



* * *

## 2024-04-18[​](/docs/zh-CN/wallet/change-log#2024-04-18 "2024-04-18的直接链接")

  * 新增钱包接口: 
    * `GET /sapi/v1/capital/withdraw/address/list`: 获取提现地址列表



* * *

## 2024-04-08[​](/docs/zh-CN/wallet/change-log#2024-04-08 "2024-04-08的直接链接")

  * 更新钱包接口: 
    * `GET /sapi/v1/capital/config/getall`: 删除返回字段 `resetAddressStatus`



* * *

## 2024-01-15[​](/docs/zh-CN/wallet/change-log#2024-01-15 "2024-01-15的直接链接")

  * 新增钱包接口: 
    * `GET /sapi/v1/spot/delist-schedule`：查询现货币对的下架计划
  * 更新钱包接口: 
    * `GET /sapi/v1/asset/dribblet`：增加参数`accountType`
    * `POST /sapi/v1/asset/dust-btc`：增加参数`accountType`
    * `POST /sapi/v1/asset/dust`：增加参数`accountType`



* * *

## 2023-11-21[​](/docs/zh-CN/wallet/change-log#2023-11-21 "2023-11-21的直接链接")

  * 新增钱包接口: 
    * `GET /sapi/v1/capital/deposit/address/list`: 根据网络币种或币种获取充值地址列表



* * *

## 2023-11-02[​](/docs/zh-CN/wallet/change-log#2023-11-02 "2023-11-02的直接链接")

  * 钱包接口更新: 
    * `GET /sapi/v1/account/apiRestrictions`: 新增相应字段 `enablePortfolioMarginTrading`



* * *

## 2023-09-22[​](/docs/zh-CN/wallet/change-log#2023-09-22 "2023-09-22的直接链接")

  * 新增钱包接口： 
    * `GET /sapi/v1/asset/wallet/balance`: 查询用户钱包余额
    * `GET /sapi/v1/asset/custody/transfer-history`: 查询用户委托资金历史(适用主账户)



* * *

## 2023-09-04[​](/docs/zh-CN/wallet/change-log#2023-09-04 "2023-09-04的直接链接")

  * 钱包接口限频调整： 
    * `GET /sapi/v1/capital/withdraw/history`: Weight(UID)调整为 18000，每秒最多请求 10 次。请查看接口描述获得更详细内容



* * *

## 2023-05-18[​](/docs/zh-CN/wallet/change-log#2023-05-18 "2023-05-18的直接链接")

  * 新增钱包接口： 
    * `POST /sapi/v1/capital/deposit/credit-apply`：申请充值到过期地址的一键上账



* * *

## 2023-05-09[​](/docs/zh-CN/wallet/change-log#2023-05-09 "2023-05-09的直接链接")

  * 更新钱包接口： 
    * `POST /sapi/v1/asset/transfer`：增加枚举类型`MAIN_PORTFOLIO_MARGIN` 和 `PORTFOLIO_MARGIN_MAIN`



* * *

## 2023-02-02[​](/docs/zh-CN/wallet/change-log#2023-02-02 "2023-02-02的直接链接")

  * 更新钱包接口: 
    * 万能划转`POST /sapi/v1/asset/transfer`支持期权



* * *

## 2022-12-26[​](/docs/zh-CN/wallet/change-log#2022-12-26 "2022-12-26的直接链接")

  * 添加钱包接口： 
    * `GET /sapi/v1/capital/contract/convertible-coins`: 查询用户充值/提现时候稳定币与 BUSD 互转的设置
    * `POST /sapi/v1/capital/contract/convertible-coins`: 修改哪些稳定币可与 BUSD 互相转换



* * *

## 2022-11-18[​](/docs/zh-CN/wallet/change-log#2022-11-18 "2022-11-18的直接链接")

  * 新增钱包接口: 
    * `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`: 云算力支付和退款历史分页查询



* * *

## 2022-11-02[​](/docs/zh-CN/wallet/change-log#2022-11-02 "2022-11-02的直接链接")

  * 更新钱包接口： 
    * `POST /sapi/v1/capital/withdraw/apply`： 权重改至 Weight(UID) 600。



* * *

## 2022-10-28[​](/docs/zh-CN/wallet/change-log#2022-10-28 "2022-10-28的直接链接")

  * 更新钱包接口： 
    * `POST /sapi/v1/asset/convert-transfer`: 增加 `accountType` 参数
    * `POST /sapi/v1/asset/convert-transfer/queryByPage`: 改为 `GET` 请求方式，增加 `clientTranId` 参数



* * *

## 2022-09-29[​](/docs/zh-CN/wallet/change-log#2022-09-29 "2022-09-29的直接链接")

  * 添加钱包接口： 
    * `POST /sapi/v1/asset/convert-transfer`: 稳定币自动兑换划转
    * `POST /sapi/v1/asset/convert-transfer/queryByPage`: 稳定币自动兑换划转查询



* * *

## 2022-07-01[​](/docs/zh-CN/wallet/change-log#2022-07-01 "2022-07-01的直接链接")

  * 添加新钱包接口： 
    * `POST /sapi/v3/asset/getUserAsset` 获取用户持仓。



* * *

## 2022-2-17[​](/docs/zh-CN/wallet/change-log#2022-2-17 "2022-2-17的直接链接")

以下更新于**2 月 24, 2022 08:00 AM UTC** 生效

  * 更新钱包接口： 
    * `GET /sapi/v1/accountSnapshot`



接口查询范围缩短为仅支持查询最近一个月数据，即 startTime 不支持选定最近 1 个月之外的时间。

* * *

## 2022-2-09[​](/docs/zh-CN/wallet/change-log#2022-2-09 "2022-2-09的直接链接")

  * 新增钱包接口: 
    * `POST /sapi/v1/asset/dust-btc` 以获取可以转换成 BNB 的小额资产



## 2021-12-30[​](/docs/zh-CN/wallet/change-log#2021-12-30 "2021-12-30的直接链接")

  * 更新钱包接口： 
    * 由于矿池钱包合并于资金账户钱包,用户万向划转接口 `POST /sapi/v1/asset/transfer`的以下划转类型 MAIN_MINING, MINING_MAIN, MINING_UMFUTURE, MARGIN_MINING,和 MINING_MARGIN 将于 **1 月 05, 2022 08:00 AM UTC** 停止使用



* * *

## 2021-11-19[​](/docs/zh-CN/wallet/change-log#2021-11-19 "2021-11-19的直接链接")

  * 更新钱包接口: 
    * 新增响应参数 `info` 于接口 `GET /sapi/v1/capital/withdraw/history` 以显示提币失败原因



* * *

## 2021-11-19[​](/docs/zh-CN/wallet/change-log#2021-11-19-1 "2021-11-19的直接链接")

  * 更新钱包接口: 
    * 新增响应参数 `info` 于接口 `GET /sapi/v1/capital/withdraw/history` 以显示提币失败原因



* * *

## 2021-11-18[​](/docs/zh-CN/wallet/change-log#2021-11-18 "2021-11-18的直接链接")

以下更新于**11 月 25, 2021 08:00 AM UTC** 生效

  * 更新钱包接口： 
    * `GET /sapi/v1/accountSnapshot`



接口查询范围缩短为仅支持查询最近半年内的数据，即 startTime 不支持选定最近 6 个月之外的时间。若您没有传入 startTime 和 endTime，则默认返回最近 7 天的数据

* * *

## 2021-11-17[​](/docs/zh-CN/wallet/change-log#2021-11-17 "2021-11-17的直接链接")

  * 以下接口将于**11 月 17, 2021 13:00 PM UTC** 停止使用: 
    * `POST /sapi/v1/account/apiRestrictions/ipRestriction` 以支持用户为 API Key 开启或关闭 IP 白名单
    * `POST /sapi/v1/account/apiRestrictions/ipRestriction/ipList` 以支持用户为 API Key 添加 IP 白名单地址列表
    * `GET /sapi/v1/account/apiRestrictions/ipRestriction` 以支持用户为 API Key 查询 IP 白名单
    * `DELETE /sapi/v1/account/apiRestrictions/ipRestriction/ipList` 以支持用户为 API Key 删除 IP 白名单地址列表



* * *

## 2021-11-16[​](/docs/zh-CN/wallet/change-log#2021-11-16 "2021-11-16的直接链接")

  * 新增子母账户接口: 
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` 以支持母账户为子账户 API Key 开启或关闭 IP 白名单
    * `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` 以支持母账户为子账户 API Key 添加 IP 白名单地址列表
    * `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` 以支持母账户为子账户 API Key 查询 IP 白名单
    * `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` 以支持母账户为子账户 API Key 删除 IP 白名单地址列表



* * *

## 2021-11-05[​](/docs/zh-CN/wallet/change-log#2021-11-05 "2021-11-05的直接链接")

  * 更新钱包接口: 
    * 新增参数 `walletType`于提币接口`POST /sapi/v1/capital/withdraw/apply`以支持用户选择从`现货钱包`或`资金钱包`进行提币



* * *

## 2021-11-04[​](/docs/zh-CN/wallet/change-log#2021-11-04 "2021-11-04的直接链接")

以下更新于**11 月 11, 2021 08:00 AM UTC** 生效

  * 更新接口： 
    * `GET /sapi/v1/asset/transfer`



接口查询范围缩短为仅支持查询最近半年内的数据，即 startTime 不支持选定最近 6 个月之外的时间。若您没有传入 startTime 和 endTime，则默认返回最近 7 天的数据

* * *

## 2021-10-22[​](/docs/zh-CN/wallet/change-log#2021-10-22 "2021-10-22的直接链接")

  * 钱包接口更新: 
    * 新增划转类型 `MAIN_FUNDING`,`FUNDING_MAIN`,`FUNDING_UMFUTURE`,`UMFUTURE_FUNDING`,`MARGIN_FUNDING`,`FUNDING_MARGIN`,`FUNDING_CMFUTURE`and `CMFUTURE_FUNDING` 于用户万向划转接口 `POST /sapi/v1/asset/transfer` 和 `GET /sapi/v1/asset/transfer` 以支持资金账户和现货账户，杠杆全仓账户，U 本位合约账户，币本位合约账户之间相互划转
    * 由于 C2C 账户，币安支付、币安卡等业务合并至资金账户，用户万向划转接口`POST /sapi/v1/asset/transfer` 和 `GET /sapi/v1/asset/transfer` 的以下划转类型`MAIN_C2C`,`C2C_MAIN`,`C2C_UMFUTURE`,`C2C_MINING`,`UMFUTURE_C2C`,`MINING_C2C`,`MARGIN_C2C`,`C2C_MARGIN`,`MAIN_PAY`和`PAY_MAIN` 将于**11 月 04, 2021 08:00 AM UTC** 停止使用



* * *

## 2021-09-03[​](/docs/zh-CN/wallet/change-log#2021-09-03 "2021-09-03的直接链接")

  * 更新钱包接口: 
    * 新增响应内容 `sameAddress`，`depositDust` 和 `specialWithdrawTips`于`GET /sapi/v1/capital/config/getall`, `sameAddress` 表示需要输入 memo 的币种,`depositDust` 表示最小可上帐金额,`specialWithdrawTips` 表示提现时的特殊说明
    * 新增响应内容 `confirmNo`于`GET /sapi/v1/capital/withdraw/history` 以支持查询提现确认数



* * *

## 2021-08-27[​](/docs/zh-CN/wallet/change-log#2021-08-27 "2021-08-27的直接链接")

  * 更新钱包接口: 
    * 新增参数 `withdrawOrderId` 于 `GET /sapi/v1/capital/withdraw/history` 以支持查询指定`withdrawOrderId`的提币历史记录
    * 新增响应内容 `unlockConfirm` 于 `GET /sapi/v1/capital/deposit/hisrec` 以支持查询解锁需要的网络确认次数



* * *

## 2021-08-20[​](/docs/zh-CN/wallet/change-log#2021-08-20 "2021-08-20的直接链接")

  * 更新钱包接口: 
    * 新增参数`fromSymbol `，`toSymbol `和新增划转类型 `ISOLATEDMARGIN_MARGIN`， `MARGIN_ISOLATEDMARGIN`， `ISOLATEDMARGIN_ISOLATEDMARGIN` 于接口 `POST /sapi/v1/asset/transfer` 和 `GET /sapi/v1/asset/transfer` 以支持杠杆逐仓钱包与杠杆全仓钱包之前相互划转



* * *

## 2021-07-16[​](/docs/zh-CN/wallet/change-log#2021-07-16 "2021-07-16的直接链接")

  * 新增钱包接口: 
    * `GET /sapi/v1/account/apiRestrictions` 以查询用户 API Key 权限



* * *

## 2021-07-09[​](/docs/zh-CN/wallet/change-log#2021-07-09 "2021-07-09的直接链接")

  * 新增钱包接口: 
    * `POST /sapi/v1/asset/get-funding-asset` 以查询资金账户资产，目前支持查询的业务为：Binance Pay, Binance Card, Binance Gift Card, Stock Token



* * *

## 2021-06-24[​](/docs/zh-CN/wallet/change-log#2021-06-24 "2021-06-24的直接链接")

  * 钱包接口更新: 
    * `GET /sapi/v1/capital/withdraw/history` 现有的 `limit` 参数增加默认值 1000，最大值 1000 的限制
    * `GET /sapi/v1/capital/deposit/hisrec` 现有的 `limit` 参数增加默认值 1000，最大值 1000 的限制



* * *

## 2021-05-26[​](/docs/zh-CN/wallet/change-log#2021-05-26 "2021-05-26的直接链接")

  * 更新钱包接口： 
    * 用户万向划转接口 `POST /sapi/v1/asset/transfer` 和`GET /sapi/v1/asset/transfer` 新增划转类型`MAIN_PAY` , `PAY_MAIN` 以支持现货和支付账户之间相互划转



* * *

## 2020-12-30[​](/docs/zh-CN/wallet/change-log#2020-12-30 "2020-12-30的直接链接")

  * 新增钱包接口: 
    * `POST /sapi/v1/asset/transfer` 用户万向划转接口，以支持现货，全仓杠杆，合约，C2C，矿池账户间划转。
    * `GET /sapi/v1/asset/transfer` 以支持查询用户万向划转历史记录。



* * *

## 2020-04-02[​](/docs/zh-CN/wallet/change-log#2020-04-02 "2020-04-02的直接链接")

  * 接口 `GET /sapi/v1/capital/config/getall` 返回内容新增字段： 
    * `minConfirm` 表示资产上账所需的最小确认数
    * `unLockConfirm` 表示资产解锁需所需确认数



* * *

## 2020-03-13[​](/docs/zh-CN/wallet/change-log#2020-03-13 "2020-03-13的直接链接")

  * 新增可选参数 `transactionFeeFlag` 于以下提币接口: 
    * `POST /sapi/v1/capital/withdraw/apply`
    * `POST /wapi/v3/withdraw.html`



* * *

## 2020-01-15[​](/docs/zh-CN/wallet/change-log#2020-01-15 "2020-01-15的直接链接")

  * 接口`POST /wapi/v3/withdraw.html` 新增参数 `withdrawOrderId`: 用户自定义提币 id

  * 接口`GET /wapi/v3/withdrawHistory.html` 返回内容新增字段 `withdrawOrderId`: 该笔提币的用户自定义 id




* * *

## 2019-12-25[​](/docs/zh-CN/wallet/change-log#2019-12-25 "2019-12-25的直接链接")

  * 新增请求时间间隔于以下接口  
`GET /sapi/v1/capital/withdraw/history`,  
`GET /wapi/v3/withdrawHistory.html`,  
`GET /sapi/v1/capital/deposit/hisrec` and  
`GET /wapi/v3/depositHistory.html`: _ 默认`startTime`为当前时间起 90 天前， 默认`endTime`为当前时间； _ 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不超过 90 天； * 同时提交`startTime` 与 `endTime`间隔不得超过 90 天.



* * *

## 2019-12-18[​](/docs/zh-CN/wallet/change-log#2019-12-18 "2019-12-18的直接链接")

  * 新增接口用以获取账户每日资产快照:  
`GET /sapi/v1/accountSnapshot`



* * *

## 2019-11-28[​](/docs/zh-CN/wallet/change-log#2019-11-28 "2019-11-28的直接链接")

  * 新增 SAPI 接口用以关闭账户站内划转功能：  
`POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)`
  * 新增 SAPI 接口用以开启账户站内划转功能：  
`POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)`



* * *

## 2019-10-29[​](/docs/zh-CN/wallet/change-log#2019-10-29 "2019-10-29的直接链接")

  * 新增钱包提币功能相关的 sapi 接口 
    * `POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)`: 提币。
    * `Get /sapi/v1/capital/withdraw/history (HMAC SHA256)`: 获取提币历史(支持多网络)。



* * *

## 2019-10-14[​](/docs/zh-CN/wallet/change-log#2019-10-14 "2019-10-14的直接链接")

  * 新增钱包功能相关的 sapi 接口 
    * `GET /sapi/v1/capital/config/getall (HMAC SHA256)`: 获取针对用户的所有币种信息。
    * `GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)`: 获取充值历史(支持多网络)。
    * `GET /sapi/v1/capital/deposit/address (HMAC SHA256)`: 获取充值地址(支持多网络).