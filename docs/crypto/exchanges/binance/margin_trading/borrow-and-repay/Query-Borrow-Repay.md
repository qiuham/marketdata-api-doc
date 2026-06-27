---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay
api_type: REST
updated_at: 2026-05-27 18:56:29.952069
---

# Query Margin Interest Rate History (USER_DATA)

## API Description[​](/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#api-description "Direct link to API Description")

Query Margin Interest Rate History

## HTTP Request[​](/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/interestRateHistory`

## Request Weight[​](/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
vipLevel| INT| NO| Default: user's vip level  
startTime| LONG| NO| Default: 7 days ago  
endTime| LONG| NO| Default: present. Maximum range: 1 months.  
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "BTC",  
            "dailyInterestRate": "0.00025000",  
            "timestamp": 1611544731000,  
            "vipLevel": 1      
        },  
        {  
            "asset": "BTC",  
            "dailyInterestRate": "0.00035000",  
            "timestamp": 1610248118000,  
            "vipLevel": 1      
        }  
    ]

---

# 获取杠杆利率历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#接口描述 "接口描述的直接链接")

获取杠杆利率历史

## HTTP请求[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/interestRateHistory`

## 请求权重[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
vipLevel| INT| NO| 默认用户当前等级  
startTime| LONG| NO| 默认7天前  
endTime| LONG| NO| 默认当天，时间间隔最大为1个月  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "BTC",  
            "dailyInterestRate": "0.00025000",  
            "timestamp": 1611544731000,  
            "vipLevel": 1      
        },  
        {  
            "asset": "BTC",  
            "dailyInterestRate": "0.00035000",  
            "timestamp": 1610248118000,  
            "vipLevel": 1      
        }  
    ]