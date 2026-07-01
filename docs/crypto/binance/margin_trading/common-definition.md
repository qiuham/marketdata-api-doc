---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/common-definition
api_type: REST
updated_at: 2026-07-01 19:08:30.304818
---

# Get All Cross Margin Pairs (MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs#api-description "Direct link to API Description")

Get All Cross Margin Pairs

## HTTP Request[​](/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/allPairs`

## Request Weight[​](/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
## Response Example[​](/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "base": "BNB",  
            "id": 351637150141315861,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "BNBBTC"  
        },  
        {  
            "base": "TRX",  
            "id": 351637923235429141,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "TRXBTC",  
            "delistTime": 1704973040  
        },  
        {  
            "base": "XRP",  
            "id": 351638112213990165,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "XRPBTC"  
        },  
        {  
            "base": "ETH",  
            "id": 351638524530850581,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "ETHBTC"  
        }  
    ]

---

# 获取所有全仓杠杆交易对(MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Get-All-Cross-Margin-Pairs#接口描述 "接口描述的直接链接")

获取所有全仓杠杆交易对

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Get-All-Cross-Margin-Pairs#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/allPairs`

## 请求权重[​](/docs/zh-CN/margin_trading/market-data/Get-All-Cross-Margin-Pairs#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Get-All-Cross-Margin-Pairs#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Get-All-Cross-Margin-Pairs#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "base": "BNB",  
            "id": 351637150141315861,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "BNBBTC"  
        },  
        {  
            "base": "TRX",  
            "id": 351637923235429141,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "TRXBTC",  
            "delistTime": 1704973040  
        },  
        {  
            "base": "XRP",  
            "id": 351638112213990165,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "XRPBTC"  
        },  
        {  
            "base": "ETH",  
            "id": 351638524530850581,  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "ETHBTC"  
        }  
    ]