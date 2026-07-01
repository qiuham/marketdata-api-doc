---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-auto-repay
anchor_id: trading-account-rest-api-set-auto-repay
api_type: REST
updated_at: 2026-07-01 19:53:31.611938
---

# Set auto repay

Only applicable to `Spot mode` (enabled borrowing)  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-auto-repay`

> Request Example
    
    
    POST /api/v5/account/set-auto-repay
    body
    {
        "autoRepay": true
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.set_auto_repay(autoRepay=True)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
autoRepay | Boolean | Yes | Whether auto repay is allowed or not under `Spot mode`  
`true`: Enable auto repay  
`false`: Disable auto repay  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "autoRepay": true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
autoRepay | Boolean | Whether auto repay is allowed or not under `Spot mode`  
`true`: Enable auto repay  
`false`: Disable auto repay

---

# 设置自动还币

仅适用于`现货模式`已开通借币的情况。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-auto-repay`

> 请求示例
    
    
    POST /api/v5/account/set-auto-repay
    body
    {
        "autoRepay": true
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.set_auto_repay(autoRepay=True)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
autoRepay | Boolean | 是 | 是否支持`现货模式`下自动还币  
`true`：支持  
`false`：不支持  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "autoRepay": true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
autoRepay | Boolean | 是否支持`现货模式`下自动还币  
`true`：支持  
`false`：不支持