---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol
api_type: Account
updated_at: 2026-01-15T23:37:51.713812
---

# Notional Bracket for Symbol(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#api-description "Direct link to API Description")

Get the symbol's notional bracket list.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#http-request "Direct link to HTTP Request")

GET `/dapi/v2/leverageBracket`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BTCUSD_PERP",  
            "notionalCoef": 1.50,  //user symbol bracket multiplier, only appears when user's symbol bracket is adjusted   
            "brackets": [  
                {  
                    "bracket": 1,   // bracket level  
                    "initialLeverage": 125,  // the maximum leverage  
                    "qtyCap": 50,  // upper edge of base asset quantity  
                    "qtylFloor": 0,  // lower edge of base asset quantity  
                    "maintMarginRatio": 0.004 // maintenance margin rate  
    				"cum": 0.0 // Auxiliary number for quick calculation   
                },  
            ]  
        }  
    ]

---

# 交易对杠杆分层标准 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#接口描述 "接口描述的直接链接")

获取交易对的杠杆分层标准

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#http请求 "HTTP请求的直接链接")

GET `/dapi/v2/leverageBracket`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BTCUSD_PERP",  
            "notionalCoef": 1.50,   //用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示  
            "brackets": [  
                {  
                    "bracket": 1,   // 层级  
                    "initialLeverage": 125,  // 该层允许的最高初始杠杆倍数  
                    "qtyCap": 50,  // 该层对应的数量上限  
                    "qtylFloor": 0,  // 该层对应的数量下限   
                    "maintMarginRatio": 0.004 // 该层对应的维持保证金率  
    				"cum": 0.0  //速算数  
                },  
            ]  
        }  
    ]