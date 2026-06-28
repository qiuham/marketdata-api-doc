---
exchange: binance
source_url: https://developers.binance.com/docs/convert/trade/Get-Convert-Trade-History
api_type: Trading
updated_at: 2026-05-27 19:00:52.839777
---

# Get Convert Trade History(USER_DATA)

## API Description[​](/docs/convert/trade/Get-Convert-Trade-History#api-description "Direct link to API Description")

Get Convert Trade History

## HTTP Request[​](/docs/convert/trade/Get-Convert-Trade-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/convert/tradeFlow`

## Request Weight(UID)[​](/docs/convert/trade/Get-Convert-Trade-History#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/convert/trade/Get-Convert-Trade-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| YES|   
endTime| LONG| YES|   
limit| INT| NO| Default 100, Max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * The max interval between startTime and endTime is 30 days.
> 


## Response Example[​](/docs/convert/trade/Get-Convert-Trade-History#response-example "Direct link to Response Example")
    
    
    {  
       "list": [  
            {  
                "quoteId": "f3b91c525b2644c7bc1e1cd31b6e1aa6",  
                "orderId": 940708407462087195,    
                "orderStatus": "SUCCESS",  // order status  
                "fromAsset": "USDT",       // from asset  
                "fromAmount": "20",        // from amount  
                "toAsset": "BNB",          // to asset  
                "toAmount": "0.06154036",  // to amount  
                "ratio": "0.00307702",     // price ratio  
                "inverseRatio": "324.99",  // inverse price   
                "createTime": 1624248872184  
            }  
       ],  
        "startTime": 1623824139000,  
        "endTime": 1626416139000,  
        "limit": 100,  
        "moreData": false  
    }

---

# 获取闪兑交易记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/convert/trade/Get-Convert-Trade-History#接口描述 "接口描述的直接链接")

获取闪兑交易记录

## HTTP请求[​](/docs/zh-CN/convert/trade/Get-Convert-Trade-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/convert/tradeFlow`

## 请求权重(UID)[​](/docs/zh-CN/convert/trade/Get-Convert-Trade-History#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/convert/trade/Get-Convert-Trade-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| YES|   
endTime| LONG| YES|   
limit| INT| NO| 默认 100, 最大 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * startTime和endTime的最大时间间隔为30天
> 


## 响应示例[​](/docs/zh-CN/convert/trade/Get-Convert-Trade-History#响应示例 "响应示例的直接链接")
    
    
    {  
       "list": [  
            {  
                "quoteId": "f3b91c525b2644c7bc1e1cd31b6e1aa6",  
                "orderId": 940708407462087195,  // 订单号  
                "orderStatus": "SUCCESS",  // 订单状态  
                "fromAsset": "USDT",       // 闪兑前币种  
                "fromAmount": "20",        // 闪兑前金额  
                "toAsset": "BNB",          // 闪兑后币种  
                "toAmount": "0.06154036",  // 闪兑后金额  
                "ratio": "0.00307702",     // 价格  
                "inverseRatio": "324.99",  // 反向价格  
                "createTime": 1624248872184  
            }  
       ],  
        "startTime": 1623824139000,  
        "endTime": 1626416139000,  
        "limit": 100,  
        "moreData": false  
    }