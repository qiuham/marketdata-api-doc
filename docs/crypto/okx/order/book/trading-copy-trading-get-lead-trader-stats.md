---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-stats
anchor_id: order-book-trading-copy-trading-get-lead-trader-stats
api_type: API
updated_at: 2026-07-22 19:19:47.315598
---

# GET / Lead trader stats

Public endpoint. Key data related to lead trader performance.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-stats`

> Request example
    
    
    GET /api/v5/copytrading/public-stats?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
lastDays | String | Yes | Last days  
`1`: last 7 days   
`2`: last 30 days  
`3`: last 90 days   
`4`: last 365 days  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "avgSubPosNotional": "213.1038",
                "ccy": "USDT",
                "curCopyTraderPnl": "96.8071",
                "investAmt": "265.095252476476294",
                "lossDays": "1",
                "profitDays": "2",
                "winRatio": "0.6667"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
winRatio | String | Win ratio  
profitDays | String | Profit days  
lossDays | String | Loss days  
curCopyTraderPnl | String | Current copy trader pnl (USDT)  
avgSubPosNotional | String | Average lead position notional (USDT)  
investAmt | String | Investment amount (USDT)  
ccy | String | Margin currency

---

# GET / 获取交易员带单情况

公共接口，获取交易员带单情况。  
  
#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-stats`

> 请求示例
    
    
    GET /api/v5/copytrading/public-stats?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
lastDays | String | 是 | 最近天数  
`1`: 近 7 天   
`2`: 近 30 天  
`3`: 近 90 天，   
`4`: 近 365 天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "avgSubPosNotional": "213.1038",
                "ccy": "USDT",
                "curCopyTraderPnl": "96.8071",
                "investAmt": "265.095252476476294",
                "lossDays": "1",
                "profitDays": "2",
                "winRatio": "0.6667"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
winRatio | String | 胜率  
profitDays | String | 盈利天数  
lossDays | String | 亏损天数  
curCopyTraderPnl | String | 当前跟随者收益 (USDT)  
avgSubPosNotional | String | 平均仓位价值 (USDT)  
investAmt | String | 带单本金 (USDT)  
ccy | String | 保证金币种