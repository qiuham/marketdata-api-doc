---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-convert-currencies
anchor_id: funding-account-rest-api-get-convert-currencies
api_type: REST
updated_at: 2026-07-18 20:05:00.762093
---

# Get convert currencies

#### Rate Limit: 6 requests per second  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/convert/currencies`

> Request Example
    
    
    GET /api/v5/asset/convert/currencies
    
    

#### Response parameters

none

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "min": "",  // Deprecated
                "max": "",  // Deprecated
                "ccy": "BTC"
            },
            {
                "min": "",
                "max": "",
                "ccy": "ETH"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. BTC  
min | String | Minimum amount to convert ( Deprecated )  
max | String | Maximum amount to convert ( Deprecated )

---

# 获取闪兑币种列表

#### 限速：6次/s  
  
#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/asset/convert/currencies`

> 请求示例
    
    
    GET /api/v5/asset/convert/currencies
    
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "min": "",  // 已废弃
                "max": "",  // 已废弃
                "ccy": "BTC"
            },
            {
                "min": "",
                "max": "",
                "ccy": "ETH"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
min | String | ~~支持闪兑的最小值~~(已废弃)  
max | String | ~~支持闪兑的最大值~~(已废弃)