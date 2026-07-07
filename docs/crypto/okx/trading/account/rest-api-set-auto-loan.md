---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-auto-loan
anchor_id: trading-account-rest-api-set-auto-loan
api_type: REST
updated_at: 2026-07-07 19:41:30.030297
---

# Set auto loan

Only applicable to `Multi-currency margin` and `Portfolio margin`  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-auto-loan`

> Request Example
    
    
    POST /api/v5/account/set-auto-loan
    body
    {
        "autoLoan":true,
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
autoLoan | Boolean | No | Whether to automatically make loans   
Valid values are `true`, `false`   
The default is `true`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "autoLoan": true
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
autoLoan | Boolean | Whether to automatically make loans

---

# 设置自动借币

仅适用于跨币种保证金模式和组合保证金模式  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-auto-loan`

> 请求示例
    
    
    POST /api/v5/account/set-auto-loan
    body
    {
        "autoLoan":true,
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
autoLoan | Boolean | 否 | 是否自动借币   
有效值为`true`, `false`  
默认为 `true`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "autoLoan": true
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
autoLoan | Boolean | 是否自动借币