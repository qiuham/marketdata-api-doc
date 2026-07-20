---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-activate-option
anchor_id: trading-account-rest-api-activate-option
api_type: REST
updated_at: 2026-07-20 19:35:16.528149
---

# Activate option

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/activate-option`

> Request Example
    
    
    POST /api/v5/account/activate-option
    
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ts": "1600000000000"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Activation time

---

# 开通期权交易

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/activate-option`

> 请求示例
    
    
    POST /api/v5/account/activate-option
    
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ts": "1600000000000"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 开通时间