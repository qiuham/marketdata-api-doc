---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History
api_type: Account
updated_at: 2026-01-15T23:45:10.910390
---

# Query Portfolio Margin Negative Balance Interest History(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#api-description "Direct link to API Description")

Query interest history of negative balance for portfolio margin.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#http-request "Direct link to HTTP Request")

`GET /papi/v1/portfolio/interest-history`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#request-weight "Direct link to Request Weight")

**50**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Response in descending order
>   * The max interval between startTime and endTime is 30 days. It is a MUST to ensure data correctness.
>   * If `startTime` and `endTime` not sent, return records of the last 7 days by default
>   * If `startTime` is sent and `endTime` is not sent, the records from `startTime` to the present will be returned; if `startTime` is more than 30 days ago, the records of the past 30 days will be returned.
>   * If `startTime` is not sent and `endTime` is sent, the records of the 7 days before `endTime` is returned.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "USDT",      
            "interest": "24.4440",               //interest amount  
            "interestAccuredTime": 1670227200000,  
            "interestRate": "0.0001164",         //daily interest rate  
            "principal": "210000"  
        }  
    ]

---

# 查询统一账户期货负余额收息历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#接口描述 "接口描述的直接链接")

查询统一账户期货负余额收息历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/portfolio/interest-history`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#请求权重 "请求权重的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 响应返回为降序排列。
>   * 查询时间范围最大不得超过30天，这是确保数据正确性必须的。
>   * 若`startTime`和`endTime`没传，则默认返回最近7天数据。
>   * 如果发送了`startTime`且未发送`endTime`，则返回`startTime`到现在的的利息历史记录；若`startTime`至今超过30天，则返回过去30天的利息历史记录。
>   * 如果没有发送`startTime`而发送了`endTime`，则返回`endTime`之前7天的利息历史记录。
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "USDT",      
            "interest": "24.4440",               //利息金额  
            "interestAccuredTime": 1670227200000,  
            "interestRate": "0.0001164",         //日利率   
            "principal": "210000"  
        }  
    ]