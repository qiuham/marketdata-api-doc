---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/country-list
api_type: REST
updated_at: 2026-06-28 18:54:49.870513
---

# Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/deposit-provide-info#api-description "Direct link to API Description")

Submit questionnaire for local entities that require travel rule. The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not yet onboarded with GTR.

## HTTP Request[​](/docs/wallet/travel-rule/deposit-provide-info#http-request "Direct link to HTTP Request")

PUT `/sapi/v1/localentity/deposit/provide-info`

## Request Weight(UID)[​](/docs/wallet/travel-rule/deposit-provide-info#request-weightuid "Direct link to Request Weight\(UID\)")

**600**

## Request Parameters[​](/docs/wallet/travel-rule/deposit-provide-info#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
tranId| LONG| YES| Wallet tran ID  
questionnaire| STRING| YES| JSON format questionnaire answers.  
timestamp| LONG| YES|   
  
>   * Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## Response Example[​](/docs/wallet/travel-rule/deposit-provide-info#response-example "Direct link to Response Example")
    
    
    {  
        "trId": 765127651,  
        "accepted": true,  
        "info": "Deposit questionnaire accepted."  
    }

---

# 提交充值问卷(针对需要旅行规则的本地站)(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/deposit-provide-info#接口描述 "接口描述的直接链接")

提交充值问卷(针对需要旅行规则的本地站)。 只有来自私有钱包或尚未接入GTR的交易所的充值交易才需要提交充值问卷。

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/deposit-provide-info#http请求 "HTTP请求的直接链接")

PUT `/sapi/v1/localentity/deposit/provide-info`

## 请求权重(UID)[​](/docs/zh-CN/wallet/travel-rule/deposit-provide-info#请求权重uid "请求权重\(UID\)的直接链接")

**600**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/deposit-provide-info#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
tranId| LONG| YES| 充值记录ID  
questionnaire| STRING| YES| JSON 格式问卷内容  
timestamp| LONG| YES|   
  
>   * 每个本地站点的问卷内容都不一样，请参考`充值问卷内容`页。
>   * 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误，请尝检查Questionnaire格式并使用 `URL-encoded format`。
> 


## 响应示例[​](/docs/zh-CN/wallet/travel-rule/deposit-provide-info#响应示例 "响应示例的直接链接")
    
    
    {  
        "trId": 765127651,  
        "accepted": true,  
        "info": "Deposit questionnaire accepted."  
    }