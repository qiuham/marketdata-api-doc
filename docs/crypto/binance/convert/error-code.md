---
exchange: binance
source_url: https://developers.binance.com/docs/convert/error-code
api_type: REST
updated_at: 2026-05-27 19:00:42.228304
---

# List All Convert Pairs

## API Description[​](/docs/convert/market-data#api-description "Direct link to API Description")

Query for all convertible token pairs and the tokens’ respective upper/lower limits

## HTTP Request[​](/docs/convert/market-data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/convert/exchangeInfo`

## Request Weight[​](/docs/convert/market-data#request-weight "Direct link to Request Weight")

**3000(IP)**

## Request Parameters[​](/docs/convert/market-data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromAsset| STRING| EITHER OR BOTH| User spends coin  
toAsset| STRING| EITHER OR BOTH| User receives coin  
  
>   * User needs to supply either or both of the input parameter
>   * If not defined for both fromAsset and toAsset, only partial token pairs will be returned
> 


## Response Example[​](/docs/convert/market-data#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "fromAsset":"BTC",  
        "toAsset":"USDT",  
        "fromAssetMinAmount":"0.0004",  
        "fromAssetMaxAmount":"50",  
        "toAssetMinAmount":"20",  
        "toAssetMaxAmount":"9E+24" // 9E+24 signals that this symbol has a very large upper limit close to infinity  
      }  
    ]

---

# 查询可交易币对信息

## 接口描述[​](/docs/zh-CN/convert/market-data#接口描述 "接口描述的直接链接")

查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。

## HTTP请求[​](/docs/zh-CN/convert/market-data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/convert/exchangeInfo`

## 请求权重[​](/docs/zh-CN/convert/market-data#请求权重 "请求权重的直接链接")

**3000(IP)**

## 请求参数[​](/docs/zh-CN/convert/market-data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromAsset| STRING| EITHER OR BOTH| 用户售出币种  
toAsset| STRING| EITHER OR BOTH| 用户买入币种  
  
>   * 用户应当fromAsset和toAsset参数至少填一个。
>   * 如果fromAsset和toAsset只填写了一个参数，将会返回部分币对信息。
> 


## 响应示例[​](/docs/zh-CN/convert/market-data#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "fromAsset":"BTC",  
        "toAsset":"USDT",  
        "fromAssetMinAmount":"0.0004",  
        "fromAssetMaxAmount":"50",  
        "toAssetMinAmount":"20",  
        "toAssetMaxAmount":"9E+24" // 9E+24 表示该符号的上限非常大，接近无穷大  
      }  
    ]