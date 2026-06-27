---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/deposit-history
api_type: REST
updated_at: 2026-05-27 18:59:57.863262
---

# Deposit History V2 (for local entities that required travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/deposit-history-v2#api-description "Direct link to API Description")

Fetch deposit history for local entities that with required travel rule information.

## HTTP Request[​](/docs/wallet/travel-rule/deposit-history-v2#http-request "Direct link to HTTP Request")

GET `/sapi/v2/localentity/deposit/history`

## Request Weight(IP)[​](/docs/wallet/travel-rule/deposit-history-v2#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/deposit-history-v2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
depositId| STRING| NO| Comma(,) separated list of wallet tran Ids.  
txId| STRING| NO| Comma(,) separated list of transaction Ids.  
network| STRING| NO|   
coin| STRING| NO|   
retrieveQuestionnaire| BOOLEAN| NO| true: return `questionnaire` within response.  
startTime| LONG| NO| Default: 90 days from current timestamp  
endTime| LONG| NO| Default: present timestamp  
offset| INT| NO| Default:0  
limit| INT| NO| Default:1000, Max:1000  
timestamp| LONG| YES|   
  
>   * Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
>   * If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.
>   * Please, note that due to network-specific characteristics, the returned source address may be inaccurate. If multiple source addresses are found, only the first one will be returned.
> 


## Response Example[​](/docs/wallet/travel-rule/deposit-history-v2#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "depositId": "4615328107052018945",  
            "amount": "0.01",  
            "network": "AVAXC",  
            "coin": "AVAX",  
            "depositStatus": 1,  
            "travelRuleReqStatus": 0,                                                         // 0:PASS,2:REJECTED,3:PENDING,-1:FAILED  
            "address": "0x0010627ab66d69232f4080d54e0f838b4dc3894a",  
            "addressTag": "",  
            "txId": "0xdde578983015741eed764e7ca10defb5a2caafdca3db5f92872d24a96beb1879",  
            "transferType": 0,  
            "confirmTimes": "12/12",  
            "requireQuestionnaire": false,                                                    // true: This deposit require user to answer questionnaire to get it credited  
                                                                                              // false: This deposit doesn't require user to answer questionnaire as it's already completed or information has been verified  
            "questionnaire": {  
                "vaspName": "BINANCE",  
                "depositOriginator": 0  
            },  
            "insertTime": 1753053392000  
        }  
    ]

---

# 获取充值历史V2(针对需要旅行规则的本地站)(支持多网络)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/deposit-history-v2#接口描述 "接口描述的直接链接")

获取充值历史(针对需要旅行规则的本地站)(支持多网络)

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/deposit-history-v2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/localentity/deposit/history`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/deposit-history-v2#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/deposit-history-v2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
depositId| STRING| NO| 入金记录ID，支持多条查询，以半角逗号(,) 分隔  
txId| STRING| NO| 链上TxId，支持多条查询，以半角逗号(,) 分隔  
network| STRING| NO|   
coin| STRING| NO|   
retrieveQuestionnaire| BOOLEAN| NO| true:返回的记录中带有问卷内容，false/缺省.  
startTime| LONG| NO| 默认当前时间90天前的时间戳  
endTime| LONG| NO| 默认当前时间戳  
offset| INTEGER| NO| 默认:0  
limit| INTEGER| NO| 默认:1000，最大1000  
timestamp| LONG| YES|   
  
>   * 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不超过90天。
>   * 同时提交`startTime` 与 `endTime`间隔不得超过90天。
>   * 请注意，由于网络特定的特性，返回的源地址可能不准确。 如果找到多个源地址，则仅返回第一个地址。
> 


## 响应示例[​](/docs/zh-CN/wallet/travel-rule/deposit-history-v2#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "depositId": "4615328107052018945",  
            "amount": "0.01",  
            "network": "AVAXC",  
            "coin": "AVAX",  
            "depositStatus": 1,  
            "travelRuleReqStatus": 0,                                                         // 0:PASS,2:REJECTED,3:PENDING,-1:FAILED  
            "address": "0x0010627ab66d69232f4080d54e0f838b4dc3894a",  
            "addressTag": "",  
            "txId": "0xdde578983015741eed764e7ca10defb5a2caafdca3db5f92872d24a96beb1879",  
            "transferType": 0,  
            "confirmTimes": "12/12",  
            "requireQuestionnaire": false,                                                    // true: This deposit require user to answer questionnaire to get it credited  
                                                                                              // false: This deposit doesn't require user to answer questionnaire as it's already completed or information has been verified  
            "questionnaire": {  
                "vaspName": "BINANCE",  
                "depositOriginator": 0  
            },  
            "insertTime": 1753053392000  
        }  
    ]