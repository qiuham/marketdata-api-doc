---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/user-assets
api_type: REST
updated_at: 2026-06-29 19:11:49.787694
---

# User Asset (USER_DATA)

## API Description[​](/docs/wallet/asset/user-assets#api-description "Direct link to API Description")

Get user assets, just for positive data.

## HTTP Request[​](/docs/wallet/asset/user-assets#http-request "Direct link to HTTP Request")

POST `/sapi/v3/asset/getUserAsset`

## Request Weight(IP)[​](/docs/wallet/asset/user-assets#request-weightip "Direct link to Request Weight\(IP\)")

**5**

## Request Parameters[​](/docs/wallet/asset/user-assets#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO| If asset is blank, then query all positive assets user have.  
needBtcValuation| BOOLEAN| NO| Whether need btc valuation or not.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If asset is set, then return this asset, otherwise return all assets positive.
>   * If needBtcValuation is set, then return btcValudation.
> 


## Response Example[​](/docs/wallet/asset/user-assets#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "AVAX",  
            "free": "1",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "BCH",  
            "free": "0.9",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "BNB",  
            "free": "887.47061626",  
            "locked": "0",  
            "freeze": "10.52",  
            "withdrawing": "0.1",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "BUSD",  
            "free": "9999.7",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "SHIB",  
            "free": "532.32",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "USDT",  
            "free": "50300000001.44911105",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "WRZ",  
            "free": "1",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        }  
    ]

---

# 用户持仓(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/user-assets#接口描述 "接口描述的直接链接")

获取用户持仓，仅返回>0的数据。

## HTTP请求[​](/docs/zh-CN/wallet/asset/user-assets#http请求 "HTTP请求的直接链接")

POST `/sapi/v3/asset/getUserAsset`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/user-assets#请求权重ip "请求权重\(IP\)的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/wallet/asset/user-assets#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO| 如果资产为空，则查询用户所有的正资产。  
needBtcValuation| BOOLEAN| NO| 是否需要返回兑换成BTC的估值  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/user-assets#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "AVAX",  
            "free": "1",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "BCH",  
            "free": "0.9",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "BNB",  
            "free": "887.47061626",  
            "locked": "0",  
            "freeze": "10.52",  
            "withdrawing": "0.1",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "BUSD",  
            "free": "9999.7",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "SHIB",  
            "free": "532.32",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "USDT",  
            "free": "50300000001.44911105",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        },  
        {  
            "asset": "WRZ",  
            "free": "1",  
            "locked": "0",  
            "freeze": "0",  
            "withdrawing": "0",  
            "ipoable": "0",  
            "btcValuation": "0"  
        }  
    ]