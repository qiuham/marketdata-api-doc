---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History
api_type: Account
updated_at: 2026-01-15T23:44:52.984909
---

# Get Margin Borrow/Loan Interest History(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#api-description "Direct link to API Description")

Get Margin Borrow/Loan Interest History

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/marginInterestHistory`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
archived| STRING| NO| Default: `false`. Set to `true` for archived data from 6 months ago  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
>   * Response in descending order
>   * The max interval between startTime and endTime is 30 days. It is a MUST to ensure data correctness.
>   * If `startTime` and `endTime` not sent, return records of the last 7 days by default
>   * If `startTime` is sent and `endTime` is not sent, the records from `startTime` to the present will be returned; if `startTime` is more than 30 days ago, the records of the past 30 days will be returned.
>   * If `startTime` is not sent and `endTime` is sent, the records of the 7 days before `endTime` is returned.
>   * Type in response has 5 enums: 
>     * `PERIODIC` interest charged per hour
>     * `ON_BORROW` first interest charged on borrow
>     * `PERIODIC_CONVERTED` interest charged per hour converted into BNB
>     * `ON_BORROW_CONVERTED` first interest charged on borrow converted into BNB
>     * `PORTFOLIO` Portfolio Margin negative balance daily interest
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#response-example "Direct link to Response Example")
    
    
    {  
      "rows": [  
        {              
          "txId": 1352286576452864727,             
          "interestAccuredTime": 1672160400000,              
          "asset": "USDT",   
          "rawAsset": “USDT”,             
          "principal": "45.3313",              
          "interest": "0.00024995",              
          "interestRate": "0.00013233",              
          "type": "ON_BORROW"            
        }  
      ],  
      "total": 1  
    }

---

# 获取杠杆利息历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#接口描述 "接口描述的直接链接")

获取杠杆利息历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/marginInterestHistory`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
archived| STRING| NO| 默认: `false`. 查询6个月以前的数据，需要设为 `true`  
recvWindow| LONG| NO| 赋值不能超过 `60000`  
timestamp| LONG| YES|   
  
>   * 响应返回为降序排列。
>   * 查询时间范围最大不得超过30天，这是确保数据正确性必须的。
>   * 若`startTime`和`endTime`没传，则默认返回最近7天数据。
>   * 如果发送了`startTime`且未发送`endTime`，则返回`startTime`到现在的的利息历史记录；若`startTime`至今超过30天，则返回过去30天的利息历史记录。
>   * 如果没有发送`startTime`而发送了`endTime`，则返回`endTime`之前7天的利息历史记录。
>   * 返回的type数据有5种类型: 
>     * `PERIODIC` 每小时收的利息
>     * `ON_BORROW` 借款的时候第一次收的利息
>     * `PERIODIC_CONVERTED` 每小时收的利息，用BNB抵扣
>     * `ON_BORROW_CONVERTED` 借款的时候第一次收的利息，用BNB抵扣
>     * `PORTFOLIO`统一账户负余额每日利息
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History#响应示例 "响应示例的直接链接")
    
    
    {  
      "rows": [  
        {              
          "txId": 1352286576452864727,             
          "interestAccuredTime": 1672160400000,              
          "asset": "USDT",   
          "rawAsset": “USDT”,             
          "principal": "45.3313",              
          "interest": "0.00024995",              
          "interestRate": "0.00013233",              
          "type": "ON_BORROW"            
        }  
      ],  
      "total": 1  
    }