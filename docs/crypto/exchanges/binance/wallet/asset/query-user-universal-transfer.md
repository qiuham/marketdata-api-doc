---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/query-user-universal-transfer
api_type: REST
updated_at: 2026-05-27 18:59:15.531293
---

# Query User Universal Transfer History(USER_DATA)

## API Description[​](/docs/wallet/asset/query-user-universal-transfer#api-description "Direct link to API Description")

Query User Universal Transfer History

## HTTP Request[​](/docs/wallet/asset/query-user-universal-transfer#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/transfer`

## Request Weight(IP)[​](/docs/wallet/asset/query-user-universal-transfer#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset/query-user-universal-transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
type| ENUM| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
current| INT| NO| Default 1  
size| INT| NO| Default 10, Max 100  
fromSymbol| STRING| NO|   
toSymbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
>   * `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
>   * Support query within the last 6 months only
>   * If `startTime`and `endTime` not sent, return records of the last 7 days by default
> 


## Response Example[​](/docs/wallet/asset/query-user-universal-transfer#response-example "Direct link to Response Example")
    
    
    {  
        "total": 2,  
        "rows": [  
            {  
                "asset": "USDT",  
                "amount": "1",  
                "type": "MAIN_UMFUTURE",  
                "status": "CONFIRMED", // status: CONFIRMED / FAILED / PENDING  
                "tranId": 11415955596,  
                "timestamp": 1544433328000  
            },  
            {  
                "asset": "USDT",  
                "amount": "2",  
                "type": "MAIN_UMFUTURE",  
                "status": "CONFIRMED",  
                "tranId": 11366865406,  
                "timestamp": 1544433328000  
            }  
        ]  
    }

---

# 查询用户万向划转历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/query-user-universal-transfer#接口描述 "接口描述的直接链接")

查询用户万向划转历史

## HTTP请求[​](/docs/zh-CN/wallet/asset/query-user-universal-transfer#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/transfer`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/query-user-universal-transfer#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset/query-user-universal-transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
type| ENUM| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
current| INT| NO| 默认 1  
size| INT| NO| 默认 10, 最大 100  
fromSymbol| STRING| NO|   
toSymbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `fromSymbol` 必须要发送，当类型为 ISOLATEDMARGIN_MARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN
>   * `toSymbol` 必须要发送，当类型为 MARGIN_ISOLATEDMARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN
>   * 仅支持查询最近半年（6个月）数据
>   * 若`startTime`和`endTime`没传，则默认返回最近7天数据
> 


## 响应示例[​](/docs/zh-CN/wallet/asset/query-user-universal-transfer#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 2,  
        "rows": [  
            {  
                "asset": "USDT",  
                "amount": "1",  
                "type": "MAIN_UMFUTURE",  
                "status": "CONFIRMED", // status: CONFIRMED / FAILED / PENDING  
                "tranId": 11415955596,  
                "timestamp": 1544433328000  
            },  
            {  
                "asset": "USDT",  
                "amount": "2",  
                "type": "MAIN_UMFUTURE",  
                "status": "CONFIRMED",  
                "tranId": 11366865406,  
                "timestamp": 1544433328000  
            }  
        ]  
    }