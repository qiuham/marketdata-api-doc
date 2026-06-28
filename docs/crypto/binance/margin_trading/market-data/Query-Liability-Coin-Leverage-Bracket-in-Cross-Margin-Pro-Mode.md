---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode
api_type: Market Data
updated_at: 2026-01-15T23:48:33.905017
---

# Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#api-description "Direct link to API Description")

Liability Coin Leverage Bracket in Cross Margin Pro Mode

## HTTP Request[​](/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/leverageBracket`

## Request Weight(IP)[​](/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#response-example "Direct link to Response Example")
    
    
    [  
      {  
         "assetNames":[  
            "SHIB",  
            "FDUSD",  
            "BTC",  
            "ETH",  
            "USDC"  
         ],            
         "rank":1,  
         "brackets":[  
            {  
               "leverage":10,  
               "maxDebt":1000000.00000000,  
               "maintenanceMarginRate":0.02000000,  
               "initialMarginRate":0.1112,  
               "fastNum":0  
            },  
            {  
               "leverage":3,  
               "maxDebt":4000000.00000000,  
               "maintenanceMarginRate":0.07000000,  
               "initialMarginRate":0.5000,  
               "fastNum":60000.0000000000000000  
            }  
         ]  
      }  
    ]

---

# Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)

## API Description[​](/docs/zh-CN/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#api-description "API Description的直接链接")

Liability Coin Leverage Bracket in Cross Margin Pro Mode

## HTTP Request[​](/docs/zh-CN/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#http-request "HTTP Request的直接链接")

GET `/sapi/v1/margin/leverageBracket`

## Request Weight(IP)[​](/docs/zh-CN/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#request-weightip "Request Weight\(IP\)的直接链接")

**1**

## Request Parameters[​](/docs/zh-CN/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#request-parameters "Request Parameters的直接链接")

None

## Response Example[​](/docs/zh-CN/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode#response-example "Response Example的直接链接")
    
    
    [  
      {  
         "assetNames":[  
            "SHIB",  
            "FDUSD",  
            "BTC",  
            "ETH",  
            "USDC"  
         ],            
         "rank":1,  
         "brackets":[  
            {  
               "leverage":10,  
               "maxDebt":1000000.00000000,  
               "maintenanceMarginRate":0.02000000,  
               "initialMarginRate":0.1112,  
               "fastNum":0  
            },  
            {  
               "leverage":3,  
               "maxDebt":4000000.00000000,  
               "maintenanceMarginRate":0.07000000,  
               "initialMarginRate":0.5000,  
               "fastNum":60000.0000000000000000  
            }  
         ]  
      }  
    ]