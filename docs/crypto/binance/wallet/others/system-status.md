---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/others/system-status
api_type: REST
updated_at: 2026-06-28 18:54:42.067627
---

# Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/broker-deposit-provide-info#api-description "Direct link to API Description")

Submit questionnaire for brokers of local entities that require travel rule. The questionnaire is only applies to transactions from un-hosted wallets or VASPs that are not yet onboarded with GTR.

## HTTP Request[​](/docs/wallet/travel-rule/broker-deposit-provide-info#http-request "Direct link to HTTP Request")

PUT `/sapi/v1/localentity/broker/deposit/provide-info`

## Request Weight(UID)[​](/docs/wallet/travel-rule/broker-deposit-provide-info#request-weightuid "Direct link to Request Weight\(UID\)")

**600**

## Request Parameters[​](/docs/wallet/travel-rule/broker-deposit-provide-info#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
subAccountId| STRING| YES| External user ID.  
depositId| STRING| YES| Wallet deposit ID.  
questionnaire| STRING| YES| JSON format questionnaire answers.  
beneficiaryPii| STRING| YES| JSON format beneficiary Pii.  
network| STRING| NO|   
coin| STRING| NO|   
amount| BigDecimal| NO|   
address| STRING| NO|   
addressTag| STRING| NO|   
timestamp| LONG| YES| Epoch Sec  
signature| STRING| YES| Must be the last parameter  
  
>   * Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## StandardPii[​](/docs/wallet/travel-rule/broker-deposit-provide-info#standardpii "Direct link to StandardPii")

**For Natural Person**

Name| Type| Mandatory| Description  
---|---|---|---  
piiType| INTEGER| YES| Fix to 0: Natural Person  
latinNames| List| YES| In case a person have complicated names or multiple names, this parameter is a list  
localNames| List| NO| In case a person have complicated names or multiple names, this parameter is a list  
nationality| STRING| NO|   
residenceCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
dateOfBirth| STRING| NO| yyyy-mm-dd. Not required but strongly recommended. Providing DOB could greatly reduce false positive rate during risk checking process.  
placeOfBirth| STRING| NO|   
address| STRING| NO|   
  
**For Legal Person**

Name| Type| Mandatory| Description  
---|---|---|---  
piiType| INTEGER| YES| Fix to 1: Legal Person  
latinName| STRING| YES| It's company name for Legal Person  
localName| STRING| NO|   
registrationCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
registrationDate| STRING| NO| yyyy-mm-dd. Not required but strongly recommended.  
address| STRING| NO|   
walletAddress| STRING| NO|   
walletTag| STRING| NO|   
  
**PiiName**

Name| Type| Mandatory| Description  
---|---|---|---  
firstName| STRING| YES| Mandatory for Natural person  
middleName| STRING| NO|   
lastName| STRING| NO|   
  
## Response Example[​](/docs/wallet/travel-rule/broker-deposit-provide-info#response-example "Direct link to Response Example")
    
    
    {  
        "trId": 765127651,  
        "accepted": true,  
        "info": "Deposit questionnaire accepted."  
    }

---

# 提交经纪商充值问卷(针对需要旅行规则的本地站的经纪商)(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#接口描述 "接口描述的直接链接")

提交充值问卷(针对需要旅行规则的本地站的经纪商)。 只有来自私有钱包或尚未接入GTR的交易所的充值交易才需要提交充值问卷。

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#http请求 "HTTP请求的直接链接")

PUT `/sapi/v1/localentity/broker/deposit/provide-info`

## 请求权重(UID)[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#请求权重uid "请求权重\(UID\)的直接链接")

**600**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
subAccountId| STRING| YES| 外部UID  
depositId| STRING| YES| 充值记录ID.  
questionnaire| STRING| YES| JSON 格式的问卷回答。  
beneficiaryPii| STRING| YES| JSON 格式的收款人个人身份信息。  
network| STRING| NO|   
coin| STRING| NO|   
amount| BigDecimal| NO|   
address| STRING| NO|   
addressTag| STRING| NO|   
timestamp| LONG| YES|   
signature| STRING| YES| 必须是最后一个参数.  
  
>   * 每个本地站点的问卷内容都不一样,请参考`充值问卷内容`页。
>   * 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误,请尝检查Questionnaire格式并使用 `URL-encoded format`。
> 


## 标准个人身份信息[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#标准个人身份信息 "标准个人身份信息的直接链接")

**自然人**

名称| 类型| 是否必需| 描述  
---|---|---|---  
piiType| INTEGER| YES| 固定为0：自然人  
latinNames| List| YES| 如果一个人有复杂的姓名或多个名字，此参数为一个列表  
localNames| List| NO| 如果一个人有复杂的姓名或多个名字，此参数为一个列表  
nationality| STRING| NO|   
residenceCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
dateOfBirth| STRING| NO| yyyy-mm-dd. 非必填，但强烈推荐. 提供出生日期可以大大降低风险审查过程中的误报率.  
placeOfBirth| STRING| NO|   
address| STRING| NO|   
  
**法人**

名称| 类型| 是否必需| 描述  
---|---|---|---  
piiType| INTEGER| YES| 固定为1：法人  
latinName| STRING| YES| 如果是法人，则为公司名称  
localName| STRING| NO|   
registrationCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
registrationDate| STRING| NO| yyyy-mm-dd. 非必填，但强烈推荐.  
address| STRING| NO|   
walletAddress| STRING| NO|   
walletTag| STRING| NO|   
  
**个人身份信息姓名**

名称| 类型| 是否必需| 描述  
---|---|---|---  
firstName| STRING| YES| 自然人必填  
middleName| STRING| NO|   
lastName| STRING| NO|   
  
## 响应示例[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#响应示例 "响应示例的直接链接")
    
    
    {  
        "trId": 765127651,                            // Travel Rule记录ID  
        "accepted": true,                             // 提交问卷请求是否被接受  
        "info": "Deposit questionnaire accepted."     // 提交问卷结果的详细信息  
    }