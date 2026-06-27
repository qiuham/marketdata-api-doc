---
exchange: binance
source_url: https://developers.binance.com/docs/convert/market-data/Query-order-quantity-precision-per-asset
api_type: Market Data
updated_at: 2026-05-27 19:00:46.721378
---

# Send Quote Request(TRADE)

## API Description[​](/docs/convert/trade#api-description "Direct link to API Description")

Request a quote for the requested token pairs

## HTTP Request[​](/docs/convert/trade#http-request "Direct link to HTTP Request")

POST `/sapi/v1/convert/getQuote`

## Request Weight[​](/docs/convert/trade#request-weight "Direct link to Request Weight")

**200(UID)**

## Request Parameters[​](/docs/convert/trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromAsset| STRING| YES|   
toAsset| STRING| YES|   
fromAmount| DECIMAL| EITHER| When specified, it is the amount you will be debited after the conversion  
toAmount| DECIMAL| EITHER| When specified, it is the amount you will be credited after the conversion  
walletType| ENUM| NO| It is to choose which wallet of assets. The wallet selection is `SPOT`, `FUNDING` and `EARN`. Combination of wallet is supported i.e. `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN` or `SPOT_EARN` Default is `SPOT`.  
validTime| ENUM| NO| 10s, 30s, 1m, default 10s  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
  * Either fromAmount or toAmount should be sent
  * `quoteId` will be returned only if you have enough funds to convert



## Response Example[​](/docs/convert/trade#response-example "Direct link to Response Example")
    
    
    {  
       "quoteId":"12415572564",  
       "ratio":"38163.7",  
       "inverseRatio":"0.0000262",  
       "validTimestamp":1623319461670,  
       "toAmount":"3816.37",  
       "fromAmount":"0.1"  
    }

---

# 发送获取报价请求(TRADE)

## 接口描述[​](/docs/zh-CN/convert/trade#接口描述 "接口描述的直接链接")

对所需的币对发送获取报价请求

## HTTP请求[​](/docs/zh-CN/convert/trade#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/convert/getQuote`

## 请求权重[​](/docs/zh-CN/convert/trade#请求权重 "请求权重的直接链接")

**200(UID)**

## 请求参数[​](/docs/zh-CN/convert/trade#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromAsset| STRING| YES|   
toAsset| STRING| YES|   
fromAmount| DECIMAL| EITHER| 这是成交后将被扣除的金额  
toAmount| DECIMAL| EITHER| 这是成交后将会获得的金额  
walletType| ENUM| NO| 这里可以选择支付钱包，可支持的钱包的选择有`SPOT`，`FUNDING`和`EARN`。组合钱包选择也可支持，如`SPOT_FUNDING`，`FUNDING_EARN`，`SPOT_FUNDING_EARN`或者`SPOT_EARN`。默认选择为`SPOT`。  
validTime| ENUM| NO| 可以支持10s、30s、1m等值，默认值为 10s  
recvWindow| LONG| NO| 此值不能大于 60000  
timestamp| LONG| YES|   
  
>   * 参数fromAmount或者toAmount只需要提供其中一个。
>   * `quoteId`仅在账户余额充足时返回。
> 


## 响应示例[​](/docs/zh-CN/convert/trade#响应示例 "响应示例的直接链接")
    
    
    {  
       "quoteId":"12415572564",  
       "ratio":"38163.7",  
       "inverseRatio":"0.0000262",  
       "validTimestamp":1623319461670,  
       "toAmount":"3816.37",  
       "fromAmount":"0.1"  
    }