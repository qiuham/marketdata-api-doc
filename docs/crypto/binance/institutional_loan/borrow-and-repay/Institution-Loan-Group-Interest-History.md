---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History
api_type: REST
updated_at: 2026-06-30 19:11:04.293655
---

# Query Loan Group Max Borrowable (USER_DATA)

## API Description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#api-description "Direct link to API Description")

Query the maximum borrowable amount of a given asset for an institutional loan risk unit. The response amount is calculated based on the collateral ratio of the borrowed token, total net equity and maintenance margin of the risk unit, and the pre-set maximum borrow limit.

This endpoint can be accessed using the API key from **either the parent or the credit account**.

  * If the API key belongs to the **credit account** , `groupId` is optional. When omitted, the member's own risk unit is used; when provided, it must match the member's risk unit, otherwise an empty result is returned.
  * If the API key belongs to the **parent account** , `groupId` is **required** and must be owned by the parent account, otherwise an empty result is returned.
  * If the caller is neither the parent account nor the credit member of the group (e.g., a collateral member, or no matching risk unit), `maxBorrowableAmount` is returned as empty/null.



## HTTP Request[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/loan-group/max-borrowable`

## Request Weight[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#request-weight "Direct link to Request Weight")

**100(IP)**

## Request Parameters[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| NO| Loan group id. Optional when the key belongs to the credit member; required when the key belongs to the parent account.  
assetName| STRING| YES| Asset to borrow, e.g., `USDT`. Case-insensitive (normalized to upper-case). Must be a borrowable asset, otherwise an error is returned.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#response-example "Direct link to Response Example")
    
    
    {  
      "maxBorrowableAmount": "12345.67890000"  
    }  
    

## Response Parameters[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#response-parameters "Direct link to Response Parameters")

Field| Type| Description  
---|---|---  
maxBorrowableAmount| BIGDECIMAL| Max borrowable amount of the asset for the risk unit. Empty/null when the caller has no matching risk unit.

---

# 查询风险单位最大可借金额 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#接口描述 "接口描述的直接链接")

查询机构借贷风险单位内指定币种的最大可借金额。返回金额基于以下因素综合计算得出:借款币种的质押率、风险单位内的净抵押品累计总额、总维持保证金,以及预设的最大借款上限。

本接口可使用母账户或放贷账户的 API Key 进行访问。

  * 若 API key 属于 **放贷账户 (credit account)** :`groupId` 可选。不传时使用该成员所属的风险单位;传了则必须与成员所属风险单位一致,否则返回空结果。
  * 若 API key 属于 **母账户** :`groupId` **必传** ,且必须归属于该母账户,否则返回空结果。
  * 若调用方既不是母账户也不是该风险单位的放贷账户(如抵押子账户,或没有匹配的风险单位):`maxBorrowableAmount` 返回空/null。



## HTTP 请求[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#http-请求 "HTTP 请求的直接链接")

GET `/sapi/v1/margin/loan-group/max-borrowable`

## 请求权重[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#请求权重 "请求权重的直接链接")

**100(IP)**

## 请求参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#请求参数 "请求参数的直接链接")

参数| 类型| 是否必填| 描述  
---|---|---|---  
groupId| LONG| 否| 风险单位组 ID。key 为 credit 成员时可选;key 为母账户时必填。  
assetName| STRING| 是| 借贷币种,如 `USDT`。大小写不敏感(自动转大写)。必须是可借币种,否则报错。  
recvWindow| LONG| 否| 不能大于 60000  
timestamp| LONG| 是|   
  
## 响应示例[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#响应示例 "响应示例的直接链接")
    
    
    {  
      "maxBorrowableAmount": "12345.67890000"  
    }  
    

## 响应参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Max-Borrowable#响应参数 "响应参数的直接链接")

字段| 类型| 描述  
---|---|---  
maxBorrowableAmount| BIGDECIMAL| 该风险单位下指定币种的最大可借金额。无匹配的风险单位时返回空/null。