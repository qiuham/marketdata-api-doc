---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History
api_type: Account
updated_at: 2026-05-27 19:02:36.955478
---

# Query Universal Transfer History (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Query-Universal-Transfer-History#api-description "Direct link to API Description")

Query Universal Transfer History

## HTTP Request[​](/docs/sub_account/asset-management/Query-Universal-Transfer-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/universalTransfer`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Query-Universal-Transfer-History#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Query-Universal-Transfer-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromEmail| STRING| NO|   
toEmail| STRING| NO|   
clientTranId| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| NO| Default 1  
limit| INT| NO| Default 500, Max 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * fromEmail and toEmail cannot be sent at the same time.
>   * Return fromEmail equal master account email by default.
>   * The query time period must be less than 7 days.
>   * If startTime and endTime not sent, return records of the last 7 days by default.
> 


## Response Example[​](/docs/sub_account/asset-management/Query-Universal-Transfer-History#response-example "Direct link to Response Example")
    
    
    {  
        "result": [  
            {  
                "tranId": 92275823339,  
                "fromEmail": "abctest@gmail.com",  
                "toEmail": "deftest@gmail.com",  
                "asset": "BNB",  
                "amount": "0.01",  
                "createTimeStamp": 1640317374000,  
                "fromAccountType": "USDT_FUTURE",  
                "toAccountType": "SPOT",  
                "status": "SUCCESS",  
                "clientTranId": "test"  
            }  
        ],  
        "totalCount": 1  
    }

---

# 查询子母账户万能划转历史 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Query-Universal-Transfer-History#接口描述 "接口描述的直接链接")

查询子母账户万能划转历史

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Query-Universal-Transfer-History#http��请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/universalTransfer`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Query-Universal-Transfer-History#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Query-Universal-Transfer-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromEmail| STRING| NO|   
toEmail| STRING| NO|   
clientTranId| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| NO| 默认 1  
limit| INT| NO| 默认 500, 最大 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 本查询接口只可以单边查询，fromEmail 和 toEmail 不能同时传入。
>   * 若 fromEmail 和 toEmail 都未传，默认返回 fromEmail 为母账户的划转记录。
>   * 若 startTime 和 endTime 都未传，则只可查询最近7天的记录。
>   * 查询时间范围最大不得超过7天。
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Query-Universal-Transfer-History#响应示例 "响应示例的直接链接")
    
    
    {  
        "result": [  
            {  
                "tranId": 92275823339,  
                "fromEmail": "abctest@gmail.com",  
                "toEmail": "deftest@gmail.com",  
                "asset": "BNB",  
                "amount": "0.01",  
                "createTimeStamp": 1640317374000,  
                "fromAccountType": "USDT_FUTURE",  
                "toAccountType": "SPOT",  
                "status": "SUCCESS",  
                "clientTranId": "test"  
            }  
        ],  
        "totalCount": 1  
    }