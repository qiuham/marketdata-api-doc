---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-exchange-list-public
anchor_id: funding-account-rest-api-get-exchange-list-public
api_type: REST
updated_at: 2026-07-19 19:16:45.173053
---

# Get exchange list (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/asset/exchange-list`

> Request Example
    
    
    GET /api/v5/asset/exchange-list
    
    
    
    
    

#### Request Parameters

None

> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "exchName": "1xbet"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
exchName | String | Exchange name, e.g. `1xbet`  
exchId | String | Exchange ID, e.g. `did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1`

---

# 获取交易所列表（公共）

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/asset/exchange-list`

> 请求示例
    
    
    GET /api/v5/asset/exchange-list
    
    
    
    

#### 请求参数

无

> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "exchName": "1xbet"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
exchName | String | 交易所名称，如 `1xbet`  
exchId | String | 交易所 ID，如 `did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1`