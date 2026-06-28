---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol
api_type: Market Data
updated_at: 2026-05-27 18:56:44.019839
---

# Get All Margin Assets (MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Get-All-Margin-Assets#api-description "Direct link to API Description")

Get All Margin Assets.

## HTTP Request[​](/docs/margin_trading/market-data/Get-All-Margin-Assets#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/allAssets`

## Request Weight[​](/docs/margin_trading/market-data/Get-All-Margin-Assets#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/market-data/Get-All-Margin-Assets#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
  
## Response Example[​](/docs/margin_trading/market-data/Get-All-Margin-Assets#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "assetFullName": "USD coin",  
        "assetName": "USDC",  
        "isBorrowable": true,  
        "isMortgageable": true,  
        "userMinBorrow": "0.00000000",  
        "userMinRepay": "0.00000000",  
        "delistTime": 1704973040  
      }  
    ]

---

# 获取所有杠杆资产信息 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Get-All-Margin-Assets#接口描述 "接口描述的直接链接")

获取所有杠杆资产信息

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Get-All-Margin-Assets#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/allAssets`

## 请求权重[​](/docs/zh-CN/margin_trading/market-data/Get-All-Margin-Assets#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Get-All-Margin-Assets#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Get-All-Margin-Assets#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "assetFullName": "USD coin",  
        "assetName": "USDC",  
        "isBorrowable": true,  
        "isMortgageable": true,  
        "userMinBorrow": "0.00000000",  
        "userMinRepay": "0.00000000",  
        "delistTime": 1704973040  
      }  
    ]