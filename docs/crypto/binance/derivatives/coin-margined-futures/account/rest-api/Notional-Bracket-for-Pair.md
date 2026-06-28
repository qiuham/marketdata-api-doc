---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair
api_type: Account
updated_at: 2026-01-15T23:37:46.404251
---

# Notional Bracket for Pair(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#api-description "Direct link to API Description")

**Not recommended to continue using this v1 endpoint**

Get the pair's default notional bracket list, may return ambiguous values when there have been multiple different `symbol` brackets under the `pair`, suggest using the following `GET /dapi/v2/leverageBracket` query instead to get the specific `symbol` notional bracket list.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#http-request "Direct link to HTTP Request")

GET `/dapi/v1/leverageBracket`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "pair": "BTCUSD",  
            "brackets": [  
                {  
                    "bracket": 1,   // bracket level  
                    "initialLeverage": 125,  // the maximum leverage  
                    "qtyCap": 50,  // upper edge of base asset quantity  
                    "qtylFloor": 0,  // lower edge of base asset quantity  
                    "maintMarginRatio": 0.004 // maintenance margin rate  
    				"cum": 0.0  // Auxiliary number for quick calculation   
                },  
            ]  
        }  
    ]

---

# 标的交易对默认杠杆分层标准(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#接口描述 "接口描述的直接链接")

**不建议继续使用该 v1 接口**

获取标的交易对默认的杠杆分层标准，当 `pair` 下曾有过多个不同 `symbol` 杠杆分层标准时可能返回歧义值，建议使用下面的 `GET /dapi/v2/leverageBracket` 代替查询以获取具体 `symbol` 杠杆分层标准

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/leverageBracket`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "pair": "BTCUSD",  
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