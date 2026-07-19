---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-lead-trader-currency-preferences
anchor_id: order-book-trading-copy-trading-get-lead-trader-currency-preferences
api_type: API
updated_at: 2026-07-19 19:15:42.323418
---

# GET / Lead trader currency preferences

Public endpoint. The most frequently traded crypto of this lead trader. Results are sorted by ratio from large to small.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-preference-currency`

> Request example
    
    
    GET /api/v5/copytrading/public-preference-currency?instType=SWAP&uniqueCode=CB4594A3BB5D3538
    
    

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
                "ccy": "ETH",
                "ratio": "0.8881"
            },
            {
                "ccy": "BTC",
                "ratio": "0.0666"
            },
            {
                "ccy": "YFII",
                "ratio": "0.0453"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency  
ratio | String | Ratio. 0.1 represents 10%

---

# GET / 获取交易员币种偏好

公共接口，获取交易员币种偏好，返回结果按 ratio 从大到小排序  
  
#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/copytrading/public-preference-currency`

> 请求示例
    
    
    GET /api/v5/copytrading/public-preference-currency?instType=SWAP&uniqueCode=CB4594A3BB5D3538
    
    

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
                "ccy": "ETH",
                "ratio": "0.8881"
            },
            {
                "ccy": "BTC",
                "ratio": "0.0666"
            },
            {
                "ccy": "YFII",
                "ratio": "0.0453"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种  
ratio | String | 占比，0.1 代表 10%