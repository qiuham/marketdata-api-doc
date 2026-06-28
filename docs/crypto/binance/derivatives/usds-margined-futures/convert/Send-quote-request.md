---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Send-quote-request
api_type: REST
updated_at: 2026-01-15T23:46:40.053991
---

# Send Quote Request(USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#api-description "Direct link to API Description")

Request a quote for the requested token pairs

## HTTP Request[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#http-request "Direct link to HTTP Request")

POST `/fapi/v1/convert/getQuote`

## Request Weight[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#request-weight "Direct link to Request Weight")

**50(IP)**

**360/hour，500/day**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromAsset| STRING| YES|   
toAsset| STRING| YES|   
fromAmount| DECIMAL| EITHER| When specified, it is the amount you will be debited after the conversion  
toAmount| DECIMAL| EITHER| When specified, it is the amount you will be credited after the conversion  
validTime| ENUM| NO| 10s, default 10s  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
  * Either fromAmount or toAmount should be sent
  * `quoteId` will be returned only if you have enough funds to convert



## Response Example[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#response-example "Direct link to Response Example")
    
    
    {  
       "quoteId":"12415572564",  
       "ratio":"38163.7",  
       "inverseRatio":"0.0000262",  
       "validTimestamp":1623319461670,  
       "toAmount":"3816.37",  
       "fromAmount":"0.1"  
    }

---

# 发送获取报价请求(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Send-quote-request#接口描述 "接口描述的直接链接")

对所需的币对发送获取报价请求

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Send-quote-request#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/convert/getQuote`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Send-quote-request#请求权重 "请求权重的直接链接")

**50(IP)** **每小时360次，每天500次**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Send-quote-request#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromAsset| STRING| YES|   
toAsset| STRING| YES|   
fromAmount| DECIMAL| EITHER| 这是成交后将被扣除的金额  
toAmount| DECIMAL| EITHER| 这是成交后将会获得的金额  
validTime| ENUM| NO| 可以支持10s，默认值为10s  
recvWindow| LONG| NO| 此值不能大于 60000  
timestamp| LONG| YES|   
  
>   * 参数fromAmount或者toAmount只需要提供其中一个。
>   * `quoteId`仅在账户余额充足时返回。
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Send-quote-request#响应示例 "响应示例的直接链接")
    
    
    {  
       "quoteId":"12415572564",  
       "ratio":"38163.7",  
       "inverseRatio":"0.0000262",  
       "validTimestamp":1623319461670,  
       "toAmount":"3816.37",  
       "fromAmount":"0.1"  
    }