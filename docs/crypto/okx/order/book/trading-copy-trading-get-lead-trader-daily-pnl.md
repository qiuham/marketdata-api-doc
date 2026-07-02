---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-daily-pnl
anchor_id: order-book-trading-copy-trading-get-lead-trader-daily-pnl
api_type: API
updated_at: 2026-07-02 19:43:52.548563
---

# GET / Lead trader daily pnl

Public endpoint. Retrieve lead trader daily pnl. Results are returned in counter chronological order.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/public-pnl`

> Request example
    
    
    GET /api/v5/copytrading/public-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

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
                "beginTs": "1701100800000",
                "pnl": "97.3309",
                "pnlRatio": "0.3672"
            },
            {
                "beginTs": "1701014400000",
                "pnl": "96.7755",
                "pnlRatio": "0.3651"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
beginTs | String | Begin time on that day  
pnl | String | Accumulated pnl  
pnlRatio | String | Accumulated pnl ratio

---

# GET / 获取交易员收益日表现

公共接口，获取交易员每日的收益表现，按时间倒序返回  
  
#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/public-pnl`

> 请求示例
    
    
    GET /api/v5/copytrading/public-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
    
    

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
                "beginTs": "1701100800000",
                "pnl": "97.3309",
                "pnlRatio": "0.3672"
            },
            {
                "beginTs": "1701014400000",
                "pnl": "96.7755",
                "pnlRatio": "0.3651"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
beginTs | String | 当天开始时间  
pnl | String | 累计收益额  
pnlRatio | String | 累计收益率