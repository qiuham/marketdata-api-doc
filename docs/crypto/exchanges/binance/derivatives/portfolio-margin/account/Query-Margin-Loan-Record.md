---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record
api_type: Account
updated_at: 2026-01-15T23:45:06.557306
---

# Query Margin Loan Record(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#api-description "Direct link to API Description")

Query margin loan record

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/marginLoan`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#request-weight "Direct link to Request Weight")

**10**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
txId| LONG| NO| the `tranId` in `POST/papi/v1/marginLoan`  
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


## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#response-example "Direct link to Response Example")
    
    
    {  
      "rows": [  
        {  
            "txId": 12807067523,  
            "asset": "BNB",  
            "principal": "0.84624403",  
            "timestamp": 1555056425000,  
            "status": "CONFIRMED"   //one of PENDING (pending execution), CONFIRMED (successfully loaned), FAILED (execution failed, nothing happened to your account);  
        }  
      ],  
      "total": 1  
    }

---

# 查询杠杆借贷记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#接口描述 "接口描述的直接链接")

查询杠杆借贷记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/marginLoan`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
txId| LONG| NO| `tranId` in `POST/papi/v1/marginLoan`  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 开始值 1。 默认:1  
size| LONG| NO| Default:10 Max:100  
archived| STRING| NO| 默认: `false`. 查询6个月以前的数据，需要设为`true`  
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
>   * 必须发送txId 或 startTime，txId 优先
>   * 响应返回为降序排列。
>   * 查询时间范围最大不得超过30天。
>   * 若startTime和endTime没传，则默认返回最近7天数据
>   * 如果想查询6个月以前数据，设置 archived 为 true
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record#响应示例 "响应示例的直接链接")
    
    
    {  
      "rows": [  
        {  
            "txId": 12807067523,  
            "asset": "BNB",  
            "principal": "0.84624403",  
            "timestamp": 1555056425000,  
            "status": "CONFIRMED"  //状态: PENDING (等待执行), CONFIRMED (成功借贷), FAILED (执行失败);  
        }  
      ],  
      "total": 1  
    }