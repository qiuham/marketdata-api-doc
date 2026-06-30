---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/error-code
api_type: REST
updated_at: 2026-06-30 19:11:16.322509
---

# Risk Unit Transfer(TRADE)

## API Description[​](/docs/institutional_loan/transfer#api-description "Direct link to API Description")

When specified risk unit LTV thresholds and/or the relevant product transfer out rules are met, the Risk Unit Transfer API allows users to perform the following:

  * Transfer of assets from margin collateral/credit accounts to spot accounts with the same Spot UID. This endpoint is accessible via each of the credit/collateral accounts with its API Key or parent account .



Please Note: To transfer funds out of the Institutional Loan Risk Unit, first transfer to the spot wallet using the dedicated Risk Unit Transfer API. After that, use the [Universal Transfer API](https://developers.binance.com/docs/sub_account/asset-management/Universal-Transfer) to move the assets to an account outside of the risk unit.

For all other designated use cases shown below, please use the [Universal Transfer API](https://developers.binance.com/docs/sub_account/asset-management/Universal-Transfer).

  * Transfer assets between Credit Account and other Margin Collateral Accounts within the risk unit without LTV restrictions. Please see [Universal Transfer API](https://developers.binance.com/docs/sub_account/asset-management/Universal-Transfer), this needs to be done via master account API key.
  * Transfers between Spot collateral account and accounts outside of the risk unit.



## HTTP Request[​](/docs/institutional_loan/transfer#http-request "Direct link to HTTP Request")

POST /sapi/v1/margin/loan-group/transfer-out

## Request Weight[​](/docs/institutional_loan/transfer#request-weight "Direct link to Request Weight")

1(IP)

## Request Parameters[​](/docs/institutional_loan/transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
subEmail| STRING| NO| When the parent account calls this endpoint, the subEmail field is mandatory. If left empty, error code -27026 will be returned.  
When a credit or collateral account calls this endpoint, the subEmail field may be omitted and will default to the account's own subEmail.  
If the wrong subEmail is inputted, error code -3003 will be returned.  
asset| STRING| YES| Asset Name , USDT or USDC  
amount| DECIMAL| YES| Transfer amount of the asset. The real transferred amount = min(risk unit max transfer amount, collateral account max transfer amount).  
  
## Response Example[​](/docs/institutional_loan/transfer#response-example "Direct link to Response Example")

None

## Error Code Description:[​](/docs/institutional_loan/transfer#error-code-description "Direct link to Error Code Description:")

  * -27025 : Please try again until the previous transaction is completed.
  * -27026 : Receiver UID is not within the Institutional Loan risk unit.
  * -27027 : The receiver UID margin wallet has not been enabled.
  * -27028 : Exceed the max transfer out amount, which is min(Risk Unit max transfer out, Collateral Account max transfer out). Risk Unit max transfer out can be checked via “Query Risk Unit Details (USER_DATA)” API endpoint.
  * -27029 : Institution loan collateral accounts can only transfer assets to other collateral accounts’ margin accounts within the same risk unit.

---

# 风险单位资金划转 (TRADE)

## 接口描述[​](/docs/zh-CN/institutional_loan/transfer#接口描述 "接口描述的直接链接")

当达到特定的风险单位 LTV 阈值和/或相关产品的转出规则时，风险单位资金划转 API 允许用户执行以下操作：

  * 将资产从杠杆抵押账户或放贷账户转至相同现货 UID 下的现货账户， 此接口可支持单个抵押账户或放贷账户调用，也可由母账户调用。



请注意：要将资金转出机构借贷风险单位，首先要使用机构借贷特定的转账 API 将资金转入现货钱包。然后，使用[万向转账 API](https://developers.binance.com/docs/zh-CN/sub_account/asset-management/Universal-Transfer)将资产转移到风险单元之外的账户。

此外的划转场景，请您使用[万向转账 API操作。](https://developers.binance.com/docs/zh-CN/sub_account/asset-management/Universal-Transfer)

  * 资金在放贷账户与风险单位内其他杠杆抵押账户之间划转，此划转不受转出 LTV 的限制。您可以查看[万向划转 API 文档](https://developers.binance.com/docs/zh-CN/sub_account/asset-management/Universal-Transfer)了解更多详情，此接口需要通过母账户 API Key 操作。
  * 现货账户与风险单位外的账户之间转账。



## HTTP请求[​](/docs/zh-CN/institutional_loan/transfer#http请求 "HTTP请求的直接链接")

POST /sapi/v1/margin/loan-group/transfer-out

## 请求权重[​](/docs/zh-CN/institutional_loan/transfer#请求权重 "请求权重的直接链接")

1(IP)

## 请求参数[​](/docs/zh-CN/institutional_loan/transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
subEmail| STRING| NO| 抵押子账户或放贷子账户的邮箱地址  
母账户调用该接口时，subEmail必填，为空则报错；  
放贷账户或抵押账户调用该接口时，subEmail可为空，默认为其本身subEmail.  
asset| STRING| YES| 资产名称，如 USDT 或 USDC  
amount| DECIMAL| YES| 转出金额。 注意 实际可转出金额取值于 min(风险单位最大可转出金额, 抵押账号最大可转出金额)， 两者取小。  
  
## 响应示例[​](/docs/zh-CN/institutional_loan/transfer#响应示例 "响应示例的直接链接")

无

## 常见错误代码：[​](/docs/zh-CN/institutional_loan/transfer#常见错误代码 "常见错误代码：的直接链接")

  1. -27025 : 前一笔交易还未完成，请稍后再试。
  2. -27026 : 接收账号不在当前风险单位内。
  3. -27027 : 接收账号没有开通杠杆账户。
  4. -27028 : 超出最大可转出金额。实际最大可转出金额取值于 min(风险单位最大可转出金额, 抵押账号最大可转出金额)， 两者取小。请通过接口“查询风险单位详情”获取最大转出金额。
  5. -27029 : 抵押账户只能划转资金到风险单位内其他杠杆账户对应的抵押账户。