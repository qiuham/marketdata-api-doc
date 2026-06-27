---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets
api_type: Account
updated_at: 2026-01-15T23:46:29.405886
---

# Notional and Leverage Brackets (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#api-description "Direct link to API Description")

Query user notional and leverage bracket on speicfic symbol

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#http-request "Direct link to HTTP Request")

GET `/fapi/v1/leverageBracket`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#response-example "Direct link to Response Example")

> **Response:**
    
    
    [  
        {  
            "symbol": "ETHUSDT",  
    	    "notionalCoef": 1.50,  //user symbol bracket multiplier, only appears when user's symbol bracket is adjusted   
            "brackets": [  
                {  
                    "bracket": 1,   // Notional bracket  
                    "initialLeverage": 75,  // Max initial leverage for this bracket  
                    "notionalCap": 10000,  // Cap notional of this bracket  
                    "notionalFloor": 0,  // Notional threshold of this bracket   
                    "maintMarginRatio": 0.0065, // Maintenance ratio for this bracket  
                    "cum": 0.0 // Auxiliary number for quick calculation   
                     
                },  
            ]  
        }  
    ]  
    

> **OR** (if symbol sent)
    
    
      
    {  
        "symbol": "ETHUSDT",  
        "notionalCoef": 1.50,  
        "brackets": [  
            {  
                "bracket": 1,  
                "initialLeverage": 75,  
                "notionalCap": 10000,  
                "notionalFloor": 0,  
                "maintMarginRatio": 0.0065,  
                "cum":0  
            },  
        ]  
    }

---

# 杠杆分层标准 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#接口描述 "接口描述的直接链接")

查询账户特定交易对的杠杆分层标准

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/leverageBracket`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    [  
        {  
            "symbol": "ETHUSDT",  
    	    "notionalCoef": 1.50,   //用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示  
            "brackets": [  
                {  
                    "bracket": 1,   // 层级  
                    "initialLeverage": 75,  // 该层允许的最高初始杠杆倍数  
                    "notionalCap": 10000,  // 该层对应的名义价值上限  
                    "notionalFloor": 0,  // 该层对应的名义价值下限   
                    "maintMarginRatio": 0.0065, // 该层对应的维持保证金率  
                    "cum": 0.0 // 速算数  
                },  
            ]  
        }  
    ]  
    

> **或** (若发送symbol)
    
    
      
    {  
        "symbol": "ETHUSDT",  
        "notionalCoef": 1.50,  
        "brackets": [  
            {  
                "bracket": 1,  
                "initialLeverage": 75,  
                "notionalCap": 10000,  
                "notionalFloor": 0,  
                "maintMarginRatio": 0.0065,  
                "cum":0  
            },  
        ]  
    }