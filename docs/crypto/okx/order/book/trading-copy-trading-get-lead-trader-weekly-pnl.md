---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-weekly-pnl
anchor_id: order-book-trading-copy-trading-get-lead-trader-weekly-pnl
api_type: API
updated_at: 2026-07-01 19:54:28.260965
---

# GET / Lead trader weekly pnl

Public endpoint. Retrieve lead trader weekly pnl. Results are returned in counter chronological order.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/public-weekly-pnl`

> Request example
    
    
    GET /api/v5/copytrading/public-weekly-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "beginTs": "1701014400000",
                "pnl": "-2.8428",
                "pnlRatio": "-0.0106"
            },
            {
                "beginTs": "1700409600000",
                "pnl": "81.8446",
                "pnlRatio": "0.3036"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
beginTs | String | Begin time of pnl ratio on that week  
pnl | String | Pnl on that week  
pnlRatio | String | Pnl ratio on that week

---

# GET / 获取交易员收益周表现

公共接口，获取交易员最近12周的收益表现，按时间倒序返回  
  
#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/public-weekly-pnl`

> 请求示例
    
    
    GET /api/v5/copytrading/public-weekly-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "beginTs": "1701014400000",
                "pnl": "-2.8428",
                "pnlRatio": "-0.0106"
            },
            {
                "beginTs": "1700409600000",
                "pnl": "81.8446",
                "pnlRatio": "0.3036"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
beginTs | String | 当周收益率的开始时间  
pnl | String | 当周收益额  
pnlRatio | String | 当周收益率