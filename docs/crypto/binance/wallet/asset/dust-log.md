---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/dust-log
api_type: REST
updated_at: 2026-06-29 19:11:40.457283
---

# Query User Delegation History(For Master Account)(USER_DATA)

## API Description[​](/docs/wallet/asset/query-user-delegation#api-description "Direct link to API Description")

Query User Delegation History

## HTTP Request[​](/docs/wallet/asset/query-user-delegation#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/custody/transfer-history`

## Request Weight(IP)[​](/docs/wallet/asset/query-user-delegation#request-weightip "Direct link to Request Weight\(IP\)")

**60**

## Request Parameters[​](/docs/wallet/asset/query-user-delegation#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES|   
startTime| LONG| YES|   
endTime| LONG| YES|   
type| ENUM| NO| Delegate/Undelegate  
asset| STRING| NO|   
current| INTEGER| NO| default 1  
size| INTEGER| NO| default 10, max 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/asset/query-user-delegation#response-example "Direct link to Response Example")
    
    
    {  
        "total": 3316,  
        "rows": [  
            {  
                "clientTranId": "293915932290879488",  
                "transferType": "Undelegate",  
                "asset": "ETH",  
                "amount": "1",  
                "time": 1695205406000  
            },  
            {  
                "clientTranId": "293915892281413632",  
                "transferType": "Delegate",  
                "asset": "ETH",  
                "amount": "1",  
                "time": 1695205396000  
            }  
        ]  
    }

---

# 查询用户委托资金历史(适用主账户)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/query-user-delegation#接口描述 "接口描述的直接链接")

查询用户委托资金历史

## HTTP请求[​](/docs/zh-CN/wallet/asset/query-user-delegation#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/custody/transfer-history`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/query-user-delegation#请求权重ip "请求权重\(IP\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/wallet/asset/query-user-delegation#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES|   
startTime| LONG| YES|   
endTime| LONG| YES|   
type| ENUM| NO| Delegate/Undelegate  
asset| STRING| NO|   
current| INTEGER| NO| 默认 1  
size| INTEGER| NO| 默认 10, 最大 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/query-user-delegation#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 3316,  
        "rows": [  
            {  
                "clientTranId": "293915932290879488",  
                "transferType": "Undelegate",  
                "asset": "ETH",  
                "amount": "1",  
                "time": 1695205406000  
            },  
            {  
                "clientTranId": "293915892281413632",  
                "transferType": "Delegate",  
                "asset": "ETH",  
                "amount": "1",  
                "time": 1695205396000  
            }  
        ]  
    }