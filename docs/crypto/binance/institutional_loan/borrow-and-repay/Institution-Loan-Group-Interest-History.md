---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History
api_type: REST
updated_at: 2026-05-27 19:01:16.198568
---

# Risk Unit Interest History(USER_DATA)

## API Description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#api-description "Direct link to API Description")

Query Institutional loan risk unit interest history. This endpoint is accessible only with the credit account API key.

## HTTP Request[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-group/interest-history

## Request Weight[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#request-weight "Direct link to Request Weight")

10(IP)

## RequestParameters[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#requestparameters "Direct link to RequestParameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| NO| Risk unit unique identifier  
asset| STRING| NO| Asset Name , USDT or USDC  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| The currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
  
  * Credit account can query currently activated and closed risk units using the parameter groupId. If groupId is empty, only currently activated risk units are returned.
  * Responses are returned in descending order.
  * The max interval between startTime and endTime is 100 days. This is required to ensure data accuracy.
  * If startTime and endTime are not provided, data from the last 7 days is returned by default.
  * If startTime is provided but endTime is omitted, returns records of [max(startTime, now-30d), now].
  * If startTime is omitted but endTime is provided, returns records of [endTime-7, endTime].



## Response Example[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#response-example "Direct link to Response Example")
    
    
    {  
      "total": 2,  
      
    "rows": [  
      
      {  
      
        "groupId": 2,  
      
        "assetName": "USDC",  
      
        "principal": 851340.57601652,  
      
        "interestRate": 0.00000833,  
      
        "interest": 7.09447643,  
      
        "interestTimestamp": 1746442800000  
      
      },  
      
      {  
      
        "groupId": 2,  
      
        "assetName": "USDC",  
      
        "principal": 851340.57601652,  
      
        "interestRate": 0.00000833,  
      
        "interest": 7.09447643,  
      
        "interestTimestamp": 1746439200000  
      
      }  
    ]  
    }  
    

## Response detail description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#response-detail-description "Direct link to Response detail description")

Parameter| Type| Description  
---|---|---  
total| STRING| Number of historical interest records  
rows| OBJECT ARRAY|   
  
→ groupId| STRING| Risk unit unique identifier  
→ assetName| STRING| Borrowed asset name  
→ principal| STRING| Principal amount  
→ interestRate| STRING| Hourly interest rate  
→ interest| STRING| Interest amount  
→ interestTimestamp| LONG| Interest last update timestamp (milliseconds)

---

# 风险单位历史利息 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#接口描述 "接口描述的直接链接")

查询机构贷风险单位给定时间段内的利息历史记录。此接口仅可使用信用账户API Key访问。

## HTTP 请求[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#http-请求 "HTTP 请求的直接链接")

GET /sapi/v1/margin/loan-group/interest-history

## 请求权重[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#请求权重 "请求权重的直接链接")

10(IP)

## 请求参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
groupId| LONG| NO| 唯一风险单位标识符  
asset| STRING| NO| 资产名称， 如 USDT 或 USDC  
startTime| LONG| NO|   
  
endTime| LONG| NO|   
  
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
  
  * 放贷账户可根据参数groupId查询当前生效状态 风险单位和已经关闭的风险单位，若groupId为空，则返回当前生效状态 的风险单位。
  * 响应返回为降序排列。
  * 查询时间范围最大不得超过100天。这是确保数据正确性必须的。
  * 若startTime和endTime没传，则默认返回最近7天数据
  * 如果startTime传递了而endTime没传，则返回 startTime到现在的利息历史记录；若startTime至今超过30天，则返回过去30天的利息历史记录。
  * 如果startTime没传而endTime传递了，则返回 endTime之前7天的利息历史记录



## 响应示例[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#响应示例 "响应示例的直接链接")
    
    
    {  
      "total": 2,  
      
    "rows": [  
      
      {  
      
        "groupId": 2,  
      
        "assetName": "USDC",  
      
        "principal": 851340.57601652,  
      
        "interestRate": 0.00000833,  
      
        "interest": 7.09447643,  
      
        "interestTimestamp": 1746442800000  
      
      },  
      
      {  
      
        "groupId": 2,  
      
        "assetName": "USDC",  
      
        "principal": 851340.57601652,  
      
        "interestRate": 0.00000833,  
      
        "interest": 7.09447643,  
      
        "interestTimestamp": 1746439200000  
      
      }  
    ]  
    }  
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Interest-History#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
total| STRINGString| 查询到的历史利息记录数量  
rows| OBJECT ARRAY|   
  
→ groupId| STRINGString| 唯一风险单位标识符  
→ assetName| STRING| 借款币种名称  
→ principal| STRING| 借款本金  
→ interestRate| STRING| 借款小时利率  
→ interest| STRING| 利息金额  
→ interestTimestamp| LONG| 利率最后更新时间戳（毫秒