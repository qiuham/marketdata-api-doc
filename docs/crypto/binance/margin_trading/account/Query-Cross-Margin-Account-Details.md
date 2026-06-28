---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Query-Cross-Margin-Account-Details
api_type: Account
updated_at: 2026-05-27 18:56:15.929707
---

# Query Cross Margin Fee Data (USER_DATA)

## API Description[​](/docs/margin_trading/account/Query-Cross-Margin-Fee-Data#api-description "Direct link to API Description")

Get cross margin fee data collection with any vip level or user's current specific data as <https://www.binance.com/en/margin-fee>

## HTTP Request[​](/docs/margin_trading/account/Query-Cross-Margin-Fee-Data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/crossMarginData`

## Request Weight[​](/docs/margin_trading/account/Query-Cross-Margin-Fee-Data#request-weight "Direct link to Request Weight")

**1 when coin is specified;(IP)** **5 when the coin parameter is omitted(IP)**

## Request Parameters[​](/docs/margin_trading/account/Query-Cross-Margin-Fee-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
vipLevel| INT| NO| User's current specific margin data will be returned if vipLevel is omitted  
coin| STRING| NO|   
recvWindow| LONG| NO| No more than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Query-Cross-Margin-Fee-Data#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "vipLevel": 0,  
            "coin": "BTC",  
            "transferIn": true,  
            "borrowable": true,  
            "dailyInterest": "0.00026125",  
            "yearlyInterest": "0.0953",  
            "borrowLimit": "180",  
            "marginablePairs": [  
                "BNBBTC",  
                "TRXBTC",  
                "ETHBTC",  
                "BTCUSDT"  
            ]  
        }  
    ]

---

# 获取全仓杠杆利率及限额 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Fee-Data#接口描述 "接口描述的直接链接")

通过VIP等级或用户当前VIP等级获取全仓杠杆利率及限额， 如：<https://www.binance.com/en/margin-fee>

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Fee-Data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/crossMarginData`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Fee-Data#请求权重 "请求权重的直接链接")

**1 指定币种;(IP)** **5 币种参数缺失(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Fee-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
vipLevel| INT| NO| 默认为用户当前VIP等级  
coin| STRING| NO|   
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Fee-Data#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "vipLevel": 0,  
            "coin": "BTC",  
            "transferIn": true,  
            "borrowable": true,  
            "dailyInterest": "0.00026125",  
            "yearlyInterest": "0.0953",  
            "borrowLimit": "180",  
            "marginablePairs": [  
                "BNBBTC",  
                "TRXBTC",  
                "ETHBTC",  
                "BTCUSDT"  
            ]  
        }  
    ]