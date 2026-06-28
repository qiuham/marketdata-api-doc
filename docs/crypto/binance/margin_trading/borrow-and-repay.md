---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/borrow-and-repay
api_type: REST
updated_at: 2026-05-27 18:56:25.654769
---

# Get Interest History (USER_DATA)

## API Description[​](/docs/margin_trading/borrow-and-repay/Get-Interest-History#api-description "Direct link to API Description")

Get Interest History

## HTTP Request[​](/docs/margin_trading/borrow-and-repay/Get-Interest-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/interestHistory`

## Request Weight[​](/docs/margin_trading/borrow-and-repay/Get-Interest-History#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/borrow-and-repay/Get-Interest-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
isolatedSymbol| STRING| NO| isolated symbol  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * Response in descending order
  * If isolatedSymbol is not sent, crossed margin data will be returned
  * The max interval between `startTime` and `endTime` is 30 days. It is a MUST to ensure data correctness.
  * If `startTime`and `endTime` not sent, return records of the last 7 days by default.
  * If `startTime` is sent and `endTime` is not sent, return records of [max(`startTime`, now-30d), now].
  * If `startTime` is not sent and `endTime` is sent, return records of [`endTime`-7, `endTime`]
  * `type` in response has 4 enums: 
    * `PERIODIC` interest charged per hour
    * `ON_BORROW` first interest charged on borrow
    * `PERIODIC_CONVERTED` interest charged per hour converted into BNB
    * `ON_BORROW_CONVERTED` first interest charged on borrow converted into BNB
    * `PORTFOLIO` interest charged daily on the portfolio margin negative balance



## Response Example[​](/docs/margin_trading/borrow-and-repay/Get-Interest-History#response-example "Direct link to Response Example")
    
    
    {  
      "rows": [  
        {              
          "txId": 1352286576452864727,             
          "interestAccuredTime": 1672160400000,              
          "asset": "USDT",   
          "rawAsset": “USDT”,  // will not be returned for isolated margin             
          "principal": "45.3313",              
          "interest": "0.00024995",              
          "interestRate": "0.00013233",              
          "type": "ON_BORROW",             
          "isolatedSymbol": "BNBUSDT"  // isolated symbol, will not be returned for crossed margin        
        }  
      ],  
      "total": 1  
    }

---

# 获取利息历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/borrow-and-repay/Get-Interest-History#接口描述 "接口描述的直接链接")

获取利息历史

## HTTP请求[​](/docs/zh-CN/margin_trading/borrow-and-repay/Get-Interest-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/interestHistory`

## 请求权重[​](/docs/zh-CN/margin_trading/borrow-and-repay/Get-Interest-History#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/borrow-and-repay/Get-Interest-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
isolatedSymbol| STRING| NO| 逐仓symbol  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 响应返回为降序排列。
  * 如果发送isolatedSymbol，返回指定逐仓symbol的记录。
  * 查询时间范围最大不得超过30天。这是确保数据正确性必须的。
  * 若`startTime`和`endTime`没传，则默认返回最近7天数据
  * 如果`startTime`传递了而`endTime`没传，则返回 `startTime`到现在的利息历史记录；若`startTime`至今超过30天，则返回过去30天的利息历史记录。
  * 如果`startTime`没传而`endTime`传递了，则返回 `endTime`之前7天的利息历史记录
  * 返回的`type`数据有4种类型: 
    * `PERIODIC` 每小时收的利息
    * `ON_BORROW` 借款的时候第一次收的利息
    * `PERIODIC_CONVERTED` 每小时收的利息，用BNB抵扣
    * `ON_BORROW_CONVERTED` 借款的时候第一次收的利息，用BNB抵扣
    * `PORTFOLIO` 统一账户负余额每日利息



## 响应示例[​](/docs/zh-CN/margin_trading/borrow-and-repay/Get-Interest-History#响应示例 "响应示例的直接链接")
    
    
    {  
      "rows": [  
        {              
          "txId": 1352286576452864727,             
          "interestAccuredTime": 1672160400000,              
          "asset": "USDT",   
          "rawAsset": “USDT”,  // 逐仓不会返回此字段            
          "principal": "45.3313",              
          "interest": "0.00024995",              
          "interestRate": "0.00013233",              
          "type": "ON_BORROW",             
          "isolatedSymbol": "BNBUSDT"  // 返回逐仓symbol; 若是全仓不会返回此字段      
        }  
      ],  
      "total": 1  
    }