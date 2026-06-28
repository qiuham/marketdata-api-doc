---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert
api_type: REST
updated_at: 2026-01-15T23:46:36.552144
---

# List All Convert Pairs

## API Description[​](/docs/derivatives/usds-margined-futures/convert#api-description "Direct link to API Description")

Query for all convertible token pairs and the tokens’ respective upper/lower limits

## HTTP Request[​](/docs/derivatives/usds-margined-futures/convert#http-request "Direct link to HTTP Request")

GET `/fapi/v1/convert/exchangeInfo`

## Request Weight[​](/docs/derivatives/usds-margined-futures/convert#request-weight "Direct link to Request Weight")

**20(IP)**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/convert#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromAsset| STRING| EITHER OR BOTH| User spends coin  
toAsset| STRING| EITHER OR BOTH| User receives coin  
  
>   * User needs to supply either or both of the input parameter
>   * If not defined for both fromAsset and toAsset, only partial token pairs will be returned
>   * Asset BNFCR is only available to convert for MICA region users.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/convert#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "fromAsset":"BTC",  
        "toAsset":"USDT",  
        "fromAssetMinAmount":"0.0004",  
        "fromAssetMaxAmount":"50",  
        "toAssetMinAmount":"20",  
        "toAssetMaxAmount":"2500000"  
      }  
    ]

---

# 查询可交易币对信息

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/convert#接口描述 "接口描述的直接链接")

查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/convert#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/convert/exchangeInfo`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/convert#请求权重 "请求权重的直接链接")

**20(IP)**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/convert#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromAsset| STRING| EITHER OR BOTH| 用户售出币种  
toAsset| STRING| EITHER OR BOTH| 用户买入币种  
  
>   * 用户应当fromAsset和toAsset参数至少填一个。
>   * 如果fromAsset和toAsset只填写了一个参数，将会返回部分币对信息。
>   * BNFCR资产仅对MICA地区用户有效
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/convert#响�应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "fromAsset":"BTC",  
        "toAsset":"USDT",  
        "fromAssetMinAmount":"0.0004",  
        "fromAssetMaxAmount":"50",  
        "toAssetMinAmount":"20",  
        "toAssetMaxAmount":"2500000"  
      }  
    ]