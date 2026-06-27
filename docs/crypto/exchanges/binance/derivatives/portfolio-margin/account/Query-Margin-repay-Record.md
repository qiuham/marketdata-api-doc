---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record
api_type: Account
updated_at: 2026-01-15T23:45:10.846472
---

# Query Margin repay Record(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record#api-description "Direct link to API Description")

Query margin repay record.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/repayLoan`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record#request-weight "Direct link to Request Weight")

**10**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
txId| LONG| NO| the tranId in `POST/papi/v1/repayLoan`  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
archived| STRING| NO| Default: `false`. Set to `true` for archived data from 6 months ago  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * txId or startTime must be sent. txId takes precedence.
>   * Response in descending order
>   * The max interval between `startTime` and `endTime` is 30 days.
>   * If `startTime` and `endTime` not sent, return records of the last 7 days by default
>   * Set `archived` to `true` to query data from 6 months ago
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record#response-example "Direct link to Response Example")
    
    
    {  
         "rows": [  
             {  
                    "amount": "14.00000000",   //Total amount repaid  
                    "asset": "BNB",     
                    "interest": "0.01866667",    //Interest repaid  
                    "principal": "13.98133333",   //Principal repaid  
                    "status": "CONFIRMED",   //one of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing happened to your account)  
                    "timestamp": 1563438204000,  
                    "txId": 2970933056  
             }  
         ],  
         "total": 1  
    }

---

# 查询杠杆还贷记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#接口描述 "接口描述的直接链接")

查询杠杆还贷记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/repayLoan`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
txId| LONG| NO| the `tranId` in `POST/papi/v1/repayLoan`  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 开始值 1。 默认:1  
size| LONG| NO| Default:10 Max:100  
archived| STRING| NO| Default: `false`. Set to `true` for archived data from 6 months ago  
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
>   * 必须发送txId 或 startTime，txId 优先
>   * 响应返回为降序排列。
>   * 查询时间范围最大不得超过30天。
>   * 若startTime和endTime没传，则默认返回最近7天数据
>   * 如果想查询6个月以前数据，设置 archived 为 true
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#响应示例 "响应示例的直接链接")
    
    
    {  
         "rows": [  
             {  
                    "amount": "14.00000000",   //还款总额  
                    "asset": "BNB",     
                    "interest": "0.01866667",    //支付的利息  
                    "principal": "13.98133333",   //支付的本金  
                    "status": "CONFIRMED",   //状态: PENDING (等待执行), CONFIRMED (成功还款), FAILED (执行失败);  
                    "timestamp": 1563438204000,  
                    "txId": 2970933056  
             }  
         ],  
         "total": 1  
    }