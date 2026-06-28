---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/account
api_type: Account
updated_at: 2026-01-15T23:40:51.777866
---

# Option Margin Account Information (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/account#api-description "Direct link to API Description")

Get current account information.

## HTTP Request[​](/docs/derivatives/options-trading/account#http-request "Direct link to HTTP Request")

GET `/eapi/v1/marginAccount`

## Request Weight[​](/docs/derivatives/options-trading/account#request-weight "Direct link to Request Weight")

**3**

## Request Parameters[​](/docs/derivatives/options-trading/account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/account#response-example "Direct link to Response Example")
    
    
    {  
        "asset": [  
            {  
                "asset": "USDT",                     // Asset type  
                "marginBalance": "99998.87365244",   // Account balance  
                "equity": "99998.87365244",          // Account equity  
                "available": "96883.72734374",       // Available funds  
                "initialMargin": "3115.14630870",    // Initial margin  
                "maintMargin": "0.00000000",         // Maintenance margin  
                "unrealizedPNL": "0.00000000",       // Unrealized profit/loss  
                "adjustedEquity": "99998.87365244"   // margin balance + qualified Long Position Value  
            }  
        ],  
        "greek": [  
            {  
                "underlying": "BTCUSDT",    // Option Underlying  
                "delta": "0",               // Account delta  
                "theta": "0",               // Account theta  
                "gamma": "0",               // Account gamma  
                "vega": "0"                 // Account vega    
            }  
        ],  
        "time": 1762843368098,  
        "canTrade": true,  
        "canDeposit": true,  
        "canWithdraw": true,  
        "reduceOnly": false  
    }

---

# 保证金账户信息

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/account#接口描述 "接口描述的直接链接")

获取保证金账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/account#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/marginAccount`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/account#请求权重 "请求权重的直接链接")

3

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| NO|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/account#响应示例 "响应示例的直接链接")
    
    
     {  
      "asset": [                    
        {  
          "asset": "USDT",                    // 资产  
          "marginBalance": "10099.448"        // 账户余额  
          "equity": "10094.44662",              
          "available": "8725.92524",            
          "initialMargin": "1084.52138",        
          "maintMargin": "151.00138",           
          "unrealizedPNL": "-5.00138",          
          "adjustedEquity": "34.13282285"       
         }  
      ],   
      "greek": [  
        {  
          "underlying":"BTCUSDT"                
          "delta": "-0.05"                      
          "gamma": "-0.002"                     
          "theta": "-0.05"                      
          "vega": "-0.002"                      
        }  
      ],  
      "time": 1592449455993                   // 时间    
    }  
    {  
        "asset": [  
            {  
                "asset": "USDT",                     // 资产  
                "marginBalance": "99998.87365244",   // 账户余额  
                "equity": "99998.87365244",          // 账户权益  
                "available": "96883.72734374",       // 账户可用  
                "initialMargin": "3115.14630870",    // 初始保证金  
                "maintMargin": "0.00000000",         // 维持保证金  
                "unrealizedPNL": "0.00000000",       // 未实现盈亏  
                "adjustedEquity": "99998.87365244"   // margin balance + BTC多仓价值  
            }  
        ],  
        "greek": [  
            {  
                "underlying": "BTCUSDT",             // 标的资产  
                "delta": "0",                        // delta  
                "theta": "0",                        // theta  
                "gamma": "0",                        // gamma  
                "vega": "0"                          // vega    
            }  
        ],  
        "time": 1762843368098,  
        "canTrade": true,  
        "canDeposit": true,  
        "canWithdraw": true,  
        "reduceOnly": false  
    }