---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol
api_type: Market Data
updated_at: 2026-06-28 18:51:53.986918
---

# Get list Schedule (MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Get-List-Schedule#api-description "Direct link to API Description")

Get the upcoming tokens or symbols listing schedule for Cross Margin and Isolated Margin.

## HTTP Request[​](/docs/margin_trading/market-data/Get-List-Schedule#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/list-schedule`

## Request Weight(IP)[​](/docs/margin_trading/market-data/Get-List-Schedule#request-weightip "Direct link to Request Weight\(IP\)")

**100**

## Request Parameters[​](/docs/margin_trading/market-data/Get-List-Schedule#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/market-data/Get-List-Schedule#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "listTime": 1686161202000,  
        "crossMarginAssets": [  
          "BTC",  
          "USDT"  
        ],  
        "isolatedMarginSymbols": [  
          "ADAUSDT",  
          "BNBUSDT"  
        ]  
      },  
      {  
        "listTime": 1686222232000,  
        "crossMarginAssets": [  
          "ADA"  
        ],  
        "isolatedMarginSymbols": []  
      }  
    ]

---

# 查询上架计划 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Get-List-Schedule#接口描述 "接口描述的直接链接")

查询全仓和逐仓的币种或币对的上架计划

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Get-List-Schedule#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/list-schedule`

## 请求权重(IP)[​](/docs/zh-CN/margin_trading/market-data/Get-List-Schedule#请求权重ip "请求权重\(IP\)的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Get-List-Schedule#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Get-List-Schedule#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "listTime": 1686161202000,  
        "crossMarginAssets": [  
          "BTC",  
          "USDT"  
        ],  
        "isolatedMarginSymbols": [  
          "ADAUSDT",  
          "BNBUSDT"  
        ]  
      },  
      {  
        "listTime": 1686222232000,  
        "crossMarginAssets": [  
          "ADA"  
        ],  
        "isolatedMarginSymbols": []  
      }  
    ]