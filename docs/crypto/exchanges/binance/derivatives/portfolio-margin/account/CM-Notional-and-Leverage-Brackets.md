---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets
api_type: Account
updated_at: 2026-01-15T23:44:32.046185
---

# CM Notional and Leverage Brackets(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#api-description "Direct link to API Description")

Query CM notional and leverage brackets

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/leverageBracket`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BTCUSD_PERP",  
            "brackets": [  
                {  
                    "bracket": 1,   // bracket level  
                    "initialLeverage": 125,  // the maximum leverage  
                    "qtyCap": 50,  // upper edge of base asset quantity  
                    "qtyFloor": 0,  // lower edge of base asset quantity  
                    "maintMarginRatio": 0.004, // maintenance margin rate  
                    "cum": 0.0 // Auxiliary number for quick calculation   
                },  
            ]  
        }  
    ]

---

# 查询CM杠杆分层标准(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#接口描述 "接口描述的直接链接")

查询CM杠杆分层标准

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/leverageBracket`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BTCUSD_PERP",  
            "brackets": [  
                {  
                    "bracket": 1,   // 层级  
                    "initialLeverage": 125,  // 该层允许的最高初始杠杆倍数  
                    "qtyCap": 50,  // 该层对应的数量上限  
                    "qtyFloor": 0,  //  该层对应的数量下限   
                    "maintMarginRatio": 0.004, // 该层对应的维持保证金率  
                    "cum": 0.0 // 速算数  
                }  
            ]  
        }  
    ]