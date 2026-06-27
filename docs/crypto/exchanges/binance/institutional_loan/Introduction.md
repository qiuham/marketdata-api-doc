---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/Introduction
api_type: REST
updated_at: 2026-05-27 19:01:05.547410
---

# Close Risk Unit (TRADE)

## API Description[​](/docs/institutional_loan/account/Institution-Loan-Group-Close#api-description "Direct link to API Description")

The closure of the Institutional Loan risk unit can only be initiated by API calls from the credit account. If the closure is successful all the collateral accounts will be unlinked. Please note the following conditions must be met:

  * The Institution Loan risk unit is active.
  * The outstanding institutional loan liabilities for that particular risk unit have been repaid.



## HTTP Request[​](/docs/institutional_loan/account/Institution-Loan-Group-Close#http-request "Direct link to HTTP Request")

DELETE /sapi/v1/margin/loan-group

## Request Weight[​](/docs/institutional_loan/account/Institution-Loan-Group-Close#request-weight "Direct link to Request Weight")

1000(UID)

## Request Parameters[​](/docs/institutional_loan/account/Institution-Loan-Group-Close#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| YES| Risk unit unique identifier  
  
## Response Example[​](/docs/institutional_loan/account/Institution-Loan-Group-Close#response-example "Direct link to Response Example")
    
    
    {  
      "groupId": 10001,  
      "status": "CLOSED"  
    }  
    

## Response detail description:[​](/docs/institutional_loan/account/Institution-Loan-Group-Close#response-detail-description "Direct link to Response detail description:")

Parameter| Type| Description  
---|---|---  
groupId| LONG| Risk unit unique identifier  
status| STRING| CLOSED:This risk unit has been closed successfully

---

# 关闭风险单位 (TRADE)

## 接口描述[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Close#接口描述 "接口描述的直接链接")

关闭操作仅支持通过机构借贷子账户 API 执行。成功关闭后，系统将自动解除该风险单位与所有抵押账户的关联。请注意，操作前需满足以下条件：

  * 机构贷单位处于生效活跃状态。
  * 已全额偿还此风险单位内贷款及利息。



## HTTP 请求[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Close#http-请求 "HTTP 请求的直接链接")

DELETE /sapi/v1/margin/loan-group

## 请求权重[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Close#请求权重 "请求权重的直接链接")

1000(UID)

## 请求参数[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Close#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
groupId| LONG| YES| 唯一风险单位标识符  
  
## 响应示例[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Close#响应示例 "响应示例的直接链接")
    
    
    {  
      "groupId": 10001,  
      "status": "CLOSED"  
    }  
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Close#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
groupId| LONG| 唯一风险单位标识符  
status| STRING| CLOSED: 此风险单位已成功关闭