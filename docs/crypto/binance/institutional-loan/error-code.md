---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/institutional-loan/error-code
api_type: REST
updated_at: 2026-11-13 20:31:22.015114
---

# Error Codes

Institutional Loan endpoints use the standard SAPI error format: the error code is in the `code` field and a human-readable message is in the `msg` field.

Standard SAPI errors, such as signature, timestamp and parameter checks (for example `-1022` or `-1102`), also apply to these endpoints. See the [SAPI error codes](/en/docs/products/wallet/error-code) for the full list.

The codes below are specific to Institutional Loan. Placeholders such as `{0}` are replaced with actual values in the returned message.

## -27000

  * Illegal argument or invalid input.



## -27001

  * Loan group not found



## -27002

  * Maximum allowed collateral accounts is {0}.



## -27003

  * The account(s) have been linked to another institutional loan risk unit.



## -27004

  * The collateral account should be a sub-account under the same parent account.



## -27005

  * The account should open a margin account first.



## -27006

  * Credit account type must be Portfolio Margin or Cross Margin



## -27007

  * Collateral account cannot be the same as CREDIT_ACCOUNT.



## -27008

  * For newly added collateral account, the net equity {0} must be greater than or equal to maintenance margin {1}.



## -27009

  * The requested borrow amount exceeds the maximum allowed limit. Maximum borrowable for asset {0} is {1}, but request {2}.



## -27010

  * Credit account not found in risk unit with GroupID {0}.



## -27011

  * No liability found in the risk unit with GroupID {0}.



## -27012

  * User has insufficient available margin to borrow asset {1}: requested {2}, available {3}.



## -27013

  * Collateral account type {0} is not supported to be added as collateral account for the user.



## -27014

  * Insufficient balance in lending account for asset {0}.



## -27015

  * Insufficient balance in balance for asset {0}.



## -27016

  * Illegal asset quantity precision for asset {0}.



## -27017

  * The requested loan asset: {0} is not supported.



## -27018

  * Liabilities of (amount: {1}) Asset {0} in the risk unit has not been fully repaid. The risk unit cannot be closed.



## -27019

  * The account is not part of the risk unit {1}, and thus cannot be removed.



## -27020

  * LTV of risk unit {0} is too high ({1}), and exceeds initial LTV threshold {2}.



## -27021

  * The credit account receiving the institutional loan cannot be removed from risk unit {0}.



## -27022

  * Risk unit {0} for the institutional loan must contain one credit account receiving the loan and one standard collateral account member.



## -27023

  * Loan is not successful, please try again or contact Margin team for assistance.



## -27024

  * The risk unit is in liquidation, please try again later.



## -27025

  * Please try again until the previous transaction is completed.



## -27026

  * Receiver UID is not within the Institutional Loan risk unit.



## -27027

  * The receiver UID margin wallet has not been enabled.



## -27028

  * Exceed the max transfer out amount, which is min(Risk Unit max transfer out, Collateral Account max transfer out). Risk Unit max transfer out can be checked via “Query Risk Unit Details (USER_DATA)” API endpoint.



## -27029

  * Institution loan collateral accounts can only transfer assets to other collateral accounts’ margin account within the same risk unit.



## -27030

  * Cannot add managed sub account into risk unit via API, please contact margin team for assistance.



## -27031

  * The new borrow or asset transfer within the risk unit can only be executed two minutes after the new collateral account being added into the Institution loan risk unit.



Was this page helpful?

Last modified on November 12, 2026

[Quick Start](/en/docs/products/institutional-loan/quick-start)[Introduction](/en/docs/products/alpha/introduction)

---

# 错误代码

机构借贷接口使用标准 SAPI 错误格式：错误码位于 `code` 字段，可读的错误信息位于 `msg` 字段。

标准 SAPI 错误（如签名、时间戳及参数校验，例如 `-1022` 或 `-1102`）同样适用于这些接口，完整列表请参阅 [SAPI 错误代码](/zh-CN/docs/products/wallet/error-code)。

以下为机构借贷专属错误码。`{0}` 等占位符在实际返回的信息中会被替换为具体数值。

## -27000

  * 输入参数无效



## -27001

  * 机构贷没有找到



## -27002

  * 最大可抵押账号数量为 {0}



## -27003

  * 该账号已在其他机构贷风险单元使用



## -27004

  * 抵押账号必须在同一母账户下的子账号



## -27005

  * 该账号还未开通杠杆账号



## -27006

  * 信用贷账号必须为统一账户或全仓杠杆账号



## -27007

  * 普通借贷账号不能和信用贷账号相同



## -27008

  * 新加入的抵押账号，净资产不能小于维持保证金金额



## -27009

  * 请求的借贷额度超过最大可借额度，币种 {0} 最大可借为 {1}，请求数量为 {2}



## -27010

  * 风险单元 {0} 下未找到信用贷账号



## -27011

  * 风险单元 {0} 下没有负债



## -27012

  * 用户的维持保证金不足，借贷币种 {1}，请求数量 {2}，可用数量 {3}



## -27013

  * 抵押账号类型 {0} 不正确



## -27014

  * 借贷账户的资产 {0} 余额不足



## -27015

  * 资产 {0} 余额不足



## -27016

  * 资产 {0} 精度不正确



## -27017

  * 请求资产 {0} 不支持借贷



## -27018

  * 风险单元无法关闭，因为单元内的负债资产 {0} 没有完全还清，还剩 {1}



## -27019

  * 账户不在风险单元 {1} 内，无法移除



## -27020

  * 风险单元 {0} 的 LTV 过高（{1}），超出初始 LTV 阈值 {2}



## -27021

  * 风险单位{0}内接收机构贷借款的放贷账户无法移除



## -27022

  * 风险单位{0}必须包含一个放贷账户来接收机构贷借款和一个普通抵押账户



## -27023

  * 借款失败，请重试或联系杠杆交易团队获得帮助



## -27024

  * 当前风险单位正在强平中，请稍后再试。



## -27025

  * 前一笔交易还未完成，请稍后再试。



## -27026

  * 接收账号不在当前风险单位内。



## -27027

  * 接收账号没有开通杠杆账户。



## -27028

  * 超出最大可转出金额。实际最大可转出金额取值于 min(风险单位最大可转出金额, 抵押账号最大可转出金额)， 两者取小。请通过接口“查询风险单位详情”获取最大转出金额。



## -27029

  * 抵押账户只能划转资金到风险单位内其他杠杆账户对应的抵押账户。



## -27030

  * 管理子账户不能通过API添加到风险单位。请联系杠杆团队获得支持



## -27031

  * 新的抵押账户添加到风险单位后，2分钟后才能进行借贷或资产划转等操作。



此页面是否有帮助？

Last modified on November 12, 2026

[快速开始](/zh-CN/docs/products/institutional-loan/quick-start)[概述](/zh-CN/docs/products/alpha/introduction)