---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-settle-currency
anchor_id: trading-account-rest-api-set-settle-currency
api_type: REST
updated_at: 2026-07-14 19:18:52.299012
---

# Set settle currency

Only applicable to USD-margined contract.  
  
#### Rate limit: 20 times per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trading

#### HTTP Request

`POST /api/v5/account/set-settle-currency`

> Request Example
    
    
    POST /api/v5/account/set-settle-currency
    body
    {
        "settleCcy": "USDC"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
settleCcy | String | Yes | USD-margined contract settle currency  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "settleCcy":"USDC"
              }
        ]  
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
settleCcy | String | USD-margined contract settle currency

---

# 设置结算币种

仅适用于 USD 本位合约。  
  
#### 限速：20 次/2 秒

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/account/set-settle-currency`

> 请求示例
    
    
    POST /api/v5/account/set-settle-currency
    body
    {
        "settleCcy": "USDC"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
settleCcy | String | 是 | USD 本位合约结算币种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "settleCcy":"USDC"
              }
        ]  
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
settleCcy | String | USD 本位合约结算币种