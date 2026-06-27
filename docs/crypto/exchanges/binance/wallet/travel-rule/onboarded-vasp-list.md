---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/onboarded-vasp-list
api_type: REST
updated_at: 2026-05-27 19:00:07.121302
---

# Withdraw (for local entities that require travel rule) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/withdraw#api-description "Direct link to API Description")

Submit a withdrawal request for local entities that required travel rule.

## HTTP Request[​](/docs/wallet/travel-rule/withdraw#http-request "Direct link to HTTP Request")

POST `/sapi/v1/localentity/withdraw/apply`

## Request Weight(UID)[​](/docs/wallet/travel-rule/withdraw#request-weightuid "Direct link to Request Weight\(UID\)")

**600**

## Request Parameters[​](/docs/wallet/travel-rule/withdraw#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
coin| STRING| YES|   
withdrawOrderId| STRING| NO| withdrawID defined by the client (i.e. client's internal withdrawID)  
network| STRING| NO|   
address| STRING| YES|   
addressTag| STRING| NO| Secondary address identifier for coins like XRP,XMR etc.  
amount| DECIMAL| YES|   
transactionFeeFlag| BOOLEAN| NO| When making internal transfer, `true` for returning the fee to the destination account; `false` for returning the fee back to the departure account. Default `false`.  
name| STRING| NO| Description of the address. Address book cap is 200, space in name should be encoded into `%20`  
walletType| INTEGER| NO| The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
questionnaire| STRING| YES| JSON format questionnaire answers.  
  
>   * If `network` not send, return with default network of the coin, but if the address could not match default network, the withdraw will be rejected.
>   * You can get `network` and `isDefault` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.
>   * Questionnaire is different for each local entity, please refer to the `Withdraw Questionnaire Contents` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## Response Example[​](/docs/wallet/travel-rule/withdraw#response-example "Direct link to Response Example")
    
    
    {  
        "trId": 123456,                         // The travel rule record Id  
        "accpted": true,                        // Whether the withdraw request is accepted  
        "info": "Withdraw request accepted"     // The detailed infomation of the withdrawal result.  
    }

---

# 提币(针对需要旅行规则的本地站)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/withdraw#接口描述 "接口描述的直接链接")

向需要旅行规则的本地站发起提币请求

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/withdraw#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/localentity/withdraw/apply`

## 请求权重(UID)[​](/docs/zh-CN/wallet/travel-rule/withdraw#请求权重uid "请求权重\(UID\)的直接链接")

**600**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/withdraw#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
coin| STRING| YES|   
withdrawOrderId| STRING| NO| 客户端内部定义的提币ID.  
network| STRING| NO| 提币网络  
address| STRING| YES| 提币地址  
addressTag| STRING| NO| 某些币种例如 XRP,XMR 允许填写次级地址标签  
amount| DECIMAL| YES| 数量  
transactionFeeFlag| BOOLEAN| NO| 当站内转账时免手续费, `true`: 手续费归资金转入方; `false`: 手续费归资金转出方; . 默认 `false`.  
name| STRING| NO| 地址的备注，填写该参数后会加入该币种的提现地址簿。地址簿上限为200，超出后会造成提现失败。地址中的空格需要encode成`%20`  
walletType| INTEGER| NO| 表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
questionnaire| STRING| YES| JSON 格式的问卷回答。  
  
>   * 如果没有传入 `network`, 则使用对应币种的默认网络, 如果地址格式不能匹配默认网络, 提币将被拒绝。
>   * 网络、默认网络的配置列表可以通过以下接口获取 `Get /sapi/v1/capital/config/getall (HMAC SHA256)`。
>   * 每个本地站点的问卷内容都不一样，请参考`提币问卷内容`页。
>   * 如果API返回 `Questionnaire format not valid.` 或 `Questionnaire must not be blank` 错误，请尝检查Questionnaire格式并使用 `URL-encoded format`。
> 


## 响应示例[​](/docs/zh-CN/wallet/travel-rule/withdraw#响应示例 "响应示例的直接链接")
    
    
    {  
        "trId": 123456,                         // Travel Rule记录ID  
        "accpted": true,                        // 提币请求是否被接受  
        "info": "Withdraw request accepted"     // 提现结果的详细信息  
    }